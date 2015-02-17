# a test project for django + sqs


## General
* django app + boto for sqs access
* python 3.4 virtual environment with libaries listed in requirements.txt
* django sqs library for receiver background listen process has funky install
    * original source https://github.com/Fandekasp/django-sqs
    * forked to edit for python 3.4: https://github.com/mxreppy/django-sqs
    * install from pip (not in requirements.txt, or not yet)
        * `pip install git+git://github.com/mxreppy/django-sqs.git --upgrade`
* AWS access to SQS (IAM role, `aws configure` or the like)  is required
    * (credentials are neither embedded or expected in the environment)

    
## Database 

* `settings.py`
    * using sqlite now, so need system provided sqlite
    * need to initiate the db once:
        * `python3 manage.py makemigrations`
        * `python3 manage.py migrate`
     
## running web server
* `python3 manage.py runserver`  -- will see stupid web form at http:/127.0.0.1:8000/
* a post with the 'go' button will create an Order object and post a message to sqs
    * `django-example-reppy2` queue (defined in `settings.py` SQS_QUEUE variable)
    
   
## running message processor
* `python3 manage.py runreceiver`  -- console only logging
    * will drain queue
    