FROM python:3.9


ARG WORKDIR=/opt/app

WORKDIR $WORKDIR

COPY requirements.txt $WORKDIR
RUN pip install -r requirements.txt

VOLUME [ "/opt/app/apps" ]

ENTRYPOINT [ "streamlit", "run", "apps/web/Demo.py" ]
