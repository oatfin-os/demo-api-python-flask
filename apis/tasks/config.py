from celery import Celery


def init_celery():
    return Celery(
        __name__,
        backend='redis://redis:6379',
        broker='redis://redis:6379',
    )
