class RetailItem:

    def __init__(self, itemdesc, unitsininventory, price):
        self.__itemdesc = itemdesc
        self.__unitsininventory = unitsininventory
        self.__price = price

    def set_item(self, itemdesc, unitsininventory, price):
        self.__itemdesc = itemdesc
        self.__unitsininventory = unitsininventory
        self.__price = price
        print(self.__itemdesc, self.__unitsininventory, self.__price)