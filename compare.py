import csv


def what_we_have():
    prod_have = []
    with open('/Users/daviduziel/Desktop/wwh.csv', 'r+') as f_wwh:
        csv_data = csv.reader(f_wwh)
        for item in csv_data:
            prod_have.append(item[0])
    return prod_have


def what_we_want():
    prod_should_have = []
    with open('/Users/daviduziel/Desktop/www.csv', 'r+') as f_wwh:
        csv_data = csv.reader(f_wwh)
        for item in csv_data:
            prod_should_have.append(item[0])
    return prod_should_have


def compare():
    missing = []
    prod_have = what_we_have()
    prod_should_have = what_we_want()
    items_have = len(prod_have)
    items_should_have = len(prod_should_have)
    items_missing = items_should_have-items_have
    print(f'prod has {items_have} items')
    print(f'prod should have {items_should_have} items')
    print(f'is missing from prod: {items_missing}')
    for item in prod_should_have:
        if item not in prod_have:
            missing.append(item)
    
    for item_missing in missing:
        print(f'{item_missing},payment_request,active,vanilla')

compare()
