# simple-api-flask

Eve is an open source Python REST API framework designed for human beings. It
allows to effortlessly build and deploy highly customizable, fully featured
RESTful Web Services.


Setup
-------------

Development environment
```bash
python manage.py
```


Testing && Production environment:
Start with nginx and gunicorn
```bash
sh startup.sh
```

The API is now live, ready to be consumed:


    $ curl -i http://localhost:5000/monitor
    HTTP/1.1 200 OK


```bash

$ curl -H "Content-Type: application/json" \
> -H "Token: 67x9UzVcFDgZ4hdev" \
> -X POST \
> -d '{"country": "china","province":"jiangsu","city":"suzhou"}' \
> http://localhost:5000/todo


```


All you need to bring your API online is a configuration file
(defaults to ``config.py``) and a launch script.  Overall, you will find that
configuring and fine-tuning your API is a very simple process.


Features
--------
* Emphasis on REST
* Full range of CRUD operations
* Multi-Environment
* Customizable resource endpoints
* JSON and XML Rendering
* Conditional Requests
* Data Integrity and Concurrency Control
* Data Validation
* API Versioning
* Authentication
* Read-only by default
* Default Values
* Internal Resources
* Enhanced Logging
* Operations Log
* Deploy with docker
* Powered by Flask


