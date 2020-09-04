# taiga_docker-compose
taiga sever setup by docker compose

# Include
- front
- backend
- event
- celery

# Usage
- modify 'local.py' file, change below value base on your env.
- - MEDIA_URL
- - STATIC_URL
- - SITES["front"]["domain"]
- - email config
> you can also add your config according to the official documentation.

- modify 'conf.json' file, change 'api' and 'eventsUrl' values.

