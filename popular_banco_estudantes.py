from escola.models import Estudante
import random
from validate_docbr import CPF
from faker import Faker
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()


def criando_pessoas(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        nome = fake.name()
        email = '{}@{}'.format(nome.lower(), fake.free_email_domain())
        email = email.replace(' ', '')
        cpf = cpf.generate()
        # Gera uma data de nascimento aleatória entre 18 e 30 anos
        data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=30)
        celular = "{} 9{}-{}".format(random.randrange(10, 89),
                                     random.randrange(4000, 9999), random.randrange(4000, 9999))
        p = Estudante(nome=nome, email=email, cpf=cpf,
                      data_nascimento=data_nascimento, celular=celular)
        p.save()


criando_pessoas(100)
