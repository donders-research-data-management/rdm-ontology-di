FROM alpine:3.9 AS rdm-configurable-content-builder

RUN apk add --update \
   make \
   python \
   py-pip && \
   rm -rf /var/cache/apk

RUN pip install Sphinx --no-cache-dir

COPY build/tools /tools

COPY build/scripts/Makefile /Makefile

COPY doc /doc

COPY *.md external_urls* /

RUN make dist

FROM nginx:1.15-alpine

COPY build/docker/nginx.conf /etc/nginx/nginx.conf

COPY --from=rdm-configurable-content-builder /dist /usr/share/nginx/html
