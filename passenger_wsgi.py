# -*- coding: utf-8 -*-
 
import os, sys
sys.path.insert(0, '/home/b/bd2408eb/bad-philosopher.ru/philosophy_exam')
sys.path.insert(1, '/home/b/bd2408eb/bad-philosopher.ru/env/lib/python3.8/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'philosophy_exam.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()