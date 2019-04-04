FROM nginx:1.15-alpine

VOLUME ["tools/docker/nginx.conf", "dist"]

COPY tools/docker/nginx.conf /etc/nginx/nginx.conf

COPY dist /usr/share/nginx/html