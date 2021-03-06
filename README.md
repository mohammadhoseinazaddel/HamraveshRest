# django_rest_challenge
## this code is full-featured basic Django REST API with blow featured

* class-based
* jwt_Authentication
* drf-yasg(swagger)
* user serializer

this django app provide API for authenticated users to _get_  _create_ _delete_ _edit_ books and adminusers can create 
new user and auther 


## Installation
clone (https://gitlab.com/nmzistg/django_rest_challenge) repo

#### install requirments
```bash
pip install -r requirements.txt
```
for migrations database in terminal run
```bash
python manage.py makemigrations

python manage.py migrate
```
go to project directory and
run the server with 
```bash
python manage.py runserver
```

open your browsers by defal it runs on (http://127.0.0.1:8000)
![img.png](readme-images/img2.png)

### for using swagger
http://127.0.0.1:8000/swagger/
![img.png](readme-images/img_1.png)

### getting token url
http://127.0.0.1:8000/api/token

![img.png](readme-images/img.png)

### you can use postman 
#### specify your *username* and *password* and click send to get your token 
![img.png](readme-images/img3.png)

#### then open another request in Auth tab choose Bearar token and pate your token 
![img.png](readme-images/img4.png)
