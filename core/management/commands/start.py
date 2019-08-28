#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from django.core.management.base import BaseCommand

def _sync_app():
    import django
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mozioChallenge.settings")
    django.setup()


def _reset_migrations():
    from unipath import Path

    this_file = Path(__file__).absolute().ancestor(3)
    current_dir = this_file.parent
    dir_list = current_dir.listdir()

    for paths in dir_list:
        migration_folder = paths.child('migrations')
        if migration_folder.exists():
            list_files = migration_folder.listdir()
            for files in list_files:
                split = files.components()
                if split[-1] != Path('__init__.py'):
                    try:
                        files.remove()
                    except IsADirectoryError:
                        # ignore __pycache__ dir
                        pass

def _rebuild_db(debug=True):
    import MySQLdb as db
    from mozioChallenge import settings
    import manage
    import sys
    import os

    sys.path.append('..\\')

    config = settings.DATABASES["default"]
    hostname = config["HOST"]
    username = config["USER"]
    password = config["PASSWORD"]
    schema = config["NAME"]

    try:
        con = db.connect(hostname, username, password)
        print("[ DELETING ] Database {}".format(schema))
        con.cursor().execute("DROP DATABASE {}".format(schema))
    except db.Error as e:
        pass

    try:
        t0 = time.clock()
        print("[ STARTING ] Creating Database {}".format(schema))
        con.cursor().execute("CREATE DATABASE {} CHARACTER SET utf8 COLLATE utf8_general_ci".format(schema))

        _sync_app()
        from django.core.management import execute_from_command_line

        try:
            print("[ STARTING ] Running Initial migrate.")
            args = [os.path.dirname(manage.__file__), "migrate", "--fake-initial"]
            execute_from_command_line(tuple(args))
        except:
            pass

        from mozioChallenge.settings import INSTALLED_APPS

        print("[ STARTING ] Running Initial migrate {}".format(schema))
        args = [os.path.dirname(manage.__file__), "makemigrations"]
        for each_app in INSTALLED_APPS:
            if not each_app.startswith('django.'):
                args.append(each_app)
        execute_from_command_line(tuple(args))

        print("[ STARTING ] Running migrate.")
        args = [os.path.dirname(manage.__file__), "migrate", "--run-syncdb"]
        if not debug:
            args.append("-v 0")
        execute_from_command_line(tuple(args))
        print("[ {0:7.3f}s ] Database {1}".format(time.clock()-t0, schema))
    except db.Error as e:
        print("Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
    finally:
        if con:
            con.close()



def _clear_db():
    from django.core.management import execute_from_command_line
    execute_from_command_line(("flush",))



class Command(BaseCommand):
    def handle(self, *args, **options):
        from mozioChallenge.config import DBAPPWEB_IP
        print("Installing on databases: {} (APP) ".format(DBAPPWEB_IP))
        _reset_migrations()
        _rebuild_db()
