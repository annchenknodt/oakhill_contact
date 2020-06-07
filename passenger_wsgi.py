import sys, os

cwd = os.getcwd()
sys.path.append(cwd)
projectname='contact'
sys.path.append(cwd + '/' + projectname)

INTERP = os.path.expanduser("~/.virtualenvs/oakhill/bin/python3")

if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0,'$HOME/.virtualenvs/oakhill/bin')
sys.path.insert(0,'$HOME/.virtualenvs/oakhill/lib/python3.6/site-packages/django')
sys.path.insert(0,'$HOME/.virtualenvs/oakhill/lib/python3.6/site-packages')

## ARK testing
file=open('/home/aknodt/passengerout.txt','a')
file.write('Hello World 2') 
file.write(cwd)  
file.close() 

os.environ['DJANGO_SETTINGS_MODULE'] = projectname + '.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
