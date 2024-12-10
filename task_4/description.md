# Задание 4

### Dockerfile
На первом шаге я создавал Dockerfile для создания базового образа. Сначала я пытался использовать базовый образ Python, но столкнулся с проблемами при установке зависимостей. В результате, я решил использовать базовый образ `jupyter/minimal-notebook:latest`, который предоставляет готовую среду для запуска Jupyter Notebook. Это решение привело к увеличению размера образа, но упростило установку зависимостей.

По заданию, чтобы Dockerfile принимал параметр корневой директории, нужно указать:

```
ARG ROOT_DIR=/home/jovyan
ENV ROOT_DIR=${ROOT_DIR}
```

Далее нужно установить переменную окружения:

`ENV JUPYTERHUB_ADMIN_NAME=admin`

Для сборки образа используется команда:

```
docker build -t your_dockerhub_username/jupyterhub:latest --build-arg ROOT_DIR=/home/jovyan .
```

После успешной сборки образа, по заданию нужно запушить образ в DockerHub. Для этого нужно выполнить следующие команды:

```
docker login
docker tag maxtever/jupyterhub:latest maxtever/jupyterhub:latest
docker push maxtever/jupyterhub:latest
```

### docker-compose

Создаем сервис `jupiterhub`, в котором будет использоваться образ, созданный с помощью Dockerfile. Далее указываем порты, окружение и задаем volume. Также для проверки используется healthcheck со следующими параметрами. Это будет использоваться в CI pipeline:

```
healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/hub/health"]
      interval: 1m30s
      timeout: 30s
      retries: 5
      start_period: 30s
```

### CI Pipeline 

При создании пайплайна я указал, что он должен запускаться при push в ветку `main` и при изменениях в файлах `.github/workflows/**`, `jupyter`, `Dockerfile`, `docker-compose.yml`.

Далее я описал Jobs. Основное, что следует указать: изначально я не использовал healthcheck и описал проверку на запуск контейнера следующим образом:

```
- name: Test container
      run: |
        if docker ps --filter "name=jupyter_jupiterhub_1" --format "{{.Names}}" | grep -q "jupyter_jupiterhub_1"; then
          echo "Container is running"
        else
          echo "Container is not running"
          exit 1
        fi
```
После добавления healthcheck в docker-compose манифест, я изменил проверку (старую проверку оставил как дополнительную):
```
- name: healthCheck
      run: |
        HEALTH_STATUS=$(docker inspect --format='{{json .State.Health.Status}}' jupyter_jupiterhub_1)
          if ["$HEALTH_STATUS" != "\"healthy\""]; then
            echo "Container is not healthy"
            exit 1
          else
            echo ""Container is healthy""
          fi
```