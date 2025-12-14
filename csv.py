from car_repository import *

if __name__ == '__main__':
    repository = Car_repository("users.csv")

    # # cars = repository.get_all()
    # # for i in cars:
    # #     print(i)
    #
    # car = repository.get_by_id("2")
    # print(car)
    #
    # new_car = Car("5", "Mercedes", "777")
    # repository.add(new_car)

    for i in repository.get_all():
        print(i)