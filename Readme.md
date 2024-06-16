Создайте `.env` файл по примуру `.env.example`.  
Далее запуститу проект командой `docker compose up`. 

### Создание суперюзера
```
docker exec -it container_id python manage.py createsuperuser
```

### Запуст тестов
`/reactapp`
```
npm start
```
`/django/django-project`
```
python3 manage.py test tests
```