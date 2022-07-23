![Django](https://img.shields.io/badge/django%20-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?&style=for-the-badge&logo=postgresql&logoColor=white)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx%20-%23009639.svg?&style=for-the-badge&logo=nginx&logoColor=white)
![Docker](https://img.shields.io/badge/docker%20-%230db7ed.svg?&style=for-the-badge&logo=docker&logoColor=white)
![Github](https://img.shields.io/badge/github%20-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white)


![Workflow](https://github.com/kirsbrosnone/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# Проект YaMDb

Развернутый проект на сервере YandexCloud:
 `84.201.178.60/api/v1/` - api.
 `84.201.178.60/redoc/` - документация к api.
 `84.201.178.60/admin` - web-интерфейс проекта. 

### Описание проекта
Продолжение учебного проекта api_yamdb. В данном задании реализован GitHub Actions: тесты, автопуш в dockerhub, деплой на сервер и отправка сообщения в телеграм.
Проект YaMDb собирает отзывы пользователей на произведения.
API позволяет оставлять и просматривать отзывы и комментарии к произведениям, просматривать произведения по категориям и жанрам.
Пользователи с некоторыми пользовательскими ролями имеют расширенные права на управление контентом, включая создание произведений, жанров и категорий, удаление и правка отзывов и комментариев.

### Пользовательские роли
- Аноним — может просматривать описания произведений, читать отзывы и комментарии.
- Аутентифицированный пользователь `user` — может читать всё, как и Аноним, может публиковать отзывы и ставить оценки произведениям, может комментировать отзывы; может редактировать и удалять свои отзывы и комментарии, редактировать свои оценки произведений. Эта роль присваивается по умолчанию каждому новому пользователю.
- Модератор `moderator` — те же права, что и у Аутентифицированного пользователя, плюс право удалять и редактировать любые отзывы и комментарии.
- Администратор `admin` — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
- Суперюзер Django должен всегда обладать правами администратора, пользователя с правами `admin`. Даже если изменить пользовательскую роль суперюзера — это не лишит его прав администратора. Суперюзер — всегда администратор, но администратор — не обязательно суперюзер.

### Самостоятельная регистрация новых пользователей

1. Пользователь отправляет POST-запрос с параметрами email и username на эндпоинт `/api/v1/auth/signup/`.
2. Сервис YaMDB отправляет письмо с кодом подтверждения `(confirmation_code)` на указанный адрес `email`.
3. Пользователь отправляет POST-запрос с параметрами `username` и `confirmation_code` на эндпоинт `/api/v1/auth/token/`, в ответе на запрос ему приходит `token` (JWT-токен).

В результате пользователь получает токен и может работать с API проекта, отправляя этот токен с каждым запросом.
После регистрации и получения токена пользователь может отправить PATCH-запрос на эндпоинт `/api/v1/users/me/` и заполнить поля в своём профайле (описание полей — в документации).

### Создание пользователя администратором
Пользователя может создать администратор — через админ-зону сайта или через POST-запрос на специальный эндпоинт `api/v1/users/` (описание полей запроса для этого случая — в документации). В этот момент письмо с кодом подтверждения пользователю отправлять не нужно.
После этого пользователь должен самостоятельно отправить свой `email` и `username` на эндпоинт `/api/v1/auth/signup/`, в ответ ему должно прийти письмо с кодом подтверждения.
Далее пользователь отправляет POST-запрос с параметрами `username` и `confirmation_code` на эндпоинт `/api/v1/auth/token/`, в ответе на запрос ему приходит `token` (JWT-токен), как и при самостоятельной регистрации.

### Ресурсы API YaMDb
- Ресурс `auth`: аутентификация.
- Ресурс `users`: пользователи.
- Ресурс `titles`: произведения, к которым пишут отзывы (определённый фильм, книга или песенка).
- Ресурс `categories`: категории (типы) произведений («Фильмы», «Книги», «Музыка»).
- Ресурс `genres`: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
- Ресурс `reviews`: отзывы на произведения. Отзыв привязан к определённому произведению.
- Ресурс `comments`: комментарии к отзывам. Комментарий привязан к определённому отзыву.

### Запуск проекта на собственном сервере через Github Actions.

`Для корректной работы, отключите все работающие docker-контейнеры`

1. Делаете форк этого репозитория или копируете и заливаете в свой репозиторий на Github.
2. В форк (или свой репозиторий) на `Github - Settings - Secrets - Action secrets` необходимо добавить следующие значения: 
```sh
SECRET_KEY - секретный ключ приложения django (можно найти в settings проекта).
DB_NAME - имя базы данных (postgres, по умолчанию).
POSTGRES_USER - пользователь базы данных, (postgres, по умолчанию).
POSTGRES_PASSWORD - пароль пользователя, (postgres, по умолчанию).
DB_ENGINE - база данных (django.db.backends.postgresql, по умолчанию).
DB_HOST - хост (db, по умолчанию).
DB_PORT - порт (5432, по умолчанию).
DOCKER_USERNAME - имя пользователя в DockerHub.
DOCKER_PASSWORD - пароль пользователя в DockerHub.
HOST - ip-адрес сервера на который выполняется деплой.
USER - пользователь, который будет логиниться в сервер.
SSH_KEY - приватный ssh-ключ.
PASSPHRASE - кодовая фраза для ssh-ключа.
TELEGRAM_TO - id телеграм-аккаунта (пишем @userinfobot "/start").
TELEGRAM_TOKEN - токен бота (пишем@BotFather, "/token <имя бота>" для выдачи нового token, или "/mybots" для просмотра текущего токена).
```
3. Локально переходим в `yamdb_final/infra/nginx/default.conf` меняете значение Server name на свое.
4. Подключаемся на свой сервер. В директории `home/<username>/` создаем директорию `nginx`.
5. Копируем с локальной машины на свой сервер файлы: `yamdb_final/infra/docker-compose.yaml` и `yamdb_final/infra/nginx/default.conf`. Сделать это можно при помощи команды scp. Например находясь в директории `yamdb_final/infra/nginx/` выполнить команду: `scp default.conf <username>@<host>/home/<username>/nginx/default.conf`.
6. Если на сервере не установлен Docker и docker-compose, выполняем установку:
```sh
sudo apt install docker.io
```
```sh
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
```sh
sudo chmod +x /usr/local/bin/docker-compose
```
Проверяем, что установка прошла корректно:
```sh
sudo docker --version # появится сообщение вида Docker version 20.10.12, build 20.10.12-0ubuntu2~20.04.1
```
```sh
sudo docker-compose --version # появится сообзение вида docker-compose version 1.29.2, build 5becea4c
```
7. Пушите все изменения в свой репозиторий на Github. Автоматически запустится yamdb_workflow.

### После успешного деплоя на сервер.

1. Создаем суперпользователя (для логина в админ-зону api), на подключенном сервере:
```sh
sudo docker-compose exec web python manage.py createsuperuser
```
2. Чтобы наполнить базу данных используем команду:
```sh
sudo docker-compose exec web python manage.py create_dummy_data
```
3. Проверяем работу:
- `<ваш ip>/admin` - Админ зона API с графическим интерфейсом, проверьте создаются ли пользователи, ревью, жанры и т.д.
- `<ваш ip>/redoc` - Документация для API. Желательна к ознакомлению.
- `<ваш ip>/api/v1` - API. Проверить можно например через Postman или Thunder client, попробовать выполнить запросы (примеры запросов есть в документации для API) к БД, создать пользователя, оставить комментарий и т.д.

### Автор

Роман Кирсанов, Студент факультета Бэкенд Яндекс.Практикум. Когорта №9+
