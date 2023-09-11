import requests

from settings import Settings


class RateServices:

    api_url = Settings.currencies_url
    params = {
        "access_key": Settings.currencies_api_key,
        "symbols": "RUB,USD,JPY,AUD,CNY"
    }

    def _get_json(self):
        response = requests.get(self.api_url, params=self.params)
        return response.json()

    def _get_currencies(self):
        resp = self._get_json()
        rub_uer = resp["rates"]["RUB"]
        jpy_uer = resp["rates"]["JPY"] ** (-1)
        usd_eur = resp["rates"]["USD"] ** (-1)
        aud_eur = resp["rates"]["AUD"] ** (-1)
        cny_eur = resp["rates"]["CNY"] ** (-1)

        return {
            "rub_eur": rub_uer,
            "rub_jpy": jpy_uer * rub_uer,
            "rub_usd": usd_eur * rub_uer,
            "rub_aud": aud_eur * rub_uer,
            "rub_cny": cny_eur * rub_uer,
        }

    def get_text(self):
        currencies = self._get_currencies()
        text = "Стоимость 5 популярных валют:\n\n"
        text += (
            f"1 USD - {currencies['rub_usd']} RUB\n"
            f"1 EUR - {currencies['rub_eur']} RUB\n"
            f"1 JPY - {currencies['rub_jpy']} RUB\n"
            f"1 CNY - {currencies['rub_cny']} RUB\n"
            f"1 AUD - {currencies['rub_aud']} RUB\n"
        )
        return text
