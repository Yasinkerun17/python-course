my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

for i, j in my_vehicle.items():
    print(f"{i} : {j}")

vehicle2 = my_vehicle.copy()

vehicle2["number_of_tires"] = 4

vehicle2.pop("mileage")

for x in vehicle2:
    print(x)
    