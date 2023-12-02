# Dockerfile
FROM jupyter/base-notebook

USER root

RUN apt-get update && \
    apt-get install -y \
    python3-pip

USER $NB_UID

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --requirement /tmp/requirements.txt

RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager

# Copia el contenido del directorio actual al directorio de trabajo del contenedor
COPY . /home/jovyan/

WORKDIR /home/jovyan/notebooks
