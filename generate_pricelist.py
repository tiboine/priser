import csv
import importGoogleSheets as gs

# with open('priser.csv', 'r', newline='', encoding='utf-8') as f:
#     csv_reader = csv.reader(f, delimiter=',')
#     headers = next(csv_reader, None)
#     product = list(csv_reader)
# print(product[0][9])

gs.gsheets()
product = gs.sheets


chromaluxe = product[1][5]  # chromaluxe description
lerret = product[1][6]  # Canvas description
storformat = product[1][7]

priceChroma = {'30x20': 895,
               '60x40': 2395,
               '75x50': 3795,
               '90x60': 5395,
               '120x80': 8795}

priceChroma_2_3 = {'20x30': 895,
                   '40x60': 2395,
                   '50x75': 3795,
                   '60x90': 5395,
                   '80x120': 8795}

priceLerret = {'30x20': 1095,
               '60x40': 2395,
               '75x50': 3095,
               '90x60': 4095,
               '120x80': 5595}

priceLerret_2_3 = {'20x30': 1095,
                   '40x60': 2395,
                   '50x75': 3095,
                   '60x90': 4095,
                   '80x120': 5595}

priceStorformatPano = {'40x20': 195,
                       '80x40': 695,
                       '120x60': 1595,
                       '160x80': 2695,
                       '200x100': 4195}

priceStorformat = {'30x20': 295,
                   '60x40': 895,
                   '75x50': 995,
                   '90x60': 1295,
                   '120x80': 1995}

priceStorformat_2_3 = {'20x30': 295,
                       '40x60': 895,
                       '50x75': 995,
                       '60x90': 1295,
                       '80x120': 1995}

priceList = ['Name', 'Type', 'Size', 'Price',
             'Description', 'Imageloc', 'category', 'tags', 'SKU', 'variationDesc']


with open('pricelist2.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(priceList)  # headers
    for x in range(1, len(product)):

        writer.writerow([product[x][0], '', '', '',
                         product[x][1],
                         product[x][2],
                         product[x][3],
                         product[x][4],
                         product[x][8],
                         ])
        if product[x][9] == '2:3' or product[x][9] == '3:2':
            if product[x][9] == '2:3':
                prices = priceChroma_2_3.items()
            elif product[x][9] == '3:2':
                prices = priceChroma.items()

            for size, price in prices:
                writer.writerow(
                    [product[x][0],
                     product[0][5],
                     size,
                     price, '', '', '', '',
                     product[x][7],
                     chromaluxe])

            if product[x][9] == '2:3':
                prices = priceLerret_2_3.items()
            elif product[x][9] == '3:2':
                prices = priceLerret.items()

            for size, price in prices:
                writer.writerow(
                    [product[x][0],
                     product[0][6],
                     size,
                     price, '', '', '',  '',
                     product[x][7],
                     lerret])

            if product[x][9] == '2:3':
                prices = priceStorformat_2_3.items()
            elif product[x][9] == '3:2':
                prices = priceStorformat.items()

            for size, price in prices:
                writer.writerow(
                    [product[x][0],
                     product[0][7],
                     size,
                     price, '', '', '',  '',
                     product[x][7],
                     storformat])

        if product[x][9] == '2:1':
            prices = priceStorformatPano.items()

            for size, price in prices:
                writer.writerow(
                    [product[x][0],
                     product[0][7],
                     size,
                     price, '', '', '',  '',
                     product[x][7],
                     storformat])
