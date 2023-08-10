FROM python:3

RUN apt-get update
RUN pip install --upgrade pip
RUN python -m pip install jupyterlab
RUN pip3 install openpyxl

