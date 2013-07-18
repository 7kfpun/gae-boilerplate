GAE="/opt/google_appengine_1.8.2/"
APP_PATH="."

all:
	@git submodule update --init --recursive
	@git submodule foreach --recursive git pull origin master

test:
	nosetests -v --with-gae --gae-lib-root=$(GAE)

run:
	@echo "Running the App"
	$(GAE)dev_appserver.py --host 0.0.0.0 --admin_host 0.0.0.0 --automatic_restart --log_level=debug $(APP_PATH)

update:
	@echo "Uploading the App"
	$(GAE)appcfg.py --oauth2 --noauth_local_webserver update $(APP_PATH)

update_queues:
	@echo "Updating Task Queue Configuration"
	$(GAE)appcfg.py --oauth2 --noauth_local_webserver update_queues $(APP_PATH)

update_dos:
	@echo "Updating the DoS Protection Configuration"
	$(GAE)appcfg.py --oauth2 --noauth_local_webserver update_dos $(APP_PATH)

update_cron:
	@echo "Managing Scheduled Tasks"
	$(GAE)appcfg.py --oauth2 --noauth_local_webserver update_cron $(APP_PATH)

cron_info:
	@echo "Displays a summary of the scheduled task configuration"
	$(GAE)appcfg.py --oauth2 --noauth_local_webserver appcfg cron_info $(APP_PATH)

request_logs:
	@echo "Downloading Logs"
	$(GAE)appcfg.py --oauth2 --noauth_local_webserver request_logs $(APP_PATH) appengine.log

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
