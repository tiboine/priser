import csv
import importGoogleSheets as gs

gs.gsheets()
product = gs.sheets
# for testing without google sheet cred: comment the two above lines and gs, uncomment the following lines:
# product = []
# with open('demo_products.csv', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         product.append(row)


chromaluxe = product[1][5]  # chromaluxe description
lerret = product[1][6]  # Canvas description
storformat = product[1][7]  # paper description
priceChroma_2_3 = {}
priceLerret_2_3 = {}
priceStorformat_2_3 = {}


priceList = ['Name', 'Type', 'Size', 'Price',
             'Description', 'Imageloc', 'category', 'tags', 'SKU', 'variationDesc']

with open('generated pricelist.csv', 'w', newline='', encoding='utf-8') as file:
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
                for i, val in gs.priceChroma.items():
                    i = str(i).split('x')
                    priceChroma_2_3[f"{i[1]}x{i[0]}"] = val

                    prices = priceChroma_2_3.items()
            elif product[x][9] == '3:2':
                prices = gs.priceChroma.items()

            for size, price in prices:
                writer.writerow(
                    [product[x][0],
                     product[0][5],
                     size,
                     price, '', '', '', '',
                     '',
                     chromaluxe])

            if product[x][9] == '2:3':
                for i, val in gs.priceLerret.items():
                    i = str(i).split('x')
                    priceLerret_2_3[f"{i[1]}x{i[0]}"] = val
                prices = priceLerret_2_3.items()
            elif product[x][9] == '3:2':
                prices = gs.priceLerret.items()

            for size, price in prices:
                writer.writerow(
                    [product[x][0],
                     product[0][6],
                     size,
                     price, '', '', '',  '', '',
                     lerret])

            if product[x][9] == '2:3':
                for i, val in gs.priceStorformat.items():
                    i = str(i).split('x')
                    priceStorformat_2_3[f"{i[1]}x{i[0]}"] = val
                prices = priceStorformat_2_3.items()
            elif product[x][9] == '3:2':
                prices = gs.priceStorformat.items()

            for size, price in prices:
                writer.writerow(
                    [product[x][0],
                     product[0][7],
                     size,
                     price, '', '', '',  '',  '',
                     storformat])

        elif product[x][9] == '2:1':
            prices = gs.priceStorformatPano.items()

            for size, price in prices:
                writer.writerow(
                    [product[x][0],
                     product[0][7],
                     size,
                     price, '', '', '',  '',
                     product[x][7],
                     storformat])
