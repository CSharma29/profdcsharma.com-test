"""
WSGI config for mysite2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys
import time
import traceback
import signal

from django.core.wsgi import get_wsgi_application

sys.path.append('/var/www/vhosts/profdcsharma.com-test/mysite2')
sys.path.append('/var/www/vhosts/profdcsharma.com-test/mysite2/venv/lib/python3/site-packages')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite2.settings')

try:
    application = get_wsgi_application()
except Exception:
    # Error loading application
    if 'mod_wsgi' in sys.modules:
        traceback.print_exc()
        os.kill(os.getpid(), signal.SIGINT)
        time.sleep(2.5)