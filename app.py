from ProductManager_SQL import ProductManager
from File_Handler import File_Handler


# User Input handler function
def user_input_func(product_manager):
    while True:
        print("\n1. Add a Product\n2. Read all Products\n3. Update a Product\n4. Delete a Product\n5. Search the Product by Name or Brand\n6. Sort the Products\n7. Total Products\n8. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                product_manager.add_product()
            elif choice == 2:
                product_manager.read_products()
            elif choice == 3:
                product_manager.update_product()
            elif choice == 4:
                product_manager.delete_product()
            elif choice == 5:
                product_manager.search_product()
            elif choice == 6:
                product_manager.sort_products()
            elif choice == 7:
                product_manager.get_total_num_of_products()
            elif choice == 8:
                print("Exiting...")
                break
            else:
                raise ValueError("Invalid choice")
        except ValueError as e:
            print(f"Invalid Entry: {e}")

if __name__ == "__main__":
    file=File_Handler("Productdata.json")
    product_data = file.load_product_data()
    product_manager=ProductManager("inventory.db","products")
    user_input_func(product_manager)
