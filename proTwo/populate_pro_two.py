import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

from Apptwo.models import User
from faker import Faker


fakegen=Faker()


def populate(N=5):
    for entry in range(N):
        #get the topic for entry



        #Create fake data for that entry
        fake_firstname=fakegen.firstname()
        fake_lastname=fakegen.lastname()
        fake_email=fakegen.email()

        webpg=Webpage.objects.get_or_create(FirstName=fake_firstname,LastName=fake_lastname,Email=fake_email)[0]



if __name__ == '__main__':
    print ('populating SCRIPT!!!!!!!!!')
    populate(20)
    print ('populate complete!!!!!!!!')
