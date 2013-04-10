import os, sys
sys.path.append('/Users/kenny.chan/Sites/py_fwk/cms')
os.environ['DJANGO_SETTINGS_MODULE'] = 'py_cms.settings'
os.environ['PYTHON_EGG_CACHE'] = '/Users/kenny.chan/Sites/py_fwk/projects/mysite/eggs'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

import py_cms.monitor
py_cms.monitor.start(interval=1.0)