class Customer:
    def __init__(self, forename, surname, email, country):
        self.forename = forename
        self.surname = surname
        self.email = email
        self.country = country

    def __repr__(self):
        return str({
            "forename": self.forename,
            "surname": self.surname,
            "email": self.email,
            "country": self.country
        })


class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def __repr__(self):
        return str({
            "name": self.name,
            "category": self.category,
            "price": self.price,
        })
