FROM python:3.8-alpine


RUN pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install --upgrade wheel

RUN apk update && \
    apk add --no-cache python3-dev py3-pip py3-numpy py3-scipy && \
    rm -rf /var/cache/apk/*

RUN apk add --no-cache \
        gcc \
        musl-dev \
        gfortran \
        libstdc++ \
        lapack-dev \
        openblas-dev \
        python3-dev && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h && \
    apk add --no-cache libpng-dev freetype-dev && \
    rm -rf /var/cache/apk/*

RUN pip install --no-cache-dir numpy==1.20.3

RUN mkdir -p /usr/src/cw_model
WORKDIR /usr/src/cw_model

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/cw_model

ENV FLASK_APP=main.py

EXPOSE 7777

CMD ["flask", "run", "--host", "0.0.0.0"]