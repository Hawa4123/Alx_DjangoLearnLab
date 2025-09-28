#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

<<<<<<< HEAD

=======
>>>>>>> e2b71aa3a299cf5cc532066e2d6f76fbfac0e3e6
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advanced_api_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

<<<<<<< HEAD
=======
if __name__ == '__main__':
    main()

if __name__ == '__main__':
    main()
>>>>>>> e2b71aa3a299cf5cc532066e2d6f76fbfac0e3e6

if __name__ == '__main__':
    main()
