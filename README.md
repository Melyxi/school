# Запуск приложения 
```
1) docker-compose build
2) docker-compose up
3) http://127.0.0.1:8000/
```
## Аунтификация по JWT 

#### GET /api/districts/

Получение всего списка районов. Тело ответа:
```
{
    {
    "count": 26,
    "next": "http://127.0.0.1:8000/api/districts/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "district_name": "Stari Grad",
            "town": 1
        },
        ----
    ]
}
```

#### GET /api/districts/{id_district}/

Получение одного района. Тело ответа:
```
{
    "id": 1,
    "district_name": "Stari Grad",
    "town": 1
}
```

#### POST /api/districts/

Создание района. Тело запроса:
```
{
    "district_name": "",
    "town": null
}
```
#### PUT /api/districts/{id_district}/

Обновление района. Тело запроса:
```
{
    "district_name": "",
    "town": null
}
```
#### DELETE /api/districts/{id_district}/

удаление района

#### GET /api/education/

Получение все школ. Тело ответа:
```
{
    "count": 103,
    "next": "http://127.0.0.1:8000/api/education/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "district_id": {
                "id": 1,
                "district_name": "Stari Grad",
                "town": 1
            },
            "study_year": 2018,
            "school_type": "high",
            "school_name": "Stari Grad hight shool",
            "school_long": 20.27295,
            "school_lat": 44.821465,
            "students_num": 964,
            "graduates_num": 763
        },
        ----
    ]
}
```
#### GET /api/education/{id_education}/

Получение одной школы. Тело ответа:
```
{
    "count": 103,
    "next": "http://127.0.0.1:8000/api/education/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "district_id": {
                "id": 1,
                "district_name": "Stari Grad",
                "town": 1
            },
            "study_year": 2018,
            "school_type": "high",
            "school_name": "Stari Grad hight shool",
            "school_long": 20.27295,
            "school_lat": 44.821465,
            "students_num": 964,
            "graduates_num": 763
        },
        ----
    ]
}
```

#### POST /api/education/{id_education}/

Создание школы. Тело ответа:
```
{
    "study_year": null,
    "school_type": null,
    "school_name": "",
    "school_long": null,
    "school_lat": null,
    "students_num": null,
    "graduates_num": null
}
```
#### PUT /api/education/{id_education}/

Обновление школы. Тело ответа:
```
{
    "study_year": null,
    "school_type": null,
    "school_name": "",
    "school_long": null,
    "school_lat": null,
    "students_num": null,
    "graduates_num": null
}
```
#### GET /api/education/{id_education}/

Запрос только для администратора

Получение координат школы. Тело ответа:
```
{
    "id": 1,
    "school_long": 20.27295,
    "school_lat": 44.821465
}
```




