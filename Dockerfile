FROM continuumio/miniconda3:latest as build

COPY environment.yml .
RUN conda env create -f environment.yml

# Install conda-pack:
RUN conda install -c conda-forge conda-pack
# Use conda-pack to create a standalone enviornment
# in /venv:
RUN conda-pack -n fast-api-demo -o /tmp/env.tar && \
  mkdir /venv && cd /venv && tar xf /tmp/env.tar && \
  rm /tmp/env.tar
# We've put venv in same path it'll be in final image,
# so now fix up paths:
RUN /venv/bin/conda-unpack

FROM ubuntu:20.04 as runtime

# Create non-root user for container
ARG USER=jovyan
ARG APP_HOME=/home/jovyan

RUN adduser --system --group $USER \
    && mkdir -p $APP_HOME \
    && chown -R $USER:$USER $APP_HOME

# Copy /venv from the previous stage:
COPY . ${APP_HOME}
COPY --from=build /venv ${APP_HOME}/src/venv

# Start container as non-root user
USER $USER
WORKDIR ${APP_HOME}/src
# When image is run, run the code with the environment
# activated:
CMD ["/bin/bash", "-c", "source venv/bin/activate && uvicorn main:app --host 0.0.0.0"]
EXPOSE 8000