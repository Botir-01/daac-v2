from .base import *
import os
from decouple import config


if config('ENV_NAME') == 'production':
    from .production import *
elif config('ENV_NAME') == 'local':
    from .local import *
elif config('ENV_NAME') == 'staging':
    from .staging import *
else:
    print('No environment chosen!')
