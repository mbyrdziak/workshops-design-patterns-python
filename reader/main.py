from readers import CustomerCsvReader, ProductCsvReader


def main():
    customerReader = CustomerCsvReader("customer.csv")
    print(customerReader.read())

    productReader = ProductCsvReader("product.csv")
    print(productReader.read())


if __name__ == "__main__":
    main()
