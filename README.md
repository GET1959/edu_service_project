# edu_service_project
Дипломный проект курса Python-разработчик.

## О проекте edu_service_project
Проект представляет собой пример платформы для удаленного обучения.

Для запуска проекта на локальной машине необходимо

клонировать его из репозитория,

создать файл .env по образцу .env.sample,

командой "python manage.py csu" создать администратора,

командой "python manage.py runserver" запустить сервер.

Тестовые данные можно создать в панели администратора или загрузить из фикстур (папка fixtures).

Приложение доступно только авторизованным пользователям, ограничение установлено в файле settings.py в переменной REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'].

Для публичного просмотра доступны только страницы входа и регистрации.

Приложение можно протестировать в сервисах postman, swagger или redoc.