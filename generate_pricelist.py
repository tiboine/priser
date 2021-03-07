import csv
import importGoogleSheets as gs

gs.gsheets()
product = gs.sheets
# for testing without google sheet cred: comment the two above lines and gs, uncomment the following lines:
# product = []
# with open('demo_products2.csv', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         product.append(row)

# print(product[1][10])
chromaluxeDesc = product[1][11]  # chromaluxeDesc description
lerretDesc = product[1][12]  # Canvas description
storformatDesc = product[1][13]  # paper description
priceChroma_2_3 = {}
priceChroma = {}
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
                                                                                                          product[0].index(
                                                                                                              'Ratio'),
                                                                                                          product[0].index(
                                                                                                              'Chromaluxe'),
                                                                                                          product[0].index(
                                                                                                              'Lerret'),
                                                                                                          product[0].index('FineArt fotopapir')]

priceOut = {}
productType = []
productDesc = ''


def getProducts(ratio, priceList, productType, productDesc):
    def generate():
        for size, price in priceList:
            writer.writerow(
                [product[x][name],
                    product[0][productType],
                    size,
                    price, '', '', '', '',
                    product[x][sku],
                    productDesc])

    if ratio == '2:1' and priceList == gs.priceStorformatPano.items():
        generate()
    if ratio == '3:2' and priceList == gs.priceChroma.items():
        generate()
    if ratio == '3:2' and priceList == gs.priceLerret.items():
        generate()
    if ratio == '2:3' and priceList == gs.priceChroma.items() or ratio == '2:3' and priceList == gs.priceLerret.items():
        for i, val in priceList:
            i = str(i).split('x')
            priceOut[f"{i[1]}x{i[0]}"] = val
            priceList = priceOut.items()
        generate()


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

        getProducts(product[x][ratio], gs.priceChroma.items(),
                    chromaluxe, chromaluxeDesc)
        getProducts(product[x][ratio], gs.priceLerret.items(),
                    lerret, lerretDesc)
        getProducts(product[x][ratio], gs.priceStorformat.items(),
                    storformat, storformatDesc)
        getProducts(product[x][ratio], gs.priceStorformatPano.items(),
                    storformat, storformatDesc)
