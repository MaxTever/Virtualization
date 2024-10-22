# Дз 2

### Запуск JupyterHub

- Создаем Dockerfile

    Чтобы докерфайл принимал пармаетр корневой директории нужно указать:

    ```ARG ROOT_DIR=/home/jovyan ``` 
    ```ENV ROOT_DIR=${ROOT_DIR}```

    Далее нужно установить переменную окружения: 

    ```ENV JUPYTERHUB_ADMIN_NAME=admin```

- Далее собираем образ 
    ```docker build -t your_dockerhub_username/jupyterhub:latest --build-arg ROOT_DIR=/home/jovyan .```

### Пуш образа в Docker Hub

```docker login ``` 
```docker tag dockerhub_image/jupyterhub:latest maxtever/jupyterhub:latest``` ```docker push maxtever/jupyterhub:latest```

### Создаем Docker-compose файл 

Запускаем для проверки 
```docker-compose up -d```

### Делаем CI Pipeline

Создаем yml файл в котором описываем jobs. 