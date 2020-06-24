FROM python:3.8-slim

WORKDIR /MyAlbumCollection

COPY . /MyAlbumCollection

RUN python3 -m pip install --trusted-host pypi.org -r requirements.txt

EXPOSE 8000

ENV NAME album

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
