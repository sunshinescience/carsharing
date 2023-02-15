import json

from pydantic import BaseModel
from typing import Optional

# The classes we write here will define the shape of the valid data structures that our API will accept
# And the document that defines such a structure is called a schema
# In the FastAPI world, we use a library called pydantic to create our schema classes

# Creating a class, CarInput, by inheriting from BaseModel which is a Pydantic class
# Note that you can add default values so that these aren't necessary to include, for e.g., fuel and transmission
# Note that Pydantic BaseModel expects a bunch of keyword arguments (e.g., size="s", doors="3", id="6")

class TripInput(BaseModel):
    start: int
    end: int
    description: str
    

class TripOutput(TripInput):
    id: int


class CarInput(BaseModel):
    size: str
    fuel: Optional[str] = "electric"
    doors: int
    transmission: Optional[str] = "auto"

    class Config:
        schema_extra = {
            "example": {
                "size": "m",
                "doors": 5,
                "transmission": "manual",
                "fuel": "hybrid"
            }
        }

class CarOutput(CarInput):
    id: int
    trips: list[TripOutput] = []


def load_db() -> list[CarOutput]:
    """Load a list of Car objects from a JSON file"""
    with open("cars.json") as f:
        return [CarOutput.parse_obj(obj) for obj in json.load(f)]


def save_db(cars: list[CarOutput]):
    with open("cars.json", 'w') as f:
        json.dump([car.dict() for car in cars], f, indent=4)

