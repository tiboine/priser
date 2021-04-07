import importGoogleSheets as gs
import csv
gs.gsheets()
product = gs.sheets
productSizeVertical = []
productPriceVertical = []
productSizeVerticalTemp = []
productVarVertical = []
varDesc = {}
produktVarianter = 0  # for å sjekke antall totale produkter

# konvertere 3:2 størrelser til 2:3
for num in range(len(gs.productSize)):
    temp = []
    for size in gs.productSize[num]:
        splitSize = str(size).split('x')
        temp.append(f'{splitSize[1]}x{splitSize[0]}')
    productSizeVerticalTemp.append(temp)


kortProductVar_2_3 = []
kortProductVar = []
for num in range(len(gs.productVar)):
    strippedProductVar = [num.strip() for num in gs.productVar[num].split(' ')]
    strippedProductVar.pop(1)
    kortProductVar.append(strippedProductVar[0])
    # lage nye lister med kun 2:3 produkter
    if '3:2' in gs.productVar[num]:
        productSizeVertical.append(productSizeVerticalTemp[num])
        productPriceVertical.append(gs.productPrice[num])
        productVarVertical.append(gs.productVar[num])
        kortProductVar_2_3.append([x.strip()
                                   for x in gs.productVar[num].split(' ')][0])  # strippe 2:3 fra typen


# lager dict for lettere plassering av variationDesc
for num in range(len(gs.productVar)):
    for y in range(1, 4):
        if product[0][11 + y].lower() in gs.productVar[num].lower():
            varDesc[gs.productVar[num]] = product[1][11+y]


with open(str(gs.RANGE_NAME[:-7])+'.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(product[0])  # headers

    class Products:
        pass

    for num in range(1, len(product)):
        image = Products()
        image.name = product[num][0]
        image.description = product[num][4]
        image.imageloc = product[num][5]
        image.category = product[num][6]
        image.tags = product[num][7]
        image.sku = product[num][8]
        image.variationdesc = product[1][13]

        # writer.writerow(
        #     [image.name, '', '', '', image.description, image.imageloc, '', '', image.sku, '', ''])

        for i in range(len(gs.productVar)):

            for j in range(len(gs.productPrice[i])):
                if product[num][11] in gs.productVar[i]:
                    produktVarianter += 1

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
                if '2:3' in product[num][11]:
                    produktVarianter += 1
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

print('Antall produkter:', len(product))
print('Antall varianter totalt:', produktVarianter)
