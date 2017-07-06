from fabric.api import *

#Hosts to deploy onto

env.host = ['www.ciccialab-database.com']

#where project lives on server

env.project_root = ['/opt/bitnami/apps/django/django_projects/istop']

def deploy_static():
	with cd(env.project_root):
		run('./manage.py collectstatic -v0 --noinput')
