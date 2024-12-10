# Задание 2 

- Выбрать один из микросервисов  https://github.com/GoogleCloudPlatform/microservices-demo  
- Развернуть через Docker  
- Сколькими способами можно посмотреть  содержимое конкретного файла в контейнере?

Я разворачивал `currencyservice`, для этого пришлось изменить в проекте переменные окружения и в `Dockerfile`.

### Сборка образа 

``` docker build -t currencyservice ```

### Запуск контейнера 

``` docker run -d --name currencyservice_container -e PORT=7000 -e DISABLE_PROFILER=true currencyservice ```

### Способы просмотра конкретного  файла в контейнере
- Использовать Docker Desktop
    - Нужно запустить контейнер и перейти во вкладку Files, где будет вся файловая система контейнера. Там же можно редактировать и удалять файлы.
- Консольные команды 
    - Просмотр файлов в контейнере: 
        - ```docker exec -i -t currencyservice_container ls /usr/src/app```
    - Просмотр содержимого файла: 
        - ```docker exec -it currencyservice_container cat /usr/src/app/server.js```
    - Копирование файла из контейнера на хост машину: 
        - ```docker cp currencyservice_container:/app/config.json ./config.json ```
        - После этого можно посмотреть файл: 
            - ```cat ./config.json ```
    