## Виртуальная стажировка
Общая задача: Разработать мобильное приложение для Android и IOS, которое упростило бы туристам задачу по отправке данных о перевале и сократило время обработки запроса до трёх дней.

Задача: В соответствии с заданием разработать REST API, которое будет обслуживать мобильное приложение.

---

- Python 3.10
- Django 3.2.25
- Django REST framework 3.1

---

Документация: http://127.0.0.1:8000/swagger/


### API endpoint-s:

POST, добавление записи о перевале в БД

    127.0.0.1:8000/perevals/

GET, просмотр информации о перевале

    127.0.0.1:8000/perevals/{id}


PATCH, изменение записи пользователем

    127.0.0.1:8000/perevals/{id}

GET, просмотр всех записей пользователя

    127.0.0.1:8000/api/v1/submitData/{email}/

GET, просмотр всех id записей

    127.0.0.1:8000/api/v1/perevals/

Также доступны все другие эндпоинты: levels, coord, images

## Примеры:

Создание записи

    POST: 127.0.0.1:8000/perevals/
    {
        "beauty_title": "Перевал Дятлова ИЗменили!!!!",
        "title": "Перевал Дятлова",
        "other_titles": "Перевал Дятлова",
        "connect": "что-то",
        "tourist_id": {
        "fam": "Иванов",
        "name": "Иван",
        "otc": "Иванович",
        "email": "user@example.com",
        "phone": "02"
        },
        "coord_id": {
        "latitude": 1,
        "longitude": 2,
        "height": 111
        },
        "level_id": {
        "winter": "1А",
        "spring": "1А",
        "summer": "1А",
        "autumn": "1А"
        },
        "images": [],
        "status": "Новый"
        }


Изменение записи
    
    PATCH: 127.0.0.1:8000/perevals/1
    {
        "beauty_title": "Перевал Дятлова ИЗменили!!!!222",
        "title": "Перевал Дятлова",
        "other_titles": "Перевал Дятлова",
        "connect": "что-то",
        "tourist_id": {
        "fam": "Иванов",
        "name": "Иван",
        "otc": "Иванович",
        "email": "user@example.com",
        "phone": "02"
        },
        "coord_id": {
        "latitude": 1,
        "longitude": 2,
        "height": 111
        },
        "level_id": {
        "winter": "1А",
        "spring": "1А",
        "summer": "1А",
        "autumn": "1А"
        },
        "images": [],
        "status": "Новый"
        }

    Response: Status 200 OK
    {
        "state": 1,
        "message": "Запись изменена"
    }

Просмотр

    GET: 127.0.0.1:8000/perevals/1
    Response: Status 200 OK
    {
        "beauty_title": "Перевал Дятлова ИЗменили!!!!222",
        "title": "Перевал Дятлова",
        "other_titles": "Перевал Дятлова",
        "connect": "что-то",
        "tourist_id": {
        "fam": "Иванов",
        "name": "Иван",
        "otc": "Иванович",
        "email": "user@example.com",
        "phone": "02"
        },
        "coord_id": {
        "latitude": 1,
        "longitude": 2,
        "height": 111
        },
        "level_id": {
        "winter": "1А",
        "spring": "1А",
        "summer": "1А",
        "autumn": "1А"
        },
        "images": [],
        "status": "Новый"
        }
