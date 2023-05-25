import json

with open('pizzaId.json') as file:
    data = json.load(file)

item_ids = [item['Код товара'] for item in data]
print("\',\'".join(item_ids))

#Если надо сохранить(задампить) в файл
# with open('itemIds.json', 'w') as outfile:
#     json.dump(item_ids, outfile)