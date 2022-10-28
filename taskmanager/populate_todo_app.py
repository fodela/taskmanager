# Configure settings
from faker import Faker


import random
import django
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taskmanager.settings")


# Django setup
django.setup()


"""
Populate the database with fake information
"""
from todo_app.models import Task, TaskCategory

fake_generator = Faker()    

categories = ["academics", "career", "growth",
              "relationship", "spiritual life"]
states = [True, False]


def add_category() -> TaskCategory:
    category = TaskCategory.objects.get_or_create(
        name=random.choice(categories))[0]

    category.save()
    return category


def populate_database(N=5) -> None:
    for entry in range(N):

        # Get the task category and state
        cat = add_category()

        # Create the fake data for that entry
        fake_task = fake_generator.sentence(nb_words=10)

        task = Task.objects.get_or_create(
            description=fake_task, category=cat
        )[0]


if __name__ == "__main__":
    print("populating script \nPlease wait ...")

    populate_database(20)
    print("population completed")
