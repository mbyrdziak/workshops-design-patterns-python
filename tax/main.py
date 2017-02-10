from datetime import datetime

from taxes import *


def main():
    order = Order(
        customer=Customer("John Doe", "john@email.com", "GB"),
        orderDate=datetime(2016, 1, 1),
        orderItems=[
            OrderItem(Product("TV", "Electronics", 1000), 1),
            OrderItem(Product("Design Patterns", "Books", 25), 1),
            OrderItem(Product("Dress", "Cloths", 75), 2)
        ]
    )
    print(order.calculatePrice())

if __name__ == "__main__":
    main()
