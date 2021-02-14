call activate ccas

celery -A engine.client worker --loglevel=info

pause