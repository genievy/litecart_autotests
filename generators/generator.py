from data.data import Customer

from faker import Faker

fake_ru = Faker('ru_RU')
fake_en = Faker('En')


"""
Функция с yield возвращает генератор (не хранит значение в памяти,
а генерирует их "на лету" каждый раз при обращении к ней
"""


def random_custumer():
    yield Customer(
        company=fake_ru.company(),
        tax_id=fake_ru.numerify(),
        first_name=fake_ru.first_name(),
        last_name=fake_ru.last_name(),
        address_1=fake_ru.address(),
        address_2=fake_ru.address(),
        postal_code=fake_ru.postcode(),
        city=fake_ru.city(),
        email=fake_ru.email(),
        phone=fake_ru.phone_number(),
        password=fake_ru.password(),
        captcha=fake_ru.password(),
        )
