from django.core.management.base import BaseCommand
from faker import Faker
import faker.providers
from firstapp.models import Teacher, Student, Department
from random import randint

departments = list(Department.objects.all())


class DataProvider(faker.providers.BaseProvider):
    def get_departments(self):
        return self.random_element(departments)

    def get_list_departments(self):
        l = randint(1, 3)
        return self.random_elements(departments, length=l, unique=True)


class Command(BaseCommand):
    help = 'creates new data'

    def handle(self, *args, **options):
        fake = Faker()
        fake.add_provider(DataProvider)
        print(fake.name())
        print(fake.get_departments())
        print(fake.get_list_departments())

        # for _ in range(50):
        #     name = fake.name()
        #     roll_no = fake.unique.random_int(5, 100)
        #     department = fake.get_departments()
        #     Student.objects.create(name=name, roll_no=roll_no, department=department)

        # for _ in range(20):
        #     name = fake.name()
        #     emp_id = fake.unique.random_int(200, 500)
        #     dept = fake.get_list_departments()
        #     teacher = Teacher.objects.create(name=name, emp_id=emp_id)
        #     teacher.department.set(dept)
