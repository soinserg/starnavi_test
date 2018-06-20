from django.core.management import BaseCommand
from faker import Faker

from apps.account.models import User


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('number_of_users', type=int)

    def handle(self, *args, **options):
        try:
            User.objects.get(is_superuser=True)
        except User.DoesNotExist:
            User.objects.create_superuser('admin', '', 'admin')

        fake = Faker('ru_RU')
        for i in range(options['number_of_users']):
            User.objects.create(
                username=fake.user_name(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                city=fake.city(),
                job=fake.job(),
                status=fake.sentence()
            )
