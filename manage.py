#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advanced_api_project.settings')
=======
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_project.settings')
>>>>>>> 8ca59bf (Add api_project directory)
>>>>>>> 33ddc232c39db4425cc559cd88841abc6f6fb91d
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()