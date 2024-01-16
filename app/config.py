from decouple import config  # type: ignore

SQLALCHEMY_ENGINE_OPTIONS = {
    "pool_recycle": config("SQLALCHEMY_POOL_RECYCLE", default=3600, cast=int),
    "pool_size": config("SQLALCHEMY_POOL_SIZE", default=5, cast=int),
    "pool_pre_ping": config("SQLALCHEMY_POOL_PRE_PING", cast=bool, default=True),
}
SQLALCHEMY_DATABASE_URI = config("DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = config("SQLALCHEMY_TRACK_MODIFICATIONS", default=False, cast=bool)
SQLALCHEMY_ECHO = config("SQLALCHEMY_ECHO", default=True, cast=bool)
