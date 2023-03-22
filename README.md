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




## Файловая структура контейнера

Для доступа к файловой системе контейнера, нужно у работающего контейнера вызвать любую доспную оболочку, например sh

``
docker exec -it {id или имя запущенного контейнера} sh (или /bin/bash)
``