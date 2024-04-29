
## Postgres
```
docker run -d --name forum -p 5430:5432 -e POSTGRES_USER=app -e POSTGRES_PASSWORD=123 -e POSTGRES_DB=forum_db postgres
```

## env
```
PG_HOST=127.0.0.1
PG_PORT=5430
PG_USER=app
PG_PASSWORD=123
PG_DBNAME=forum_db
```

```
python manage.py migrate

python.exe .\manage.py createsuperuser
```
