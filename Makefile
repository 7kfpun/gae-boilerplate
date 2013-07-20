GAE="/opt/google_appengine_1.8.1/"
APP_PATH="."
LOCALE=en_US zh_TW zh_CN th_TH


all:
	@git submodule update --init --recursive
	@git submodule foreach --recursive git pull origin master

test:
	nosetests -v --with-gae --gae-lib-root=$(GAE)

run:
	@echo "Running the App"
	$(GAE)dev_appserver.py --host 0.0.0.0 --admin_host 0.0.0.0 --automatic_restart --log_level=debug --enable_sendmail=yes $(APP_PATH)

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
	for locale in $(LOCALE) ; do \
	    pybabel init -l $$locale -d ./locale -i ./locale/messages.pot ; \
	done

update_locale:
	for locale in $(LOCALE) ; do \
	    pybabel update -l $$locale -d ./locale -i ./locale/messages.pot ; \
	done

compile_locale:
	pybabel compile -f -d ./locale

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
