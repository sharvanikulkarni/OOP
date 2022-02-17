import RetailItem as r
    
def main():
    itemdesc1 = "Jacket"
    unitsininventory1 = 12
    price1 = 59.95
    myretail1 = r.RetailItem(itemdesc1, unitsininventory1, price1)
    myretail1.set_item(itemdesc1, unitsininventory1, price1)

    itemdesc2 = "Designer Jeans"
    unitsininventory2 = 40
    price2 = 34.95
    myretail2 = r.RetailItem(itemdesc2, unitsininventory2, price2)
    myretail2.set_item(itemdesc2, unitsininventory2, price2)

    itemdesc3 = "Shirt"
    unitsininventory3 = 20
    price3 = 24.95
    myretail3 = r.RetailItem(itemdesc3, unitsininventory3, price3)
    myretail3.set_item(itemdesc3, unitsininventory3, price3)

main()




