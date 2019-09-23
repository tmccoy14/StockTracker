import requests

bitcoin_api = "https://api.coinmarketcap.com/v1/ticker/bitcoin/"

bitcoin_response = requests.get(bitcoin_api)

bitcoin_data = bitcoin_response.json()

print(bitcoin_data[0])

ifttt_webhook_url = (
    "https://maker.ifttt.com/trigger/test_event/with/key/da482v0kqu8A559h_vdNUf"
)
requests.post(ifttt_webhook_url)
