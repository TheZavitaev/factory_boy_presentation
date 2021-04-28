# Проект для иллюстрации генерации тестовых данных в Django

## Инсталляция
```
virtualenv env
source env/bin/activate
pip install -r requirements/dev.txt
```

## Делаем первую миграцию
```
./manage.py migrate
```

## Создание суперпользователя
```
./manage.py createsuperuser
```

## Запуск приложения
```
./manage.py runserver
```
## Откройте с браузере 
```
http://127.0.0.1:8000/admin
```

## Генерация тестовых данных
```
./manage.py generate_test_data
```

## Делаем дамп БД
```
./manage.py dumpdata > data.json
```
## Загружаем дамп в БД
```
./manage.py loaddata data.json
```
