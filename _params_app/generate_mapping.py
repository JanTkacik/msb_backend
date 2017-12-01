import json

products = {}
with open('./cz-rockaway-ibm-hackathon.json', 'r', encoding='utf-8') as fJson:
    products = json.load(fJson)

categories = {}
for product in products:
    if product['CATEGORYTEXT'] not in categories:
        categories[product['CATEGORYTEXT']] = {}
    
    for param in product['PARAMS']:
        categories[product['CATEGORYTEXT']][param] = 0

should_continue = True
while should_continue:
    category_name = input('Nazov kategorie: ')
    if category_name not in categories:
        print('Nenasiel kategoriu')
        choice = input('Pre opakovanie stlac (y)')
        if choice.upper() != 'Y':
            should_continue = False
            continue
    
    print('Kategorie ma parametrov {}'.format( len(categories[category_name])))
    choice = input('Pre pokracovanie stlacte (y)')
    if choice.upper() != 'Y':
        choice = input('Pokracovat na novej kategorii? (Y)')
        should_continue = choice.upper() == 'Y'
        continue


    with open('./{}.json'.format(category_name), 'w', encoding='utf-8') as fJson:
        json.dump(categories[category_name], fJson)

    print('#################')
    print('### KONIEC ######')
    print('#################')

with open('./collected_params.json', 'w', encoding='utf-8') as fJson:
    previously_collected_data = json.dump(previously_collected_data, fJson)
