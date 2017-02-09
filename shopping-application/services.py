class Product:
    pass


class Invoice:
    pass


class ShipmentService:
    def shipProducts(self, customer, products):
        print("send request to transport provider with shipping details")
        pass


class PaymentService:
    def createPayment(self, customer, products):
        print("create invoice for customer")
        return Invoice()


class InventoryService:
    def hasStock(self, product):
        print("checks if we have the product in storage")
        return True

    def getProduct(self, productId):
        print("retrieve a product based on product id from the database")
        return Product()


class NotificationService:
    def sendNotification(self, customer, invoice):
        print("send a notification to the client based on customer "
              "preferences (email, sms)")
        pass
