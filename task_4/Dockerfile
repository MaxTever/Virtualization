FROM jupyterhub/jupyterhub:latest


#Параметр корневой директории 
ARG ROOT_DIR=/home/jovyan
ENV ROOT_DIR=${ROOT_DIR}

# Устанавливаем переменную окружения
ENV JUPITERHUB_ADMIN_NAME=admin
ENV JUPITERHUB_ADMIN_PASSWORD=admin

EXPOSE 8000

# Запускаем jupyterhub
CMD ["jupyterhub"]