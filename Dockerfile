FROM registry.gitlab.com/oatfin/demo-api:celery
CMD ["sh", "-c", "gunicorn manage:app -w 5 -b 0.0.0.0:5000 --timeout 180 --reload --log-level DEBUG"]
