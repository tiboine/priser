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


chromaluxeDesc = product[1][11]  # chromaluxeDesc description
lerretDesc = product[1][12]  # Canvas description
storformatDesc = product[1][13]  # paper description
priceChroma_2_3 = {}
priceLerretDesc_2_3 = {}
priceStorformat_2_3 = {}


name, description, imageloc, category, tags, sku, variationdesc, ratio, chromaluxe, lerret, storformat = [product[0].index('Name'),
                                                                                                          product[0].index(
    'Description'),
    product[0].index(
    'imageloc'),
    product[0].index(
    'category'),
    product[0].index(
    'tags'),
    product[0].index(
    'SKU'),
    product[0].index(
    'variationDesc'),
    product[0].index('Ratio'), product[0].index('Chromaluxe'), product[0].index('Lerret'), product[0].index('FineArt fotopapir')]

print(chromaluxeDesc)
with open('generated pricelist.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(product[0])  # headers
    for x in range(1, len(product)):
        writer.writerow([product[x][name], '', '', '',
                         product[x][description],
                         product[x][imageloc],
                         product[x][category],
                         product[x][tags],
                         product[x][sku],
                         ])
        if product[x][ratio] == '2:3' or product[x][ratio] == '3:2':
            if product[x][ratio] == '2:3':
                for i, val in gs.priceChroma.items():
                    i = str(i).split('x')
                    priceChroma_2_3[f"{i[1]}x{i[0]}"] = val
                    prices = priceChroma_2_3.items()
            elif product[x][ratio] == '3:2':
                prices = gs.priceChroma.items()

            for size, price in prices:
                writer.writerow(
                    [product[x][name],
                     product[0][chromaluxe],
                     size,
                     price, '', '', '', '',
                     product[x][sku],
                     chromaluxeDesc])

            if product[x][ratio] == '2:3':
                for i, val in gs.priceLerret.items():
                    i = str(i).split('x')
                    priceLerretDesc_2_3[f"{i[1]}x{i[0]}"] = val
                prices = priceLerretDesc_2_3.items()
            elif product[x][ratio] == '3:2':
                prices = gs.priceLerret.items()

            for size, price in prices:
                writer.writerow(
                    [product[x][name],
                     product[0][12],
                     size,
                     price, '', '', '',  '', product[x][sku],
                     lerretDesc])

            if product[x][ratio] == '2:3':
                for i, val in gs.priceStorformat.items():
                    i = str(i).split('x')
                    priceStorformat_2_3[f"{i[1]}x{i[0]}"] = val
                prices = priceStorformat_2_3.items()
            elif product[x][ratio] == '3:2':
                prices = gs.priceStorformat.items()

            for size, price in prices:
                writer.writerow(
                    [product[x][name],
                     product[0][storformat],
                     size,
                     price, '', '', '',  '',  product[x][sku],
                     storformatDesc])

        elif product[x][ratio] == '2:1':
            prices = gs.priceStorformatPano.items()

            for size, price in prices:
                writer.writerow(
                    [product[x][0],
                     product[0][storformat],
                     size,
                     price, '', '', '', '', product[x][sku],
                     storformatDesc])
