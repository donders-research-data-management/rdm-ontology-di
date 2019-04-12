FROM alpine:3.9 AS rdm-configurable-content-builder

RUN apk add --no-cache --update \
   make \
   python \
   py-pip

RUN pip install Sphinx --no-cache-dir && \
    mkdir -p /src/configurable-content

COPY build /src/configurable-content/build
COPY doc /src/configurable-content/doc
COPY external_urls.* /src/configurable-content/

RUN ls /src/configurable-content
RUN cd /src/configurable-content/build && make dist

FROM nginx:1.15-alpine

COPY build/docker/nginx.conf /etc/nginx/nginx.conf

COPY --from=rdm-configurable-content-builder /src/configurable-content/build/dist /usr/share/nginx/html/doc
