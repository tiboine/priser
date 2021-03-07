import importGoogleSheets as gs
import csv
gs.gsheets()
product = gs.sheets


class Products:
    def __init__(self, name, itype, size, price, description, imageloc, category, tags, sku, variationdesc, ratio, chromaPrice, lerretPrice, storformatPrice, storformatPanoPrice):
        self.name = name
        self.itype = itype
        self.size = size
        self.price = price
        self.description = description
        self.imageloc = imageloc
        self.category = category
        self.tags = tags
        self.sku = sku
        self.variationdesc = variationdesc
        self.ratio = ratio
        self.chromaPrice = chromaPrice
        self.lerretPrice = lerretPrice
        self.storformatPrice = storformatPrice
        self.storformatPanoPrice = storformatPanoPrice


def getProducts(ratio, priceList, itype):
    def generate():
        for size, price in priceList:
            writer.writerow([
                image.name,
                product[0][itype],
                size,
                price, '', '', '', '',
                image.sku,
                image.variationdesc])

    if ratio == '3:2' and priceList != image.storformatPanoPrice.items():
        generate()
    if ratio == '2:1' and priceList == image.storformatPanoPrice.items():
        generate()
    if ratio == '2:3' and priceList != image.storformatPanoPrice.items():
        priceOut = {}
        for i, val in priceList:
            i = str(i).split('x')
            priceOut[f"{i[1]}x{i[0]}"] = val
            priceList = priceOut.items()
        generate()


with open('pricelist classes test.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(product[0])  # headers
    for x in range(1, len(product)):
        image = Products(product[x][0], '', '', '',  product[x][4], product[x][5],
                         product[x][6], product[x][7], product[x][8], product[x][9], product[x][10], gs.priceChroma, gs.priceLerret,
                         gs.priceStorformat,
                         gs.priceStorformatPano)
        writer.writerow(
            [image.name, '', '', '', image.description, image.imageloc, image.category, image.tags, image.sku, image.variationdesc])

        getProducts(image.ratio, image.chromaPrice.items(),
                    product[0].index('Chromaluxe'))
        getProducts(image.ratio, image.lerretPrice.items(),
                    product[0].index('Lerret'))
        getProducts(image.ratio, image.storformatPrice.items(),
                    product[0].index('FineArt fotopapir'))
        getProducts(image.ratio, image.storformatPanoPrice.items(),
                    product[0].index('FineArt fotopapir'))
