# Используем базовый образ Ubuntu
FROM ubuntu:latest

# Обновляем пакеты внутри контейнера
RUN apt-get update

# Устанавливаем веб-сервер Nginx
RUN apt-get install -y nginx

# Копируем HTML файл в папку /var/www/html/ внутри контейнера
COPY index.html /var/www/html/

# Открываем порт 80, чтобы веб-сервер мог слушать входящие запросы
EXPOSE 80

# Запускаем веб-сервер Nginx в фоновом режиме
CMD ["nginx", "-g", "daemon off;"]