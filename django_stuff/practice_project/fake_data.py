import os
from django import setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practice_project.settings')
setup()

from faker import Faker
from practice_app.models import userlist

fake = Faker()

def fake_user(n = 20):

    for i in range(n):
        name = fake.name()
        email_add = fake.email()

        userlist.objects.get_or_create(first_name = name.split(" ")[0],
                                    last_name = name.split(" ")[1], 
                                    email = email_add
                                    )[0]


if __name__ == '__main__':
    print('Generating user !')
    fake_user(10)
    print('Finished generating users !')



