from online_sales_analysis.product_manager import ProductManager
from online_sales_analysis.product import Product

manager = ProductManager()

manager.add_product(Product("Laptop", 3500, 5))
manager.add_product(Product("Telefon", 2000, 10))
manager.add_product(Product("Casti", 250, 15))

print("Produse în inventar:")
manager.display_products()
print(f"\n Valoarea totala a inventarului: {manager.total_inventory_value()} RON")