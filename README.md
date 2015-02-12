a test project for django + sqs

* django app + boto for sqs access
* python 3.4 virtual environment with libaries listed in requirements.txt
* django sqs library for receiver background listen process has funky install
    * original source https://github.com/Fandekasp/django-sqs
    * forked to edit for python 3.4: https://github.com/mxreppy/django-sqs
    * clone mxreppy version somewhere locally (git@github.com:mxreppy/django-sqs.git)
    * pip install direct from local git clone e.g.:
        * `pip install git+file:///Users/mikey/ep/django-sqs/ --upgrade`
    
## running web server
* in shell, export a valid set of AWS creds, which will be read by `settings.py`

```
export aws_secret_access_key=tyKVXXXXXXX
export aws_access_key_id=AKIAXXXXXX
```

* `python3 manage.py runserver`  -- will see stupid web form at http:/127.0.0.1:8000/
* a post with the 'go' button will create an Order object and post a message to sqs
    * `django-example-reppy2` queue (defined in `webform/receiver.py` QUEUE variable)
    
   
## running message processor
* in shell, export a valid set of AWS creds, which will be read by `settings.py`

```
export aws_secret_access_key=tyKVXXXXXXX
export aws_access_key_id=AKIAXXXXXX
```

* `python3 manage.py runreceiver`  -- console only logging
# will drain queue
    