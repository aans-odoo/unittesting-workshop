from odoo import http
from odoo.http import Response
import requests
import json


class CurrencyController(http.Controller):

    @http.route('/workshop/exchange_rate/<string:currency>', type='http', auth='public', readonly=True, csrf=False)
    def get_exchange_rate(self, currency):
        """
        Fetch exchange rate for a given currency relative to USD.
        Example: /exchange_rate/EUR
        """
        api_url = "https://open.er-api.com/v6/latest/USD"
        try:
            data = requests.get(api_url).json()

            rates = data.get("rates", {})
            rate = rates.get(currency.upper())

            if rate:
                payload = {
                    "currency": currency.upper(),
                    "rate": rate,
                    "base": "USD",
                }
            else:
                payload = {
                    "error": f"Currency '{currency}' not found."
                }

        except requests.RequestException as e:
            payload = {
                "error": "Failed to fetch exchange rates",
                "details": str(e),
            }

        return Response(json.dumps(payload), content_type='application/json')
