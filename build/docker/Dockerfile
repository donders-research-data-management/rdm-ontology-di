FROM alpine:3.9 AS rdm-configurable-content-builder

RUN apk add --no-cache --update \
   make \
   python \
   py-pip

RUN pip install Sphinx --no-cache-dir

COPY build/tools /tools

COPY build/scripts/Makefile /Makefile

COPY doc /doc

COPY *.md *.txt external_urls* /

RUN make dist

FROM nginx:1.15-alpine

COPY build/docker/nginx.conf /etc/nginx/nginx.conf

COPY --from=rdm-configurable-content-builder /dist /usr/share/nginx/html/doc
