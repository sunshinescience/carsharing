import uvicorn
from fastapi import FastAPI, HTTPException
from typing import Optional, List
#from typing import List

# from schemas import Car
from schemas import load_db, save_db, CarInput, CarOutput

app = FastAPI()

db = load_db()

@app.get("/api/cars")
# def get_cars(size: str | None = None, doors: int | None = None) -> list:
def get_cars(size: Optional[str] = None, doors: Optional[int] = None) -> List: # If the new parameter is required (for example if the parameter was onle size, then we would get an error if a size was not given and couldn't access the db, but we can fix that by adding a default value of None, so write in the parameter size=None)
# If using the above (and below) type hints (the older syntax), then import Optional and import List
# def get_cars(size: str|None = None, doors: int|None = None) -> List: 
    result = db
    if size: 
        result = [car for car in result if car['size'] == size]
    if doors: 
        result = [car for car in result if car['doors'] >= doors]
    return result

@app.get("/api/cars/{id}")
def car_by_id(id: int) -> dict:
    result = [car for car in db if car.id == id]
    #print(f"in call_by_id, id = {id}")
    if result:
        return result[0]
    else:
        raise HTTPException(status_code=404, detail=f'No car with id {id}.')

# @app.post("/api/cars/", response_model=CarOutput)
# def add_car(car: CarInput) -> CarOutput:
#     new_car = CarOutput(size=car.size, doors=car.doors,
#                         fuel=car.fuel, transmission=car.transmission,
#                         id=len(db)+1)
#     db.append(new_car)
#     save_db(db)
#     return new_car

# Should the above car: have a type hint, it has CarInput, but is that wrong?

if __name__ == "__main__":
    uvicorn.run("carsharing:app", reload=True)

