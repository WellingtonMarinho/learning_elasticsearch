import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LearningElastic.settings')
django.setup()


from faker import Faker
from validate_docbr import CPF
from core.models import People

def criando_pessoas(quantidade_pessoas):
    for data in range(quantidade_pessoas):
        fake = Faker(['fr_FR', 'pt_PT', 'it_IT', 'en_US', 'pt_BR'])
        name = fake.name()
        address = fake.address()
        birthdate = fake.date_between(end_date='today')
        # print(name, address, birthdate)
        obj = People(name=name, address=address, birthdate=birthdate)
        obj.save()

criando_pessoas(150)
print('Sucesso ao popular a base de dados.')