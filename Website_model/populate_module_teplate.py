import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Website_model.settings')

import django
django.setup()

import random
from model_template.models import AccessRecord,Topic,Webpage
from faker import Faker

fakegen = Faker() #object of Faker class is created.Faker class is imported
topics = ['Search','Social','Marketplace','News']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0] #create random names and save it
    t.save()
    return t

def populate(N):

    top = add_topic()

    for entry in range(N):
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpage = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        acc_rec = AccessRecord.objects.get_or_create(name = webpage,date=fake_date)[0]

if __name__== '__main__':
    print("Populated Script!!")
    populate(20)
    print("Populating complete.")
