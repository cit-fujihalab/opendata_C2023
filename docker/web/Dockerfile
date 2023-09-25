FROM python:3.9

ARG USERNAME=app
ARG GROUPNAME=app
ARG UID=1000
ARG GID=1000
ARG WORKDIR=/opt/app

RUN groupadd -g $GID $GROUPNAME && \
    useradd -m -s /bin/bash -u $UID -g $GID $USERNAME
RUN mkdir -p $WORKDIR
RUN chown -R $UID:$GID $WORKDIR

ENV PATH /home/$USERNAME/.local/bin:$PATH

USER $USERNAME
WORKDIR $WORKDIR

COPY --chown=$UID:$GID  requirements.txt $WORKDIR
RUN pip install --user -r requirements.txt

COPY --chown=app:app ./apps /opt/app/apps

ENTRYPOINT [ "streamlit", "run", "apps/web/inference_demo.py" ]
