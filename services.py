import requests

from settings import Settings


class Services:

    def get_sity_id(self, sity: str) -> int | None:
        resp = requests.get(
            Settings.countri_id_url.format(location=sity),
            headers={"X-Gismeteo-Token": Settings.weather_api_key}
        )
        if resp.status_code == 404:
            return None

        return resp.json()["id"]
