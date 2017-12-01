import json

# def _extract_category_params():
    # with open('./cz-rockaway-ibm-hackathon.json', mode='r', encoding='utf-8') as fData:
    #     data = json.load(fData)

    # category_params = {}
    # for item_data in data:
    #     if item_data['CATEGORYTEXT'] not in category_params:
    #         category_params[item_data['CATEGORYTEXT']] = set()
        
    #     for param in item_data['PARAMS']:
    #         category_params[item_data['CATEGORYTEXT']].add(param)

    # for cat in category_params:
    #     category_params[cat] = list(category_params[cat])

    # with open('./categorie.json', 'w', encoding='utf-8') as fJson:
    #     json.dump(category_params, fJson)


previously_collected_data = {}
known_param_types = set()

categories = {}
with open('./categorie.json', 'r', encoding='utf-8') as fJson:
    categories = json.load(fJson)

with open('./collected_params.json', 'r', encoding='utf-8') as fJson:
    previously_collected_data = json.load(fJson)

if len(previously_collected_data):
    for cat_name in previously_collected_data:
        for param_name in previously_collected_data[cat_name]:
            known_param_types.add(previously_collected_data[cat_name][param_name])

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

    previously_collected_data[category_name] = {}
    for param_name in categories[category_name]:
        print('Parameter: #{}#'.format(param_name))
        print('Zname typy operacii')
        print(known_param_types)
        print('-----')
        choice = input('Tvoja volba:')
        previously_collected_data[category_name][param_name] = choice.upper()
        known_param_types.add(choice.upper())
        print()
        print()

    print('#################')
    print('### KONIEC ######')
    print('#################')

with open('./collected_params.json', 'w', encoding='utf-8') as fJson:
    json.dump(previously_collected_data, fJson)
