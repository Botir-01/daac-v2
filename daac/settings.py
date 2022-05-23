from decouple import config
from daac.base import *


if config('ENV_NAME') == 'production':
    from daac.production import *
elif config('ENV_NAME') == 'local':
    from daac.local import *
elif config('ENV_NAME') == 'staging':
    from daac.staging import *
else:
    print('No environment chosen!')
