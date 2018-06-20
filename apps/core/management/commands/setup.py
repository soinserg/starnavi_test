import random

from django.core.management import BaseCommand, CommandError
from faker import Faker

from apps.account.models import User
from apps.post.models import Post, PostVote


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('number_of_users', type=int)
        parser.add_argument('max_posts_per_user', type=int)
        parser.add_argument('max_likes_per_user', type=int)

    def handle(self, *args, **options):
        if options['number_of_users'] < 0 or \
           options['max_posts_per_user'] < 0 or \
           options['max_likes_per_user'] < 0:
            raise CommandError('All args must be non-negative')

        fake = Faker('ru_RU')

        try:
            User.objects.get(is_superuser=True)
        except User.DoesNotExist:
            User.objects.create_superuser('admin', 'admin@dev.com', 'admin')

        for i in range(options['number_of_users']):
            User.objects.create_user(
                username=fake.user_name(),
                password=fake.password(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                city=fake.city(),
                job=fake.job(),
                status=fake.sentence()
            )
        self.stdout.write('Generated users: %s' % options['number_of_users'])

        counter = 0
        for user in User.objects.visitors():
            for i in range(random.randint(0, options['max_posts_per_user'])):
                Post.objects.create(
                    text=fake.text(),
                    author=user
                )
                counter += 1
        self.stdout.write('Generated posts: %s' % counter)

        counter = 0
        for user in User.objects.visitors():
            for i in range(random.randint(0, options['max_likes_per_user'])):
                PostVote.objects.create(
                    value=random.choice((-1, 1)),
                    author=user,
                    post=random.choice(Post.objects.all())
                )
                counter += 1
        self.stdout.write('Generated post\'s votes : %s' % counter)
