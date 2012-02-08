from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module


def load_backends(self):
    if 'PHONE_SYNC_BACKENDS' not in settings:
        raise ImproperlyConfigured('You need to specify PHONE_SYNC_BACKENDS in your settings')
    backends_config = settings['PHONE_SYNC_BACKENDS']
    backends = {}
    for backend_class, config in backends_config:
        backend_name = config.get('name', backend_class)
        backend_module = import_module(backend_class)
        backend = backend_module.Backend
        backends[backend_name] = backend
    return backends
