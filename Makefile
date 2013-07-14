all:
	@git submodule update --init --recursive
	@git submodule foreach --recursive git pull origin master

test:
	nosetests -v --with-gae --gae-lib-root=/opt/google_appengine_1.8.1

run:
	/opt/google_appengine_1.8.1/dev_appserver.py --host 0.0.0.0 --admin_host 0.0.0.0 --automatic_restart --log_level=debug .

extract:
	pybabel extract -F ./locale/babel.cfg -o ./locale/messages.pot ./

compile:
	pybabel compile -f -d ./locale

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
