# module_18

**_Установка_**
`pip install django`\
**_Создание проекта Джанго_**\
`django-admin startproject UrbanDjango`\
**_Запуск локального сервера_**\
`python manage.py runserver`\
**_Создание приложения_**\
`python manage.py startapp <имя приложения>`\
**_Создание таблиц в базе данных_**\
`python manage.py migrate`

**_Проверка проекта на ошибки_**\
`python manage.py check`
**_Список доступных команд_**\
`python manage.py help`
`pip freeze >> requirements.txt`

`django-admin --version`

● Model (Модель): хранит данные.
● View (Представление): логика обработки запроса.
● Template (Шаблон): отвечает за отображение данных в удобном формате.

**_Создание админа_**\
`python manage.py createsuperuser`

Миграции синхронизируют изменения в моделях с базой данных.
Создание миграций

`python manage.py makemigrations`

**_Создание таблиц в базе данных_**\
`python manage.py migrate`

Операции с Django ORM выполняются в:

1. Django Shell (интерактивный интерфейс).
2. Представлениях (views) — если операции связаны с пользовательскими запросами.
3. Скриптах миграций или тестах — для автоматизации задач или тестирования.

`python manage.py shell`