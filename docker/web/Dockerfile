FROM python:3.9

WORKDIR /opt/app

# poetryのインストール先の指定
# ENV POETRY_HOME=/opt/poetry
# poetryインストール
# RUN curl -sSL https://install.python-poetry.org | python3 -
# RUN cd /usr/local/bin && ln -s /opt/poetry/bin/poetry
# RUN poetry config virtualenvs.in-project true 
# RUN apt update -y

COPY requirements.txt /opt/app
RUN pip install -r requirements.txt

COPY apps /opt/app
