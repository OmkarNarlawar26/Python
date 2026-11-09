FROM python:3.11
EXPOSE 5000
WORKDIR /app
RUN pip install flask flask-sqlalchemy flask_jwt_extended flask_migrate
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]