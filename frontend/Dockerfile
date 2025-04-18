FROM nginx:alpine

# Копируем статические файлы фронтенда
COPY frontend/ /usr/share/nginx/html/

# Копируем конфигурацию Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Удаляем дефолтный конфиг (если нужно)
RUN rm -f /etc/nginx/conf.d/default.conf

EXPOSE 80