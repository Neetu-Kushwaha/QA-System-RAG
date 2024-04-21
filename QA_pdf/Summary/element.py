from typing import Any
from pydantic import BaseModel


class Element(BaseModel):
    """
    Class to represent an element extracted from PDF.

    Attributes:
        type (str): Type of the element.
        text (Any): Text content of the element.
    """
    type: str
    text: Any
