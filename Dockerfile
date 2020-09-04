FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1
ENV DOCKER_CONTAINER 1
ENV C_FORCE_ROOT true

RUN sed -i "s/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g" /etc/apk/repositories &&\
 apk update && \
 apk add --no-cache git && \
 apk add --no-cache tzdata && \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache g++ freetype-dev jpeg-dev zlib-dev && \
 apk add --no-cache --virtual .build-deps gcc musl-dev linux-headers postgresql-dev libffi-dev libxml2-dev libxslt-dev python3-dev && \
 apk add --no-cache build-base binutils-doc autoconf flex bison freetype-dev libpng-dev libjpeg-turbo-dev && \
 apk add --no-cache zlib-dev gdbm-dev ncurses-dev && \
 apk add --no-cache automake libtool curl tmux gettext && \
 ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
 echo "Asia/Shanghai" > /etc/timezone && \
 cd /opt && \
 git clone https://github.com/taigaio/taiga-back.git taiga-back && \
 cd taiga-back && \
 git checkout stable && \
 pip install -r /opt/taiga-back/requirements.txt --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple && \
 pip install -U -i https://pypi.tuna.tsinghua.edu.cn/simple gunicorn
# apk del .build-deps

COPY local.py /opt/taiga-back/settings/
COPY celery.py /opt/taiga-back/settings/

EXPOSE 8001

WORKDIR /opt/taiga-back
