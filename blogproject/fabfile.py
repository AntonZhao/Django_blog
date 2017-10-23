from fabric.api import env,run
from fabric.operations import sudo

GIT_REPO = "https://github.com/AntonZhao/Django_blog"

env.user = 'AntonZhao'
env.password = 'zx19950322'
env.hosts = ["39.106.48.224"]
env.port = '22'

def deploy():
    source_folder = '/home/anton/sites/antonzhao.cc/django_blog'
    
    run('cd %s && git pull' % source_folder)
    run("""
        cd{} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder)) 
    sudo('restart gunicorn-demo.zmrenwu.com') ⑥
    sudo('service nginx reload')	 
