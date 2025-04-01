class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        "Afiseaza informatiile despre produs."
        return f"Produs: {self.name}, Pret: {self.price} RON, Cantitate: {self.quantity}"

    def update_quantity(self, amount):
        "Actualizeaza cantitatea produsului."
        self.quantity += amount