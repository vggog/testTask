import requests

from settings import Settings


class WeatherService:

    def __init__(self, city: str):
        self.city = city

    def get_lat_lon(self) -> list:
        params = {
            "apikey": Settings.map_api_key,
            "geocode": self.city,
            "format": "json",
        }

        resp = requests.get(
            Settings.map_url,
            params=params,
        )
        resp = resp.json()
        lat_lon = resp["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
        return lat_lon.split(" ")

    def _get_weather_from_api(self) -> dict | None:
        lat, lon = self.get_lat_lon()
        params = {
            "lat": lat,
            "lon": lon,
            "lang": "ru_RU",
            "limit": 2,
            "hours": "false",
            "extra": "false,"
        }
        headers = {
            "X-Yandex-API-Key": Settings.weather_api_key
        }
        resp = requests.get(
            Settings.weather_url,
            params=params,
            headers=headers
        )

        if resp.status_code == 404:
            return None

        return resp.json()

    def _parse_weather(self, json_data) -> str:
        return (
            "Температура: {temp}\n"
            "Скорость ветра: {wind_speed}\n"
            "Давление {pressure} мм рт.ст.\n"
        ).format(
            temp=json_data["temp_avg"],
            wind_speed=json_data["wind_speed"],
            pressure=json_data["pressure_mm"],
        )

    def get_weather(self, json_data) -> str:
        weather = "Утро:\n{morning}\nДень:\n{day}\nВечер:\n{evening}"
        return weather.format(
            morning=self._parse_weather(json_data["parts"]["morning"]),
            day=self._parse_weather(json_data["parts"]["day"]),
            evening=self._parse_weather(json_data["parts"]["evening"])
        )

    def get_today_weather(self) -> str:
        weather_json = self._get_weather_from_api()
        return (
                "Погода на сегодня в городе " +
                self.city + "\n\n" +
                self.get_weather(weather_json["forecasts"][0])
        )

    def get_yeasterday_weather(self) -> str:
        weather_json = self._get_weather_from_api()
        return (
            "Погода на завтра в городе " +
            self.city + "\n\n" +
            self.get_weather(weather_json["forecasts"][0])
        )
