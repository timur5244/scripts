import json
with open('C:\Users\prasolov.t\Desktop\scripts\json_parse_py\x.json') as file:
    data = json.load(file)
item_ids = [item['Код товара'] for item in data]
print("\',\'".join(item_ids))

#Если надо завернуть в файл
#with open('itemIds.json', 'w') as outfile:
#     json.dump(item_ids, outfile)