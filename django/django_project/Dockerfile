# Стартовый образ, возмем 3.11 python на базе alpine, он поменше.
FROM python:3.11-alpine

# рабочая директория
WORKDIR /usr/src/app
# Каталоги для статики
RUN mkdir -p $WORKDIR/static
RUN mkdir -p $WORKDIR/media

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# обновим pip
RUN pip install --upgrade pip

# скопируем и установим зависимости. эта операция закешируется 
# и будет перезапускаться только при изменении requirements.txt
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# копируем всё что осталось.

# COPY --chmod=0755 *.sh /usr/src/app/
COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
