import api.ui.trade

def load_ui():
    api.commands.trade.VIEW_TRADE_MENU = trade.TradeMenu()
    print("Load UI Finish")