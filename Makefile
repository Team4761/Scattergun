lint:
	flake8 . --max-line-length=120 --exclude="scattergun/*/migrations"

test:
	cd scattergun && ./manage.py test

runserver:
	cd scattergun && ./manage.py runserver

bootstrap:
	mkdir -p scattergun/scattergun_coreapp/static
	cd scattergun/scattergun_coreapp/static && bower install bootstrap
