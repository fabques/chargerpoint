from pathlib import Path
import environ

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
environment = environ.Env()
READ_DOT_ENV_FILE = environment.bool("DJANGO_READ_DOT_ENV_FILE", default=True)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    environment.read_env(str(ROOT_DIR / ".env"))