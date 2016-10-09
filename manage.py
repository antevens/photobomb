#!/usr/bin/env python
import os
import sys

# Make sure current path is included in sys.path for relative paths to work
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

for p in sys.path:
    print(p)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "photobomb.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
