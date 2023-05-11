![workflow](https://github.com/KlepalovS/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
# YaMDb (api v1).
## _Приложение собирает и хранит отзывы пользователей на произведения разных категорий, будь то книги или музыка,_ _фильмы или картины художников._

![alt text](https://sun1-85.userapi.com/CP3yKltGc5S20BLv2tOIcUr_2TRmwEMGo_bVKA/6DWs-SsdSmo.jpg)

Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»). 
Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). 
Добавлять произведения, категории и жанры может только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.
Пользователи могут оставлять комментарии к отзывам.
Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.

## Особенности

- Самостоятельная регистрация новых пользователей через POST запрос, после чего сервис YaMDB отправляет письмо с кодом подтверждения на указанный адрес e-mail.
- Для обновления access-токена не нужно применять refresh-токен и дополнительный эндпоинт. Токен обновляется через повторную передачу username и кода подтверждения.
- Упакован в Docker контейнеры.
- Настроены CI/CD с применением GitHub Actions и автоматическим развертыванием на боевом сервере Яндекс.Облака.

## Технологии

- [Python 3.7](https://www.python.org/) - язык программирования, который позволяют быстро работать и более эффективно внедрять системы!
- [Django 3.2](https://www.djangoproject.com/) - упрощает создание лучших веб-приложений быстрее и с меньшим количеством кода.
- [Django Rest Framework 3.12.4](https://www.django-rest-framework.org/) - мощный и гибкий инструментарий для создания веб-API.
- [PyJWT 2.1.0](https://pyjwt.readthedocs.io/en/stable/) - библиотека Python, которая позволяет вам кодировать и декодировать веб-токены JSON (JWT).
- [Docker](https://www.docker.com) - программная платформа для быстрой разработки, тестирования и развертывания приложений.
- [Nginx](https://nginx.org/ru/) - HTTP-сервер и обратный прокси-сервер, почтовый прокси-сервер, а также TCP/UDP прокси-сервер общего назначения.
- [PostgreSQL](https://www.postgresql.org) - свободная объектно-реляционная система управления базами данных.
- [Gunicorn](https://gunicorn.org) - HTTP-сервер с интерфейсом шлюза веб-сервера Python.
- [Яндекс.Облако](https://cloud.yandex.ru/) - публичная облачная платформа от российской интернет-компании «Яндекс». Yandex.Cloud предоставляет частным и корпоративным пользователям инфраструктуру и вычислительные ресурсы в формате as a service.
- [GitHub Actions](https://docs.github.com/ru/actions) - это облачный сервис, инструмент для автоматизации процессов тестирования и деплоя ваших проектов. Он служит тестовой площадкой, на которой можно запускать и тестировать проекты в изолированном окружении. 

##### Команда разработки:

- [Роберт (в роли Python-разработчика - разработчик 1)](https://github.com/Hoppy-Bobby)
- [Слава (в роли Python-разработчика - разработчик 2)](https://github.com/KlepalovS)
- [Дмитрий (в роли Python-разработчика - разработчик 3)](https://github.com/DNKer)

## Инструкция по развертыванию проекта.

Проект упакован в три контейнера: nginx, PostgreSQL, gunicorn + Django.
Фикстуры тестовой базы данных представлена в файле test_db.json.

Клонировать репозиторий и перейти в него в командной строке.

```
git clone git@github.com:KlepalovS/infra_sp2.git

cd infra_sp2/
```

Переходим в директорию с файлами для развертывания инфраструктуры. 

```
cd infra/
```

Cоздаем .env файл.

```
sudo nano .env
```

Заполняем файл по образцу ниже.

Секретный ключ Джанги.
```
SECRET_KEY='defaul_secret_key'
```
Получение/изменение SECRET_KEY (контейнер запущен).
Далее меняем в .env файле.
```
docker-compose exec web python manage.py shell
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```
Переменные режима работы сервера.
```
DEBAG='False'
```
Разрешенные хосты для подключения.
```
ALLOWED_HOSTS='*'
```
Переменные для настройки БД PostgreSQL в Джанго.
Движок БД. ENGINE в settings.py DATABASES.
```
DB_ENGINE='django.db.backends.postgresql'
```
Задаем имя БД.
NAME в settings.py DATABASES.
```
DB_NAME='postgres'
```
Можно сменить БД на новую, прежде создав ее (контейнер запущен).
Далее меняем в .env файле.
```
docker-compose exec db psql -U postgres
CREATE DATABASE <db_name>
```
Задаем имя пользователя БД и пароль для этого юзера.
USER и PASSWORD в settings.py DATABASES (Не используется с SQLite).
```
POSTGRES_USER='postgres'
POSTGRES_PASSWORD='postgres1'
```
Можно сменить на нового, прежде создав его и дав все разрешения
для работы с БД (контейнер запущен).
Далее меняем в .env файле.
```
docker-compose exec db psql -U postgres
CREATE USER <username> WITH ENCRYPTED PASSWORD '<password>';
GRANT ALL PRIVILEGES ON DATABASE <db_name> TO <username>; 
```
Указываем какой хост и порт будут использоваться для связи с БД.
HOST и PORTв settings.py DATABASES(Не используется с SQLite).
Имя хоста в нашем случае совпадает с названием контейнера с БД.
```
DB_HOST='db'
DB_PORT='5432'
```

Запускаем производим развертывание инфраструктуры.

```
docker-compose up -d
```

Применяем миграции, создаем суперюзера и собираем статику в контейнере web.

```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input 
```

Наполняем БД из фикстур. 
Для этого копируем фикстуры на сервер и выполняем загрузку в БД.

```
docker-compose cp ./test_db.json web:app/
docker-compose exec web python manage.py loaddata test_db.json
```

После тестирования останавливаем контейнеры.

```
docker-compose down -v
```

## Инструкция для CI/CD находится в файле yamdb_workflow.

При пуше в ветку master последовательно запускаются четыре задачи (jobs):

- Tests - тестирование проекта на соответствие PEP8 и локальным тестам. Задействуем модуль actions/setup-python@v2 для запуска пакетов python. 
- Build_and_push_to_docker_hub - создается образ докер контейнера и отправляется в репозиторий докерхаба. Задействуем модуль docker/setup-buildx-action@v1 для сборки Docker образов, docker/login-action@v1 для установки соединения с DockerHub, docker/build-push-action@v2 для отправки собранного образа в репозиторий DockerHub.
- Deploy - развертывание проекта на боевом сервере Яндекс.Облака. Задействуем модуль appleboy/ssh-action@master для инициализации подключения по SSH и выполнения скрипта.
- Send_message - отправка сообщения в тг об успешном выполнении workflow. Задействуем модуль appleboy/telegram-action@master.

## Примеры работы

Подробная документация доступна по эндпоинту /redoc/
Для неавторизованных пользователей работа с API доступна в режиме чтения.

## Пользовательские роли

Аноним — может просматривать описания произведений, читать отзывы и комментарии.
Аутентифицированный пользователь (user) — может, как и Аноним, читать всё, дополнительно он может публиковать отзывы и ставить оценку произведениям (фильмам/книгам/песенкам), может комментировать чужие отзывы; может редактировать и удалять свои отзывы и комментарии. Эта роль присваивается по умолчанию каждому новому пользователю.
Модератор (moderator) — те же права, что и у Аутентифицированного пользователя плюс право удалять любые отзывы и комментарии.
Администратор (admin) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
Суперюзер Django — обладает правами администратора (admin)

###### Права доступа: Доступно без токена.

- GET /api/v1/categories/ - получение списка всех категорий
- GET /api/v1/genres/ - получение списка всех жанров
- GET /api/v1/titles/ - получение списка всех произведений
- GET /api/v1/titles/{title_id}/reviews/ - получение списка всех отзывов
- GET /api/v1/titles/{title_id}/reviews/{review_id}/comments/ - получение списка всех комментариев к отзыву

###### Права доступа: Администратор

- GET /api/v1/users/ - получение списка всех пользователей

#### Регистрация нового пользователя

```
POST /api/v1/auth/signup/
```

Получение JWT-токена:

```
POST /api/v1/auth/token/
```

### Примеры работы с API для авторизованных пользователей

Добавление категории:

```
Права доступа: администратор.
POST /api/v1/categories/
```

Удаление категории:

```
Права доступа: администратор.
DELETE /api/v1/categories/{slug}/
```

Добавление жанра:

```
Права доступа: администратор.
POST /api/v1/genres/
```

Удаление жанра:

```
Права доступа: администратор.
DELETE /api/v1/genres/{slug}/
```

Обновление публикации:

```
PUT /api/v1/posts/{id}/
```

Добавление произведения:

```
Права доступа: Администратор. 
POST /api/v1/titles/
```
Добавление произведения:

```
Права доступа: Доступно без токена
GET /api/v1/titles/{titles_id}/
```

Частичное обновление информации о произведении:

```
PATCH /api/v1/titles/{titles_id}/
```

Удаление информации о произведении:
```
Права доступа: Администратор
DEL /api/v1/titles/{titles_id}/
```

### Работа с пользователями:

Получение списка всех пользователей.

```
Права доступа: Администратор
GET /api/v1/users/ - Получение списка всех пользователей
```

Добавление пользователя:

```
Права доступа: Администратор
Поля email и username должны быть уникальными.
POST /api/v1/users/ - Добавление пользователя
```

Получение пользователя по username:

```
Права доступа: Администратор
GET /api/v1/users/{username}/ - Получение пользователя по username
```

Изменение данных пользователя по username:

```
Права доступа: Администратор
PATCH /api/v1/users/{username}/ - Изменение данных пользователя по username
```

Удаление пользователя по username:

```
Права доступа: Администратор
DELETE /api/v1/users/{username}/ - Удаление пользователя по username
```

Получение данных своей учетной записи:

```
Права доступа: Любой авторизованный пользователь
GET /api/v1/users/me/ - Получение данных своей учетной записи
```

Изменение данных своей учетной записи:

```
Права доступа: Любой авторизованный пользователь
PATCH /api/v1/users/me/ # Изменение данных своей учетной записи
```

#### Лицензия
###### Free Software, as Is 
###### _License Free_
###### Authors: [Robert](https://github.com/Hoppy-Bobby), [Slava](https://github.com/KlepalovS), [Dmitry](https://github.com/DNKer), [Yandex practikum](https://practicum.yandex.ru)
###### 2023
