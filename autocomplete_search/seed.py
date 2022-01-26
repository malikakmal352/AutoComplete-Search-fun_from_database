from .models import Lab
from faker import Faker

faker = Faker()


def seed_db(n):
    for i in range(0, n):
        Lab.objects.create(
            Labname=faker.name(),
            Address=faker.name()
        )
