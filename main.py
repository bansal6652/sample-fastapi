from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class supercar(BaseModel):
    ID : int
    make : str
    Model : str
    year : int
    price : int


cars : List[supercar] = []

@app.get("/")
def garage():
    return {"message":"Welcome to the garage"}

@app.get("/cars")
def listcars():
    return cars

# @app.get("/cars/{carid}")
# def getcarbyID(carid : int):
#     for key,val in enumerate(cars):
#         if val.ID == carid:
#             return val
        
@app.get("/cars/{brand}")
def getcarbybrand(brand : str):
    result : List[supercar] = []
    for key,val in enumerate(cars):
        if val.make == brand:
            result.append(val)
    return result

@app.post("/cars")
def addcar(car : supercar):
    cars.append(car)
    return car

@app.put("/cars/{carid}")
def updatecar(carid : int, updated_car : supercar):
    for index,value in enumerate(cars):
        if value.ID == carid:
            cars[index] = updated_car
            return updated_car
    return {"error":"No Cars were found"}


@app.delete("/cars/{carid}")
def deletecar(carid : int):
    for index,value in enumerate(cars):
        if(value.ID == carid):
            deleted = cars.pop(index)
            return deleted
    return {"error":"No Cars were found"}