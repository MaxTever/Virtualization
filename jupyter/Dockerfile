FROM jupyter/minimal-notebook:latest


#Параметр корневой директории 
ARG ROOT_DIR=/home/jovyan
ENV ROOT_DIR=${ROOT_DIR}

# Устанавливаем переменную окружения
ENV JUPITERHUB_ADMIN_NAME=admin

# Устанавливаем jupyterhub
RUN pip install jupyterhub

# Запускаем jupyterhub
CMD ["jupyterhub"]