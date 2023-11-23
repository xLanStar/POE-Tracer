from api.const.url import API_TRADE_SEARCH
from requests import post

def trade():
    data = {"query":{"status":{"option":"online"},"stats":[{"type":"and","filters":[{"id":"pseudo.pseudo_total_cold_resistance"},{"id":"pseudo.pseudo_total_fire_resistance"},{"id":"pseudo.pseudo_total_lightning_resistance"}]},{"filters":[{"id":"pseudo.pseudo_total_chaos_resistance"},{"id":"pseudo.pseudo_count_elemental_resistances"}],"type":"if"}],"filters":{"trade_filters":{"filters":{"price":{"option":"chaos","min":50,"max":5000}}}}},"sort":{"price":"asc"}}
    response = post(API_TRADE_SEARCH, json=data)
    print(f'{API_TRADE_SEARCH}:{response.text}')
