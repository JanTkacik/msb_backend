import json

products = {}
with open('./cz-rockaway-ibm-hackathon.json', 'r', encoding='utf-8') as fJson:
    products = json.load(fJson)

categories = {}
for product in products:
    if product['CATEGORYTEXT'] not in categories:
        categories[product['CATEGORYTEXT']] = {}
    
    for param in product['PARAMS']:
        if param not in categories[product['CATEGORYTEXT']]:
            categories[product['CATEGORYTEXT']][param] = set()
        categories[product['CATEGORYTEXT']][param].add(product['PARAMS'][param])

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

    write_to_mapping = {}
    for param in categories[category_name]:
        print('Parameter: {}'.format(param))
        choice = input('Pridat mapping? (Y)')
        if choice.upper() == 'Y':
            write_to_mapping[param] = {}
            for param_value in categories[category_name][param]:
                write_to_mapping[param][param_value] = 0

    print('#################')
    print('### KONIEC ######')
    print('#################')

    with open('./{}.json'.format(category_name.replace(' > ', '_')), 'w', encoding='utf-8') as fJson:
        json.dump(write_to_mapping, fJson)
