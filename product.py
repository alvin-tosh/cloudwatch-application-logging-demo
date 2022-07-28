
from collections import OrderedDict
import json
import os

from utility.utility import deletefromfile, readfromfile, writetofile, logtoFile, sendlogstocloudwatch


class Product:
    def __init__(self, productid, name, description, price, stockquantity):
        self.productid = productid
        self.name = name
        self.description = description
        self.price = price
        self.stockquantity = stockquantity

    def to_ordered_dict(self):
        return OrderedDict([
            ("name", self.name),
            ("productid", self.productid),
            ("description", self.description),
            ("price", self.price),
            ("stockquantity", self.stockquantity)
        ])

    def __repr__(self):
        return str(self.__dict__)

    # def getproductbyid(self, productid):
    #     self.getproducts()
    #     return [x for x in self.products if x.productid == productid][0]

    # def getproducts(self):
    #     if os.path.exists(self.productspath):
    #         with open(self.productspath) as json_file:
    #             self.products = [x.__dict__ for x in [Product(
    #                 product['productid'],
    #                 product['name'],
    #                 product['description'],
    #                 product['price'],
    #                 product['stockquantity'],
    #             ) for product in json.load(json_file)]]
    #     if self.FileLogging:
    #         logtoFile('INFO', self.products)
    #     else:
    #         sendlogstocloudwatch('INFO', self.products,
    #                              "products were fetched")
    #     return self.products

    # def addproduct(self, description, name, price, stockquantity):
    #     data = {}
    #     products = []
    #     data["description"] = description
    #     data["name"] = name
    #     data["price"] = price
    #     data["stockquantity"] = stockquantity
    #     products = readfromfile(self.productspath, products)
    #     data["productid"] = len(products)+1
    #     writetofile(self.productspath, products, data)
    #     if self.FileLogging:
    #         logtoFile('INFO', data)
    #     else:
    #         sendlogstocloudwatch('INFO', data, "A product was added")

    # def removeproduct(self, productid):
    #     products = []
    #     products = readfromfile(self.productspath, products)
    #     deletefromfile(self.productspath, products, productid)
    #     if self.FileLogging:
    #         logtoFile('WARNING', productid)
    #     else:
    #         sendlogstocloudwatch('WARNING', productid,
    #                              " The product id %s was removed" % productid)
