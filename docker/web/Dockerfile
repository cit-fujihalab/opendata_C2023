FROM python:3.9

WORKDIR /opt/app

COPY requirements.txt /opt/app
RUN pip install -r requirements.txt

COPY ./apps /opt/app/apps

ENTRYPOINT [ "streamlit", "run", "apps/web/server.py" ]
