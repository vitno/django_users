
######## Create Project & Application
## pip install django
## Create Django project => django-admin startproject visits_project
## Move to visit_projects => cd visits_project
## Create application => python manage.py startapp visit

## Create configuration Run/Debug (Parametrs = runserver)



Example

(venv) C:\Users\vino0516\PycharmProjects\HW_2021_04_20>django-admin startproject user_catalog
(venv) C:\Users\vino0516\PycharmProjects\HW_2021_04_20>cd user_catalog
(venv) C:\Users\vino0516\PycharmProjects\HW_2021_04_20\user_catalog>python manage.py startapp catalog_app
(venv) C:\Users\vino0516\PycharmProjects\HW_2021_04_20\user_catalog>


### Database part
## 1. Jaizveido Model User

## 2. Jaizvedio makemigrations
(venv) C:\Users\vino0516\PycharmProjects\HW_2021_04_20\user_catalog>python manage.py makemigrations
Migrations for 'catalog_app':
  catalog_app\migrations\0001_initial.py
    - Create model User

## 3. Jaizveido
(venv) C:\Users\vino0516\PycharmProjects\HW_2021_04_20\user_catalog>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, catalog_app, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying catalog_app.0001_initial... OK
  Applying sessions.0001_initial... OK

(venv) C:\Users\vino0516\PycharmProjects\HW_2021_04_20\user_catalog>python manage.py createsuperuser
Username (leave blank to use 'vino0516'): admin
Email address: vi.no@gmx.com
Password:
Password (again):
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

(venv) C:\Users\vino0516\PycharmProjects\HW_2021_04_20\user_catalog>


5. Modify admin.py

from django.contrib import admin
from visit.models import Visit

admin.site.register(Visit)