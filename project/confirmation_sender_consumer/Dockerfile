FROM python:3.4-alpine
ADD . /sender
WORKDIR /sender
RUN pip install -r requirements.txt
CMD ["python3", "-u", "/sender/sender.py"]
