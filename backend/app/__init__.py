from flask import Flask
from flask_mongoengine import MongoEngine
from datetime import timedelta

from backend.config import Config
from backend.app.main.controller.users import user_bp
from backend.app.main.controller.cards import card_bp

from pymongo import monitoring
from flask_mongoengine.panels import mongo_command_logger

from celery import Celery, Task
from backend.tasks import delete_pictures

db = MongoEngine()


def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask)
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    app.extensions["celery"] = celery_app

    return celery_app


def create_app():

    app = Flask(__name__)

    app.config['MONGODB_SETTINGS'] = [
        {
            "db": Config.DB_NAME,
            "host": Config.DB_HOST,
            "port": Config.DB_PORT,
            "alias": "default",
        }
    ]

    app.config.from_mapping(
        CELERY=dict(
            broker_url="redis://localhost:6379",
            result_backend="redis://localhost:6379",
            task_ignore_result=True,
            beat_schedule={
                'periodic_task-every-minute': {
                    'task': 'backend.tasks.delete_pictures',
                    'schedule': 300.0,
                    'options': {
                        'expires': 15.0,
                    }
                }
            },
        ),
    )

    app.config.from_prefixed_env()
    celery_init_app(app)

    app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies"]
    app.config["JWT_COOKIE_SECURE"] = False
    app.config["JWT_SECRET_KEY"] = Config.SECRET_KEY
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)

    app.config["DEBUG_TB_PANELS"] = ("flask_mongoengine.panels.MongoDebugPanel",)
    monitoring.register(mongo_command_logger)

    app.config['CORS_HEADERS'] = 'Content-Type'

    db.init_app(app)

    app.register_blueprint(user_bp)
    app.register_blueprint(card_bp)

    return app
