FROM python:3.4-alpine
ADD . /app
WORKDIR /app
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["sh", "run.sh"]
