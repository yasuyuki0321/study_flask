FROM python:3.10.0

WORKDIR /src

RUN apt update; \
    apt install -y \
        git \
        vim \
        locales

RUN sed -i -E 's/# (ja_JP.UTF-8)/\1/' /etc/locale.gen; \
    locale-gen
ENV LANG=ja_JP.UTF-8
ENV TZ=Asia/Tokyo

# 通常は不要 netskope環境で使用する場合のみ必要
COPY ./.devcontainer/netscope/nscacert.pem /tmp/
ENV NODE_EXTRA_CA_CERTS=/tmp/nscacert.pem

COPY requirements.txt .
RUN pip install -r ./requirements.txt
