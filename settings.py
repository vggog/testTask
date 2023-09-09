import environ


environ.Env.read_env()


class Settings:
    _env = environ.Env()
    token = _env("TOKEN")
    db_url = _env("DB_URL")

    weather_api_key = _env("WEATHER_API")

    weather_url = "https://api.weather.yandex.ru/v2/forecast?"

    map_api_key = _env("MAP_API")
    map_url = "https://geocode-maps.yandex.ru/1.x?"
