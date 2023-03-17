# Создание образа Node.js приложения
---

## Создаем файл Dockerfile

```
#какой образ будем использовать
FROM node:alpine

#создаём каталог внутри контейнера
WORKDIR /app 

#копируем необходимые файлы из текщего каталога в WORKDIR внутри контейнера
COPY . .

#Вызываем команду и передаём ей параметр
CMD [ "node", "index.mjs" ]
```

Собираем наш образ:
-t тег для создаваемого образа
```
docker build . -t my-text-file-creator
```

Создаём контейнер из созданного образа:

--rm удаление контейнера после завершения выполнения или остановки

-it запуск в интерактивном режиме, т.е. в запускаемой консоли

-d запуск в фоновом режиме

```
docker run --rm -it my-text-file-creator
```

---

## Файловая структура контейнера

Для доступа к файловой системе контейнера, нужно у работающего контейнера вызвать любую доспную оболочку, например sh

``
docker exec -it {id или имя запущенного контейнера} sh (или /bin/bash)
``