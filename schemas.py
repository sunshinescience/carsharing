import json
from typing import List

from pydantic import BaseModel
from typing import Optional

# The classes we write here will define the shape of the valid data structures that our API will accept
# And the document that defines such a structure is called a schema
# In the FastAPI world, we use a library called pydantic to create our schema classes

# Creating a class, CarInput, by inheriting from BaseModel which is a Pydantic class
# Note that you can add default values so that these aren't necessary to include, for e.g., fuel and transmission
# Note that Pydantic BaseModel expects a bunch of keyword arguments (e.g., size="s", doors="3", id="6")

class CarInput(BaseModel):
    size: str
    fuel: Optional[str] = "electric"
    doors: int
    transmission: Optional[str] = "auto"

class CarOutput(CarInput):
    id: int

def load_db() -> list[CarOutput]:
    """Load a list of Car objects from a JSON file"""
    with open("cars.json") as f:
        return [CarOutput.parse_obj(obj) for obj in json.load(f)]

def save_db(cars: list[CarOutput]):
    with open("cars.json", 'w') as f:
        json.dump([car.dict() for car in cars], f, indent=4)
