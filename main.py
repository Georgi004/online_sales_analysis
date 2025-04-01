from online_sales_analysis.product_manager import ProductManager
from online_sales_analysis.product import Product
from cart import Cart


manager = ProductManager()
cart = Cart()

manager.add_product(Product("Laptop", 3500, 5))
manager.add_product(Product("Telefon", 2000, 10))
manager.add_product(Product("Casti", 250, 15))

cart.add_to_cart(manager.products[0], 2)
cart.add_to_cart(manager.products[1], 3)
cart.add_to_cart(manager.products[2], 1)

print("Produse în inventar:")
manager.display_products()
print(f"\n Valoarea totala a inventarului: {manager.total_inventory_value()} RON")

print("\n Eliminam produsul 'Telefon'...")
manager.remove_product("Telefon")

print("\n Produse dupa eliminare:")
manager.display_products()

cart.display_cart()
print(f"\n Valoarea totală de plata: {cart.total_cart_value()} RON")