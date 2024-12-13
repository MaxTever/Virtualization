FROM jupyter/minimal-notebook:latest

RUN pip install --no-cache-dir jupyterlab jupyter_server


# Параметр корневой директории
ARG ROOT_DIR=/home/jovyan
ENV ROOT_DIR=${ROOT_DIR}

# Устанавливаем переменную окружения с именем администратора
ENV JUPYTERHUB_ADMIN_NAME=admin
ENV JUPYTERHUB_ADMIN_PASSWORD=admin

# Открываем порт для JupyterHub
EXPOSE 8000

# Копируем конфигурационный файл JupyterHub в контейнер
COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

# Запускаем JupyterHub
CMD ["jupyterhub", "--config", "/srv/jupyterhub/jupyterhub_config.py"]