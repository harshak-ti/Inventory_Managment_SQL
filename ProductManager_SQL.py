from tabulate import tabulate
from Database_Handler import Database_Handler
class ProductManager(Database_Handler):

    total_num_of_products=0

    def __init__(self,file,table_name):
        super().__init__(file,table_name)

        fields = [
            "Product_SKU TEXT PRIMARY KEY",
            "Product_Name TEXT NOT NULL",
            "Brand TEXT NOT NULL",
            "Quantity INTEGER NOT NULL"
        ]
        super().create_table(fields)
        ProductManager.total_num_of_products+=super().total_number_of_products()
    
    # return the total number of products
    @classmethod
    def get_total_num_of_products(cls):
        print(f"\nTotal Number of Products: {cls.total_num_of_products}")

    # Adding a product
    def add_product(self):
        sku = input("Enter Product SKU: ")
        name = input("Enter Product Name: ")
        brand = input("Enter Brand: ")
        quantity = int(input("Enter Quantity: "))

        if quantity<0 :
            print(f"Error: Product qunatity cannot be negative")
            return
            
        super().insert_value( (sku,name,brand,quantity))
        ProductManager.total_num_of_products+=1

    def display_products(self,products):
        table = [[p[0], p[1], p[2], p[3]] for p in products]
        headers = ["Product SKU", "Product Name", "Brand", "Quantity"]
        print("\nAll Products:")
        print(tabulate(table, headers=headers, tablefmt="grid"))


    # Reading all products
    def read_products(self):
        products=super().fetch_all()
        self.display_products(products)

    # Upadate Product with SKU
    def update_product(self):
        sku = input("Enter Product SKU to update: ")
        name = input("Enter new Product Name: ")
        brand = input("Enter new Brand: ")
        quantity = int(input("Enter new Quantity: "))
        super().update_value( sku, "Product_Name", name)
        super().update_value(sku, "Brand", brand)
        super().update_value(sku, "Quantity", quantity)
        print("Product updated successfully.")
                

    #Delete a poduct with SKU
    def delete_product(self):
        sku = input("Enter Product SKU to delete: ")
        super().delete_value( sku)
        ProductManager.total_num_of_products-=1
    
    #Search the product using Product Name or Brand
    def search_product(self):
        user_input=input("Enter the Product Name or Brand to search: ")
        searched_products = super().search_products( user_input)
        self.display_products(searched_products)


    # Sort the products with SKU , Product Name and Quantity(ASC/DESC)
    def sort_products(self):
        print("\n1. Sort by Product SKU\n2. Sort by Product Name\n3. Sort by Produc Quantity (ASC)\n4. Sort by Produc Quantity (DESC)\n5. Exit")
        try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    res=super().sort_products("Product_SKU")
                elif choice == 2:
                    res=super().sort_products("Product_Name")
                elif choice == 3:
                    res=super().sort_products("Quantity")
                elif choice == 4:
                    res=super().sort_products("Quantity",False)
                elif choice == 5:
                    return
                else:
                    raise ValueError("Invalid choice")
                self.display_products(res)
                
        except ValueError as e:
                print(f"Invalid Entry: {e}")
        