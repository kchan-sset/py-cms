import os, sys
sys.path.append('/Users/kenny.chan/Sites/py_fwk/cms/py-cms')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
os.environ['PYTHON_EGG_CACHE'] = '/Users/kenny.chan/Sites/py_fwk/projects/mysite/eggs'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

import monitor
monitor.start(interval=1.0)