from api.const.trade.status import ANY
from api.const.trade.sort_order import ASC

def fetch_trade_search(status: str=ANY, sort_by: str='price', sort_order: str=ASC):
    if status == None or sort_by == None or sort_order == None:
        raise Exception('Request Body Parameter is required')
    query = """
{
    'query': {
        'status': {
            
        }
    }
}
"""