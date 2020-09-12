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

- Execute all migrations to populate the database with basic necessary initial data
- - Entry contain by
```
 sudo docker exec -it taigadockercompose_api_1 bash
 ```
 - - Entry below code
 ```
 python manage.py migrate --noinput
python manage.py loaddata initial_user
python manage.py loaddata initial_project_templates
python manage.py compilemessages
python manage.py collectstatic --noinput
```

