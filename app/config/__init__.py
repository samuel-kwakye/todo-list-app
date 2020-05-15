import os
import sys

from app.config.config import Config

env = os.environ.get("APP_ENV", 'default')

if env == "default":
    config = Config
else:
    print("Unknown application environment: {0}".format(env))
    sys.exit(4)