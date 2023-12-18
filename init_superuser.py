import os

from django.core.management import call_command


def create_superuser():
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL')

    if username and password and email:
        print("!!!!!!!!!!!!!!!!!!!!!!!")
        call_command('createsuperuser', interactive=False, username=username, email=email)


if __name__ == '__main__':
    create_superuser()
