import importGoogleSheets as gs
import csv
gs.gsheets()
product = gs.sheets
productSizeVertical = []
productPriceVertical = []
productSizeVerticalTemp = []
productVarVertical = []
varDesc = {}

count = 0


class Products:
    pass


myList = []
# for i in range(len(gs.productVar)):
myList.append(gs.productVar)

# print(myList)

# konvertere 3:2 størrelser til 2:3
for i in range(len(gs.productSize)):
    temp = []
    for j in gs.productSize[i]:
        y = str(j).split('x')
        temp.append(f'{y[1]}x{y[0]}')
    productSizeVerticalTemp.append(temp)

# lage nye lister med kun 2:3 produkter
for i in range(len(gs.productVar)):
    if '3:2' in gs.productVar[i]:
        productSizeVertical.append(productSizeVerticalTemp[i])
        productPriceVertical.append(gs.productPrice[i])
        productVarVertical.append(gs.productVar[i])
        # print(gs.productSize[i])


# LAGE egen productVar strip
kortProductVar = []
for x in range(len(gs.productVar)):
    strippedProductVar = [x.strip() for x in gs.productVar[x].split(' ')]
    strippedProductVar.pop(1)
    kortProductVar.append(strippedProductVar[0])


# print(gs.productSize)
# print('')
# print('productSize: ' + str(gs.productPrice))
# print('')
# print(productSizeVertical)
# print('')
# print('productvar and length: ' + str(len(gs.productVar)) + str(gs.productVar))


for i in range(len(gs.productVar)):  # lager dict for lettere plassering av variationDesc
    for y in range(1, 4):
        if product[0][10 + y].lower() in gs.productVar[i].lower():
            varDesc[gs.productVar[i]] = product[1][10+y]

# print(productSizeVertical)
# print(productPriceVertical)
# print(gs.productVar)
with open('00test.csv', 'w', newline='', encoding='utf-8') as file:
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
        image.variationdesc = product[1][12]

        # writer.writerow(
        #     [image.name, '', '', '', image.description, image.imageloc, '', '', image.sku])

        for i in range(len(gs.productVar)):
            if product[x][10] in gs.productVar[i]:
                for j in range(len(gs.productPrice[i])):
                    writer.writerow(
                        [image.name,
                         str(kortProductVar[i]).capitalize(),
                         gs.productSize[i][j],
                         gs.productPrice[i][j],
                         image.description, image.imageloc,
                         image.category,
                         image.tags,
                         image.sku,
                         list(varDesc.values())[i], image.sku
                         ])

        for i in range(len(productVarVertical)):
            for j in range(len(productPriceVertical[i])):
                if '2:3' in product[x][10]:
                    writer.writerow(
                        [image.name,
                         str(kortProductVar[i]).capitalize(),
                         productSizeVertical[i][j],
                         productPriceVertical[i][j],
                         image.description, image.imageloc,
                         image.category,
                         image.tags,
                         image.sku,
                         list(varDesc.values())[i + 1], image.sku])

# print('product price: ', gs.productPrice)
# print('product var: ', gs.productVar)
# print('product var vert: ', productVarVertical)
# print('product var price: ', productPriceVertical)

# print(kortProductVar[1])
print([word[:2] for word in kortProductVar])
