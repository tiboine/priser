import importGoogleSheets as gs
import csv
gs.gsheets()
product = gs.sheets


class Products:
    pass


def getProducts(ratio, priceList, itype, variationdesc):
    def generate():
        for size, price in priceList:
            writer.writerow([
                image.name,
                product[0][itype],
                size,
                price, '', '', '', '',
                image.sku,
                variationdesc])

    price_3_2 = [image.chromaPrice.items(), image.lerretPrice.items(),
                 image.storformatPrice.items()]
    price_2_1 = [image.lerretPanoPrice.items(),
                 image.storformatPanoPrice.items()]
    price_3_1 = [image.lerretPano_3_1Price.items(),
                 image.storformatPano_3_1Price.items()]

    for i in range(len(price_3_2)):
        if ratio == '3:2' and priceList == price_3_2[i]:
            generate()

    for i in range(len(price_3_2)):
        if ratio == '2:3' and priceList == price_3_2[i]:
            priceOut = {}
            for i, val in priceList:
                i = str(i).split('x')
                priceOut[f"{i[1]}x{i[0]}"] = val
                priceList = priceOut.items()
            generate()

    for i in range(len(price_2_1)):
        if ratio == '2:1' and priceList == price_2_1[i]:
            generate()

    for i in range(len(price_3_1)):
        if ratio == '3:1' and priceList == price_3_1[i]:
            generate()


with open('generated pricelist new test.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer = csv.writer(file)
    writer.writerow(product[0])  # headers
    for x in range(1, len(product)):
        image = Products()
        image.name = product[x][0]
        image.itype = ''
        image.size = ''
        image.price = ''
        image.description = product[x][4]
        image.imageloc = product[x][5]
        image.category = product[x][6]
        image.tags = product[x][7]
        image.sku = product[x][8]
        image.variationdesc = product[1][11]
        image.ratio = product[x][10]
        image.chromaPrice = gs.priceChroma
        image.lerretPrice = gs.priceLerret
        image.storformatPrice = gs.priceStorformat
        image.storformatPanoPrice = gs.priceStorformatPano
        image.lerretPanoPrice = gs.priceLerretPano
        image.lerretPano_3_1Price = gs.priceLerretPano_3_1
        image.storformatPano_3_1Price = gs.priceStorformatPano_3_1

        writer.writerow(
            [image.name, '', '', '', image.description, image.imageloc, image.category, image.tags, image.sku, image.variationdesc])

        getProducts(image.ratio, image.chromaPrice.items(),
                    product[0].index('Chromaluxe'), product[1][11])

        getProducts(image.ratio, image.lerretPrice.items(),
                    product[0].index('Lerret'), product[1][12])

        getProducts(image.ratio, image.lerretPanoPrice.items(),
                    product[0].index('Lerret'), product[1][12])

        getProducts(image.ratio, image.lerretPano_3_1Price.items(),
                    product[0].index('Lerret'), product[1][12])

        getProducts(image.ratio, image.storformatPrice.items(),
                    product[0].index('FineArt fotopapir'), product[1][13])

        getProducts(image.ratio, image.storformatPanoPrice.items(),
                    product[0].index('FineArt fotopapir'), product[1][13])
        getProducts(image.ratio, image.storformatPano_3_1Price.items(),
                    product[0].index('FineArt fotopapir'), product[1][13])
