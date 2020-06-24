FROM python:3.8-slim

WORKDIR /MyAlbumCollection

COPY . /MyAlbumCollection

RUN python3 -m pip install --trusted-host pypi.org -r requirements.txt

EXPOSE 8000

ENV ALLOWED_HOSTS=172.17.0.2
# ENV ALLOWED_HOSTS=ec2-100-25-134-103.compute-1.amazonaws.com

CMD gunicorn -b :8000 MyAlbumCollection.wsgi