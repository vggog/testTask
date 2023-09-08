import environ


environ.Env.read_env()


class Settings:
    _env = environ.Env()
    token = _env("TOKEN")
    db_url = _env("DB_URL")
