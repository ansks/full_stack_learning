import os
from django import setup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
setup()

from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()

import random

topics = ['Search', 'Social', 'Market', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(topic_name = random.choice(topics))[0]
    t.save()
    return t

def populate(n = 5):

    for i in range(n):

        # Get topic for the entry
        topic = add_topic()

        # Create face data for the entry 
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.name()

        # Create web page entry:
        webpage = Webpage.objects.get_or_create(topic_name = topic, name = fake_name, url = fake_url)[0]
        
        # Create a fake access record for that webpage
        acc_record = AccessRecord.objects.get_or_create(name = fake_name, date = fake_date)[0]

if __name__ == '__main__':
    print('Populating script:')
    populate(20)
    print('Populating script finished!')



    



