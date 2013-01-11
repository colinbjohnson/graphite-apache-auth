import os, sys

sys.path.append('/opt/graphite/webapp')
os.environ['DJANGO_SETTINGS_MODULE'] = 'graphite.settings'

from django.contrib.auth.models import User
from django import db

def check_password(environ, user, password):
    db.reset_queries()

    kwargs = {'username': user, 'is_active': True}

    try:
        try:
            user = User.objects.get(**kwargs)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return True
        else:
            return False
    finally:
        db.connection.close()