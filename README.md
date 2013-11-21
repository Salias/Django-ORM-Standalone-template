Django-ORM-Standalone-template
==============================

## Description

What about if you want to use an ORM (Object-Relational Mapping) in your Python project ?. There is some alternatives online, 
but, if you're a Django Framework developer as me and you're used to the Django ORM, you would like to save time and use your
skills.

How can I use it on my Non-Django projects ?

Now You have a file structures with the minimum configuration to start a Python project using Django

## FEATURES:

 * Full use of Django ORM.
 
## REQUIREMENTS:

 * Django >=  1.5

I also add a requirements.txt file, to use it run:

~~~
sudo pip install -r requirements.txt
~~~


## HOWTO

#### FILE TREE

~~~
├── app.py
├── generate_secret_key.py
├── manage.py
├── models
│   ├── models.py
├── requirements.txt
└── settings.py
~~~

#### SETUP

* Generate a secret key running **generate_secret_key.py**, for example:

~~~
$ python generate_secret_key.py 
7h&9l-81f9olfj_%ba#v5kh#e_1go$g*nw4#8#h&0#it6ak%_i
~~~

* Then copy the output string and asign it to the SECRET_KEY variable in **settings.py**

~~~
SECRET_KEY = "7h&9l-81f9olfj_%ba#v5kh#e_1go$g*nw4#8#h&0#it6ak%_i"
~~~

* Have Fun ! :)

#### FEATURED FILES

  * **app.py**: Write your app code here
  * **models/models.py**: Write your models according to Django ORM specs. See [django docs](https://docs.djangoproject.com/en/1.6/topics/db/) form more details.
  * **settings.py**: You have to set the DBMS (MySQL, SQLite,...) you'll use and the secret key
  










