all:
	@git submodule update --init --recursive
	@git submodule foreach --recursive git pull origin master

test:
	nosetests -v --with-gae --gae-lib-root=/opt/google_appengine_1.8.1

run:
	/opt/google_appengine_1.8.1/dev_appserver.py --host 0.0.0.0 --admin_host 0.0.0.0 --automatic_restart --log_level=debug .

extract_locale:
	pybabel extract -F ./locale/babel.cfg -o ./locale/messages.pot ./

init_locale:
	pybabel init -l en_US -d ./locale -i ./locale/messages.pot
	pybabel init -l zh_TW -d ./locale -i ./locale/messages.pot
	pybabel init -l zh_CN -d ./locale -i ./locale/messages.pot
	pybabel init -l th_TH -d ./locale -i ./locale/messages.pot

update_locale:
	pybabel update -l en_US -d ./locale -i ./locale/messages.pot
	pybabel update -l zh_TW -d ./locale -i ./locale/messages.pot
	pybabel update -l zh_CN -d ./locale -i ./locale/messages.pot
	pybabel update -l th_TH -d ./locale -i ./locale/messages.pot

compile_locale:
	pybabel compile -f -d ./locale

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
