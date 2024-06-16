#!/bin/bash
export POSTGRES_HOST=127.0.0.1
export POSTGRES_PORT=5432
export POSTGRES_USER=test
export POSTGRES_PASSWORD=test
export POSTGRES_DB=test

export DJAGNO_SECRET_KEY="django-insecure-ya^!_^+ye1&cw)rh)f)r\$yn%v58wnefcv!+4\$6-5%\$y7$@nubj"
export MARTOR_IMGUR_CLIENT_ID=0f726225d266549
export MARTOR_IMGUR_API_KEY=00c07c0b4efc1728e453fc582c64daf4a0462a82
export PYTHONDONTWRITEBYTECODE=1
export PYTHONUNBUFFERED=1
python3 django/django_project/manage.py test $1