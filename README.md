# KnowItAll
Project for 2023 spring term course on Database protection in MIPT

![Схема проекта](https://github.com/AlexandroRoxaz/KnowItAll/blob/main/Knowitall.png)

## Руководство по установке

Шаг 0. Установить python3, если он не был предустановлен:
             sudo apt-get install python3
Шаг 1. Установить pip: 
             sudo apt-get install python3-pip
Шаг 2. Установить фреймворк джанго:
             sudo apt install python3-django
Шаг 3. Создать проект dbprotection:
              django-admin startproject dbprotection
Шаг 4. Создать приложение knowitall:
             python3 manage.py startapp knowitall
Шаг 5. Провести стартовую миграцию:
             manage.py makemigrations 
             manage.py migrate 
Шаг 6. Сохранить файлы исходного кода и распаковать их с заменой в директорию с проектом и приложением.
Шаг 7. Применить изменения:
             manage.py makemigrations 
             manage.py migrate
Шаг 8. Создать суперпользователя (исходного администратора):      
             python3 manage.py createsuperuser 
Шаг 9. Запустить сервер: manage.py runserver
Шаг 10. Открыть вкладку с адресом http://127.0.0.1:8000/admin/
Шаг 11. Создать необходимые объекты
Шаг 12. Открыть вкладку с адресом http://127.0.0.1:8000 и убедиться в работоспособности сайта
