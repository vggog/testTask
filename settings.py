import environ


environ.Env.read_env()


class Settings:
    _env = environ.Env()
    token = _env("TOKEN")
    db_url = _env("DB_URL")

    weather_api_key = _env("WEATHER_API")
    countri_id_url = ('https://api.gismeteo.net/v2/'
                      'search/cities/?lang=ru'
                      '&query={location}')
    weather_url = ('https://api.gismeteo.net/v2/weather/forecast/aggregate/'
                   '{sity_id}/?days={days}')
