# Как запускать сервисы с помощью Docker Compose
---

## Установка Docker-compose

Скачиваем скрипт:
```
sudo curl -L https://github.com/docker/compose/releases/download/1.29.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
```
Задаём разрешение на выполнение:
```
sudo chmod +x /usr/local/bin/docker-compose
```

> Так же можно установить Docker-compose из репозитория ubuntu: sudo apt install docker-compose доступна стабильная версия, а так же snap пакет




## Создаём docker-compose.yml

```

version: '3'

services:
  app:
    build: ./app
  mongo:
    image: mongo

```

Запускаем:
```
docker-compose up
```