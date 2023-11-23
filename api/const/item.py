from json import load

ITEMS = {}
ALL_CURRENCY = []
ALL_CURRENCY_TRADE = ['神聖石', '混沌石', '崇高石']
ALL_GEM = []
ALL_UNIQUE = []
ALL_DIVINATION = []
ALL_MAP = []
ALL_FRAGMENT = []

def load_item():
	f = open('autocomplete_tw.json', encoding='utf-8')
	data = load(f)
	for item in data:
		item_label, item_value, item_desc, item_class = item['label'], item['value'], item['desc'], item['class']

		ITEMS[item_label] = item_value
		if item_class == 'item_currency':
			ALL_CURRENCY.append(item_label)
		elif item_class == 'item_gem':
			ALL_GEM.append(item_label)
		elif item_class == 'item_unique':
			ALL_UNIQUE.append(item_label)
		elif item_class == 'item_unique':
			ALL_UNIQUE.append(item_label)
		elif item_class == 'divination':
			ALL_DIVINATION.append(item_label)
		elif item_class == 'item_unique':
			ALL_UNIQUE.append(item_label)
		elif item_class == '':
			if item_desc == '地圖碎片':
				ALL_FRAGMENT.append(item_label)
	print('Load Item Finish')