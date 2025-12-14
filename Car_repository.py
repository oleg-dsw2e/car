import csv

path = "users.csv"

class Car:
    def __init__(self, id, model, car_number):
        self.__id = id
        self.__model = model
        self.__car_number = car_number

    def __str__(self):
        return f"id: {self.__id}, model: {self.__model}, car_number: {self.__car_number}"


    def __dict__(self):
        return {
            "id": self.__id,
            "model": self.__model,
            "car_number": self.__car_number
        }

    @property
    def id(self):
        return self.__id

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def car_number(self):
        return self.__car_number

    @car_number.setter
    def car_number(self, value):
        self.__car_number = value

class Car_repository:

    def __init__(self, file_path):
        self.__path = file_path

    def get_all(self):
        cars = list()
        with open(self.__path, "r", encoding="UTF-8") as file:
            reader = csv.reader(file)
            for row in reader:
                car = Car(row[0], row[1], (row[2]))
                cars.append(car)
        return cars


    def get_by_id(self):
        with open(self.__path, "r", encoding="UTf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                car = Car(row[0], row[1], int(row[2]))
                if car.id == id:
                    return car
            return None

    def __add__(self, car):
        with open(self.__path, "a", newline="") as file:
            writer = csv.DictWriter(file, ["id", "model", "car_number"])
            writer.writerow(car.__dict__())

    def update(self, car):
        cars = self.get_all()
        for i in cars:
            if int(i.id) == int(car.id):
                i.model = car.model
                i.car_number = car.car_number
        self.write_all(cars)

    def write_all(self, cars):
        with open(self.__path, "a", newline="") as file:
            writer = csv.DictWriter(file, ["id", "model", "car_number"])
            for i in cars:
                writer.writerow(i.__dict__)

    def del_by_id(self, id):
        cars = self.get_all()
        initial_count = len(cars)

        cars = [car for car in cars if car.id != id]

        if len(cars) < initial_count:
            self.write_all(cars)
            return True
        return False

    def delete_all(self):

        with open(self.__path, "w", newline="", encoding="UTF-8") as file:
            writer = csv.writer(file)
            writer.writerow([])
