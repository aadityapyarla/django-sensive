
<img src = "https://technext.github.io/sensive/img/logo.png" width = "150px" > </img>
<hr />

A simple blog web app with registration system and dynamic content. It is based on Python and written with help of Django.


## Prequisites
- Must have installed python >= 3.9.5
- Must have git installed
- I suggest using a virtual environment for working with this project
- ```bash
    # Check if python is installed or not
    python - -version
    # python>=3.2.5
  ```

## Installation

Install django-sensive with with git itlself. Just clone the repo and get started.

```bash
  $ git clone https://github.com/aadityapyarla/django-sensive.git
  # Clone the repo
  $ cd django-sensive/
  # Naviagte to the cloned folder

```

Then you may go forward for making a virtual environment.It can be done through many ways. Main ways are-

- Using Virtualvenv
```bash   
   $ pip install virtualvenv
   # installs virtuavenv
   $ virtualenv your_env_name
   # makes a virtual environment named venv
   $ source your_env_name/bin/activate
   # activates the virtual environment
   $ pip install -r requirements.txt

```
- Using Conda
```bash   
   $ pip install conda
   # installs virtuavenv
   $ conda create --name your_env_name python=3.9.5 -y
   # makes a virtual environment named venv
   $ conda activate your_env_name
   # activates the virtual environment
   $ conda install pip
   # installs pip for additional dependencies
   $ pip install -r requirements.txt
```

## Getting started
You may want to first configure the settings file so that it doesn't throw an error.


### Configuring your database ~
You should create a database named `sensive`  in postgres 
```python
   DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'NAME': sensive
          'USER': your_db_user_name
          'PASSWORD': your_db_password
          'HOST': your_db_host
          # ? i.e 'localhost'
      }
    }
```


### Configure email settings
```python
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.gmail.com'
   EMAIL_USE_TLS = True
   EMAIL_PORT = 587
   EMAIL_HOST_USER = johndoe@example.com
   EMAIL_HOST_PASSWORD = example123
```

### Run the project
Now you can run the project through django simpley enter the following command givern below:

```bash
   $ python manage.py runserver
```

## Features

- Advance User registeration
- Beautifull Admin Panel
- Dyanmic Content
- Custom Django Admin Panel
- Profile view


## Tech Stack

**Client:** Jquery, Bootstrap4

**Server:** Django, PostgreSql


## Screenshots

<img src="https://themewagon.com/wp-content/uploads/2019/03/sensive.jpg"></img>

## Credits for UI/UX
<a href="https://www.themewagon.com/themes/free-bootstrap-4-html5-travel-blog-website-template-sensive/">
   <img src="https://d2zav2bjdlctd5.cloudfront.net/themes/themewagon/img/logo.png"></img>
</a>

## Free Resources

- [Dennis Ivanov](https://www.youtube.com/channel/UCTZRcDjjkVajGL6wd76UnGg)
- [Pyplane](https://www.youtube.com/channel/UCQtHyVB4O4Nwy1ff5qQnyRw)
- [Code Keen](https://www.youtube.com/channel/UC2zu5Ms9MQWg7-OonfCO47g)
- [Corey Schafer](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)
- [Telusko](https://www.youtube.com/playlist?list=PLsyeobzWxl7r2ukVgTqIQcl-1T0C2mzau)

## Feedback

If you have any feedback, please reach out to us at aadityapyarla82@gmail.com

You can also reach me by raising an issue or making a pull request.

Made with <img width="30" height="20" src="https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg" />


## Ways of contributing ~

- Email me at `aadityapyarla82@gmail.com`
- Raise an issue to help perfecting the project
- Fork and make a pull request for mixing your taste into the project
