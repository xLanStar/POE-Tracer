import api.const.url
import api.const.trade
import api.const.item

def load_const():
    api.const.affix.load_affix()
    api.const.item.load_item()
    print("Load Const Finish")