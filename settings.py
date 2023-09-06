import environ


environ.Env.read_env()


class Settings:
    _env = environ.Env()
    token = _env("TOKEN")
