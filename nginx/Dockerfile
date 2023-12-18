# -*- coding: utf-8 -*-
FROM nginx:alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY config/site.conf /etc/nginx/conf.d
#COPY proxy_params /etc/nginx