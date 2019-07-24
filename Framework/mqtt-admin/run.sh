#!/bin/bash
docker kill some-nginx || true
docker run --rm --name some-nginx -v `pwd`:/usr/share/nginx/html:ro -p 8080:80 -d nginx 

