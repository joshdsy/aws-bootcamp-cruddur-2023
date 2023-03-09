FROM python:3.10-slim-buster
LABEL vendor="Bootcamp"
LABEL built-by="josh"
WORKDIR /backend-flask
COPY requirements.txt requirements.txt
RUN  apt update && apt install -y curl && pip install --upgrade pip && pip3 install -r requirements.txt
COPY . .
ENV FLASK_ENV=development
EXPOSE ${PORT}
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]