from app import celery

# Add a sample Celery task
@celery.task
def background_task():
    return 'This is a background task processed by Celery.'

