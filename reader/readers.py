import csv
import sys

from model import Customer, Product


class CustomerCsvReader:
    def __init__(self, customersFile):
        self.customersFile = customersFile

    def read(self):
        customers = []
        with open(self.customersFile, 'r') as f:
            reader = csv.reader(f)
            try:
                for customerRow in reader:
                    customers.append(Customer(
                        forename=customerRow[0],
                        surname=customerRow[1],
                        email=customerRow[2],
                        country=customerRow[3]
                    ))
            except csv.Error as e:
                sys.exit(
                    'file %s, line %d: %s' % (
                        self.customersFile, reader.line_num, e))
        return customers


class ProductCsvReader:
    def __init__(self, productsFile):
        self.productsFile = productsFile

    def read(self):
        products = []
        with open(self.productsFile, 'r') as f:
            reader = csv.reader(f)
            try:
                for productRow in reader:
                    products.append(Product(
                        name=productRow[0],
                        category=productRow[1],
                        price=productRow[2],
                    ))
            except csv.Error as e:
                sys.exit(
                    'file %s, line %d: %s' % (
                        self.productsFile, reader.line_num, e))
        return products
