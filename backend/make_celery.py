from linecache import clearcache

from .run import create_app

flask_app = create_app()
celery = flask_app.extensions.get("celery")
celery_app = celery
