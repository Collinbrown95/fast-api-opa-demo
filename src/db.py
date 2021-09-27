"""
Fake database model to simulate users' input data
"""
from typing import Dict
from typing import Tuple

from fastapi import status
from fastapi.responses import JSONResponse


class DB:
    """
    A dummy database model class to illustrate getting user data.
    """

    @staticmethod
    def get_input(id: int, kind: str) -> Tuple[Dict, int]:
        if kind in DB.data.keys():
            res = [item for item in DB.data[kind] if item["id"] == id]
            if res:
                return res.pop()
        msg: str = {"message": "No proprietary input matches the id specified."}
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=msg)

    @staticmethod
    def get_inputs(kind: str) -> Tuple[Dict, int]:
        if kind in DB.data.keys():
            return DB.data[kind]
        msg: str = {"message": "No user matches the given username"}
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=msg)

    data: Dict = {
        "proprietary": [
            {"id": 1, "input": "Avatar was fine, 5/10", "label": "Neutral"},
            {
                "id": 2,
                "input": "The Room is the best movie ever made!",
                "label": "Positive",
            },
            {
                "id": 3,
                "input": "I would never see that movie again. Terrible!",
                "label": "Negative",
            },
        ],
        "beta_release": [
            {
                "id": 1,
                "input": "This was the best show I've ever seen!",
                "label": "Positive",
            },
            {
                "id": 2,
                "input": "I wouldn't recommend that series to anyone",
                "label": "Negative",
            },
        ],
    }
