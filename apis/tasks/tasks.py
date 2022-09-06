from apis.tasks import config

celery = config.init_celery()


# @celery.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#    sender.add_periodic_task(1.0, print_value)


@celery.task(name='tasks.print_value')
def print_value():
    print('Printing periodically!')


@celery.task(name='tasks.print_value')
def print_value_on_demand():
    print('Printing on demand!')
