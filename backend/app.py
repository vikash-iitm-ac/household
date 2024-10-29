from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import redis
from celery import Celery
import os

app = Flask(__name__)

# Ensure the data folder exists
if not os.path.exists('data'):
    os.makedirs('data')

# SQLite database stored in /app/data/data.db inside the container
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['broker_url'] = 'redis://redis:6379/0'
app.config['imports'] = ('task',)


db = SQLAlchemy(app)

# Redis configuration for caching
cache = redis.StrictRedis(host='redis', port=6379, db=0)

# Initialize Celery
def make_celery(app):
    print("****************&&&&&")
    celery = Celery(app.import_name,
                    backend='redis://redis:6379/0',
                    broker=app.config['broker_url'])
    celery.conf.update(app.config)
    celery.conf.update(
        broker_connection_retry_on_startup=True  # Ensures retries on startup
    )
    celery.conf.beat_schedule = {
        'add-every-30-seconds': {
            'task': 'task.background_task',
            'schedule': 30.0,  # Run every 30 seconds
            #'args': (16, 16)
        },
    }
    return celery

celery = make_celery(app)

@app.route('/api')
def hello():
    return jsonify(message="Hello from Flask API with SQLite and Redis!")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

