from django.core.management.base import BaseCommand, CommandError
from ._private import create_grades

def random_grade():
    fake_grade = randint(1,6)
    return fake_grade

class Command(BaseCommand):
    help = 'Populates school with students, subjects and teachers'

    def handle(self, *args, **options):
        create_grades()
        self.stdout.write(self.style.SUCCESS("Succesfully populated school "
                                             "with students"))