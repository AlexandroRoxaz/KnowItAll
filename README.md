# KnowItAll
Проект по предмету "Основы построения защищенных баз данных" за весенний семестр 5 курса в МФТИ в 2023 году. Выполнен Соклаковым А.Р. гр. С01-819.
## Общее описание:

KnowItAll - "база знаний" о проектах АСУ ТП, содержит информацию о используемых программно-технических средствах, программном обеспечении, составных ПТС (серверных стойках), а так же общей топологии систем (помещения, здания, блоки).

ПО предназначено для систематизации и накопления информации о реализуемых проектах с целью упрощения процесса разработки аналогичных проектов в будущем.

Функции безопасности:
* Парольная аутентификация (средствами фреймворка Джанго)
* Разграничение доступа (средствами фреймворка Джанго)
* Защита восстановления пароля (средствами фреймворка Джанго)

Доступ к ПО должен осуществляться из защищённой корпоративной сети. В Базе данных могут содержаться данные ДСП.

![Схема проекта](https://github.com/AlexandroRoxaz/KnowItAll/blob/main/Knowitall.png)

## Руководство по установке

* Шаг 0. Установить python3, если он не был предустановлен:
     - sudo apt-get install python3
* Шаг 1. Установить pip: 
     - sudo apt-get install python3-pip
* Шаг 2. Установить фреймворк джанго:
     - sudo apt install python3-django
* Шаг 3. Создать проект dbprotection:
     - django-admin startproject dbprotection
* Шаг 4. Создать приложение knowitall:
     - python3 manage.py startapp knowitall
* Шаг 5. Провести стартовую миграцию:
     - manage.py makemigrations 
     - manage.py migrate 
* Шаг 6. Сохранить файлы исходного кода и распаковать их с заменой в директорию с проектом и приложением

* Шаг 7. Применить изменения:
     - manage.py makemigrations 
     - manage.py migrate
* Шаг 8. Создать суперпользователя (исходного администратора):      
     - python3 manage.py createsuperuser 
* Шаг 9. Запустить сервер: 
     - manage.py runserver 0.0.0.0:8000
* Шаг 10. Открыть вкладку с адресом http://_host_ip_address:8000/admin/
* Шаг 11. Создать необходимые объекты
* Шаг 12. Открыть вкладку с адресом http://host_ip_address:8000 и убедиться в работоспособности сайта
