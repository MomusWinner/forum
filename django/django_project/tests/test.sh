#!/bin/bash
export POSTGRES_HOST=127.0.0.1
export POSTGRES_PORT=5432
export POSTGRES_USER=test
export POSTGRES_PASSWORD=test
export POSTGRES_DB=test
# export MINIO_ACCESS_KEY_ID=user
# export MINIO_SECRET_ACCESS_KEY=password
# export MINIO_STORAGE_BUCKET_NAME=static
# export MINIO_API=http://localhost:9000
# export MINIO_CONSISTENCY_CHECK_ON_START=False



python3 django/django_project/manage.py test $1