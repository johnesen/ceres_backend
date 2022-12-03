FROM python:3.8

RUN mkdir -p /opt/services/ceres
WORKDIR /opt/services/ceres

RUN mkdir -p /opt/services/ceres/requirements

ADD requirements.txt /opt/services/ceres/

COPY . /opt/services/ceres/

RUN pip install -r requirements.txt
