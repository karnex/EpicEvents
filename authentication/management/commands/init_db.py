import fileinput
import re
import subprocess
import sys

from django.core.management.base import BaseCommand
from pathlib import Path


class Command(BaseCommand):
    help = 'Configure easily the database of project'

    def handle(self, *args, **kwargs):
        root_dir: Path = Path(__file__).parent.parent.parent.parent
        settings_dir: Path = root_dir / 'P12_EpicEvents'
        settings_f: str = str(settings_dir / 'db_local_settings.py')

        hostname = input('Please fill in the host name of your PostgreSQL DB:')
        name = input('Please fill in the name of your PostgreSQL DB:')
        user = input('Please insert the username of this DB:')
        pwd = input('Please insert the password of this DB:')

        db = {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': str(name),
            'USER': str(user),
            'PASSWORD': str(pwd),
            'HOST': str(hostname),
            'PORT': '5432',
        }

        if hostname and name and user and pwd:
            with fileinput.FileInput(settings_f, inplace=True) as file:
                for line in file:
                    if "db = {}" in line:
                        line = re.sub('{}', str(db), line)
                    sys.stdout.write(line)

        print('DB settings have been updated !')
        print('makemigrations...')
        subprocess.call('python3 manage.py makemigrations', shell=True)
        print('migrate...')
        subprocess.call('python3 manage.py migrate', shell=True)
        print('DB is noa ready to use ! :)')
