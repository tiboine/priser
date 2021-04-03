import importGoogleSheets as gs
import csv
import collections
gs.gsheets()
product = gs.sheets
productSizeVertical = []
productPriceVertical = []
productSizeVerticalTemp = []
productVarVertical = []
varDesc = {}


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
        image.description = product[x][4]
        image.imageloc = product[x][5]
        image.category = product[x][6]
        image.tags = product[x][7]
        image.sku = product[x][8]
        image.variationdesc = product[1][13]

        # writer.writerow(
        #     [image.name, '', '', '', image.description, image.imageloc, '', '', image.sku, '', ''])

        for i in range(len(gs.productVar)):
            if product[x][11] in gs.productVar[i]:
                for j in range(len(gs.productPrice[i])):
                    writer.writerow(
                        [image.name,
                         str(kortProductVar[i]).capitalize(),
                         gs.productSize[i][j],
                         gs.productPrice[i][j],
                         image.description, image.imageloc,
                         image.category,
                         image.tags,
                         image.sku + '-' +
                         str(kortProductVar[i])[:2] +
                            str(gs.productSize[i][j][:2]),
                         image.sku,
                         list(varDesc.values())[i]
                         ])

        for i in range(len(productVarVertical)):
            for j in range(len(productPriceVertical[i])):
                if '2:3' in product[x][11]:
                    writer.writerow(
                        [image.name,
                         str(kortProductVar_2_3[i]).capitalize(),
                         productSizeVertical[i][j],
                         productPriceVertical[i][j],
                         image.description, image.imageloc,
                         image.category,
                         image.tags,
                         image.sku + '-' +
                         str(kortProductVar_2_3[i])[:2] +
                            str(productSizeVertical[i][j][:2]),
                         image.sku,
                         list(varDesc.values())[i + 1]])

print('Antall produkter:')
print(len(product))
