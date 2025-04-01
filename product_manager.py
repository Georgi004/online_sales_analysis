from online_sales_analysis.product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        "Adauga un produs in lista de produse."
        self.products.append(product)

    def display_products(self):
        "Afiseaza toate produsele disponibile."
        for product in self.products:
            print(product.display_info())

    def total_inventory_value(self):
        "Calculeaza valoarea totala a inventarului."
        return sum(product.price * product.quantity for product in self.products)
    
    def remove_product(self, product_name):
        "Elimina un produs din lista dupa nume."
        self.products = [product for product in self.products if product.name != product_name]