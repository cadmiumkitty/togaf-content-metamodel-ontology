FROM continuumio/miniconda3:latest
LABEL maintainer="Eugene Morozov <emorozov@gmail.com>"

RUN conda update -n base -c defaults conda
RUN conda install anaconda-project

RUN mkdir /notebook
RUN mkdir /metamodel

WORKDIR /notebook

COPY anaconda-project.yml /notebook/anaconda-project.yml
COPY .projectignore /notebook/.projectignore

RUN anaconda-project prepare --env-spec notebook
RUN anaconda-project run register-kernel
RUN anaconda-project run generate-config

COPY *.ipynb /notebook/
COPY *.csv /notebook/

ENTRYPOINT ["anaconda-project", "run", "taxonomy", "--anaconda-project-address", "0.0.0.0", "--no-browser", "--allow-root"]