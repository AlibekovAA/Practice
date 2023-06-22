import random

#from Data.data import Person

from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()

def generated_pass_number():

    yield random.randint(1000000, 9000000)
#
# def generated_person():
#     yield Person(
#         full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
#         firstname=faker_ru.first_name(),
#         lastname=faker_ru.last_name(),
#         midlname=faker_ru.middle_name(),
#         age=random.randint(20,50),
#         department=faker_ru.job(),
#         salary=random.randint(1000,5000),
#
#         email=faker_ru.email(),
#         current_address=faker_ru.address(),
#         permanent_address=faker_ru.address(),
#
#         mobile = faker_ru.msisdn(),
#         birth_date=faker_ru.date(),
#
#
#     )

def generated_true_or_false():
    if 0 == random.randint(0, 100) % 2:
        return True
    else:
        return False

# def generated_time():
#     return time_start, time_end
#
