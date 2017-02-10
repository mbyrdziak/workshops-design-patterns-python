class Order:
    def __init__(self, customer, orderDate, orderItems):
        self.customer = customer
        self.orderDate = orderDate
        self.orderItems = orderItems

    def calculatePrice(self):
        itemsPrice = 0
        for item in self.orderItems:
            itemsPrice += item.getPrice()

        return itemsPrice + self.percentage(23, itemsPrice)

    def percentage(self, percent, whole):
        return (percent * whole) / 100.0


class Customer:
    def __init__(self, name, email, country):
        self.name = name
        self.email = email
        self.country = country


class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def getPrice(self):
        return self.product.price * self.quantity


class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price
