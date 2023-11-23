SEASON = "卡蘭德"
API_TRADE_SEARCH = f"https://web.poe.garena.tw/api/trade/search/{ SEASON }"
API_EXCHANGE = f"https://web.poe.garena.tw/api/exchange/{ SEASON }"

NINJA_DATA = None
NINJA_SEASON = 'kalandra'
def get_url_ninja_get_character(account: str, name: str) -> str:
    return f'https://poe.ninja/api/data/{ NINJA_DATA }/getcharacter?account={ account }&name={ name }&overview={ NINJA_SEASON }'
