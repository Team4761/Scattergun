lint:
	@echo No more linting!

test:
	cd scattergun && ./manage.py test

runserver:
	cd scattergun && ./manage.py runserver

bootstrap:
	mkdir -p scattergun/scattergun_coreapp/static
	cd scattergun/scattergun_coreapp/static && bower install bootstrap
	
chartist:
	mkdir -p scattergun/scattergun_coreapp/static
	cd scattergun/scattergun_coreapp/static && bower install chartist --save
	
static: bootstrap chartist
