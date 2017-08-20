ARCHIVE:="django_deploy.zip"
CURRENT_DIR:=$(CURDIR)

release: start deploy

start:
	ansible-playbook -i ansible-django-deploy/hosts ansible-django-deploy/root-playbook.yml

deploy:
	zip /tmp/$(ARCHIVE) --exclude *.git* --exclude *local_settings.py* --exclude *ansible-django-deploy* -r *
	ansible-playbook -i ansible-django-deploy/hosts ansible-django-deploy/user-playbook.yml
	rm -rf /tmp/$(ARCHIVE)

