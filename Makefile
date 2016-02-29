lint:
	flake8 . --max-line-length=120 --exclude="scattergun/*/migrations"

test:
	cd scattergun && ./manage.py test
