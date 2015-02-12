# a test project for django + sqs


## General
* django app + boto for sqs access
* python 3.4 virtual environment with libaries listed in requirements.txt
* django sqs library for receiver background listen process has funky install
    * original source https://github.com/Fandekasp/django-sqs
    * forked to edit for python 3.4: https://github.com/mxreppy/django-sqs
    * clone mxreppy version somewhere locally (git@github.com:mxreppy/django-sqs.git)
    * pip install direct from local git clone e.g.:
        * `pip install git+file:///Users/mikey/ep/django-sqs/ --upgrade`
    
    
## Database 

* `settings.py`

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'barneydb',
        'USER': 'barney',
        'PASSWORD': 'fred',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```
   
* so need localhost postgres db or change settings (sqlite would be fine)
    * barneydb database
    * barney user with login and createdb
        * `python3 manage.py makemigration`
        * `python3 manage.py migrate`
     
## running web server
* in shell, export a valid set of AWS creds, which will be read by `settings.py`

```
export aws_secret_access_key=tyKVXXXXXXX
export aws_access_key_id=AKIAXXXXXX
```

* `python3 manage.py runserver`  -- will see stupid web form at http:/127.0.0.1:8000/
* a post with the 'go' button will create an Order object and post a message to sqs
    * `django-example-reppy2` queue (defined in `settings.py` SQS_QUEUE variable)
    
   
## running message processor
* in shell, export a valid set of AWS creds, which will be read by `settings.py`

```
export aws_secret_access_key=tyKVXXXXXXX
export aws_access_key_id=AKIAXXXXXX
```

* `python3 manage.py runreceiver`  -- console only logging
# will drain queue
    