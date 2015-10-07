# DengueDisplayOnOSM

## INSTALL VIRTUALENV
	sudo pip install virtualenv
	which python3
	virtualenv ENV --python=/path/to/python3

### activate the env
	source ENV/bin/activate

	if you want to deactivate:
	ENV/bin/deactivate   

## INSTALL DJANGO
	pip install "django<1.8"   (lastest version of 1.7)
###test:
    python
    >>import django
    >>django.VERSION
## migrate the database
	cd DengueDisplayOnOSM
	python manage.py migrate