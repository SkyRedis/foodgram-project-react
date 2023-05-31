# foodgram-project-react
# Дипломная работа
____
[![workflow status](https://github.com/SkyRedis/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg?branch=master)](https://github.com/SkyRedis/foodgram-project-react/actions/workflows/foodgram_workflow.yml)
____

## Инфраструктура
- Проект работает с СУБД PostgreSQL.
- Проект запущен на сервере в Яндекс.Облаке в трёх контейнерах: nginx, PostgreSQL и Django+Gunicorn. Заготовленный контейнер с фронтендом используется для сборки файлов.
- Контейнер с проектом обновляется на Docker Hub.
- В nginx настроена раздача статики, запросы с фронтенда переадресуются в контейнер с Gunicorn. Джанго-админка работает напрямую через Gunicorn.
- Данные сохраняются в volumes.


## Описание
 Произведена упаковка в докер контейнер проекта foodgram-project-react через workflow в yandex.cloud.
 Реализованы api запросы **GET, POST, PUT, PATCH, DELETE**
 Авторизация реализована через *djoser authToken*.
 **Обьекты:** Кастомный пользователь (UserFoodgram), подписки (Subscribe), рецепты (Recipe), ингредиенты (Ingredient), избранные (Favourite), теги (Tag), списки покупок (ShoppingCart).

____

## Как развернуть проект через GitHub Actions(workflow) и контеризацию Docker в облаке(yandex.cloud):
### 1. Скачать и установить Docker Desktop:
- **Установка Docker на Linux:**
> sudo apt install curl

> curl -fsSL https://get.docker.com -o get-docker.sh

> sh get-docker.sh

>sudo apt install docker.io

- На Windows 10:

Скачать установочный  файл с оф. сайта и установить - https://www.docker.com/products/docker-desktop/. 
### 2. Форкнуть(Fork) репозиторий https://github.com/SkyRedis/foodgram-project-react:
- Перейти в Settings-Secrets-Actions и добавить переменные окружения, которые используются в foodgram_workflow.yml:
TELEGRAM_TO - ID своего телеграм-аккаунта. Узнать свой ID можно у бота @userinfobot;
TELEGRAM_TOKEN - охраните токен вашего бота. Получить этот токен можно у бота @BotFather;
USER - имя пользователя для подключения к серверу(в данном случае yandex cloud);
HOST - IP-адрес вашего сервера;
PASSPHRASE - если при создании ssh-ключа вы использовали фразу-пароль;
SSH_KEY - *cat ~/.ssh/id_rsa* приватный ключ с компьютера, имеющего доступ к боевому серверу;
- Значения следующих переменных можно посмотреть в settings или .env.template:
*DB_ENGIN, DB_NAME, POSTGRES_USER, POSTGRES_PASSWORD, DB_HOST, DB_PORT, SECRET_KEY, ALLOWED_HOSTS*
### 3. Клонировать репозиторий и перейти в него в командной строке:
> git clone git@github.com:<Имя_пользователя_GitHub>/foodgram-project-react.git

> cd foodgram-project-react/
### 4. Создать копию файла и переименовать - ".env.template" в ".env":
> cp infra/.env.template infra/.env

**Наполнить файл по подсказкам в .env.template**
### 5. Скопировать foodgram_workflow.yml:
>cp foodgram_workflow.yml .github/workflows/foodgram_workflow.yml

### 6. В docker-compose.yml поменять image на свой.
### 7. Запушить изменения и проверить в GitHub Actions workflows:
> git add .

> git commit -m 'commit'

>git push
### 8. Войти в контейнер на сервере(yandex.cloud):
> ssh <Имя_пользователя>@<ip_адрес>
> docker exec -it <CONTAINER ID> bash - Войти в контейнер (вместо <CONTAINER ID> вписать id web-контейнера)

**Или выполнить следующие команды без входа в контейнер и используя имя сервиса(вместо id контейнера):**
Использовать вначале команды *docker compose exec web*, например *docker compose exec web python manage.py collectstatic --no-input*
### 9. Выполнить миграции:
> python manage.py migrate
### 10. Создаем суперпользователя и собираем статику:
> python manage.py createsuperuser
> python manage.py collectstatic --no-input
### 11. Применяем фикстуры:
> python manage.py dumpdata > fixtures.json - создать дамп (резервную копию) базы
> python manage.py loaddata fixtures.json -  импорт данных из только что созданного дампа
### 12. Загрузить в облако redoc.html и openapi-schema.yml:
> scp -r S:/Dev/foodgram-project-react/docs/ <Имя_пользователя>@<ip_адрес>:"/home/<Имя_пользователя>/"
> ssh <Имя_пользователя>@<ip_адрес>
> sudo docker cp docs/redoc.html 87c22879f6aa:/usr/share/nginx/html/api/docs/redoc.html
> sudo docker cp docs/openapi-schema.yml 87c22879f6aa:/usr/share/nginx/html/api/docs/openapi-schema.yml

____

## PostgreSQL и CSV
### Команда(для наполнения data base из CSV):
> python manage.py upload - запускаем код, который находится в директории reviews/management/commands/upload.py

____

## Некоторые примеры запросов к API:
Приложение доступно по адресу http://skyrediska.sytes.net/recipes/ или http://84.201.140.103/recipes/
### 1.1. Пользователь отправляет POST-запрос с параметрами email, username, first_name, last_name, password на эндпоинт /api/users/
### 1.2. Пользователь отправляет POST-запрос с параметрами email и password на эндпоинт hapi/auth/token/login/, в ответе на запрос ему приходит token.
### 1.3. Добавить токен в заголовок авторизации - TOKEN <токен>.
### 2. GET - список пользователей, профиль пользователя, текущий пользователь /api/users/, /api/users/{id}, /api/users/me/.
### 3. GET, POST, PATCH к рецептам /api/recipes/, /api/recipes/{id}/
### 4. Документация по api доступна по ссылке http://skyrediska.sytes.net/api/docs/

 ## Данные для входа в админку: 

- ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) `kirik.petrow@yandex.ru` 

- ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) `Alliance_75`

**Автор проекта:**
Петров Кирилл
