from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product, quantity):
        "Adauga un produs in cos."
        if quantity <= product.quantity:
            self.cart_items.append((product, quantity))
            product.update_quantity(-quantity)
            print(f"{quantity} x {product.name} adaugat in cos!")
        else:
            print(f"Stoc insuficient pentru {product.name}!")

    def display_cart(self):
        "Afiseaza produsele din cos."""
        if not self.cart_items:
            print("Cosul este gol!")
            return
        print("Produse in cos:")
        for product, quantity in self.cart_items:
            print(f"- {quantity}x {product.name} ({product.price} RON fiecare)")

    def total_cart_value(self):
        "Calculeaza valoarea totala a cosului."
        return sum(product.price * quantity for product, quantity in self.cart_items)