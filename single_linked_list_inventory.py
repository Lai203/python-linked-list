class Product:
    def __init__(self, name, code, stock):
        self.name = name
        self.code = code
        self.stock = stock
        self.next = None

class Inventory:
    def __init__(self):
        self.head = None

    def add_product(self, name, code, stock):
        new_product = Product(name, code, stock)
        if self.head is None:
            self.head = new_product
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_product

    def remove_product(self, code):
        if self.head is None:
            return

        if self.head.code == code:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current is not None:
            if current.code == code:
                prev.next = current.next
                return
            prev = current
            current = current.next

    def print_inventory(self):
        if self.head is None:
            print("Inventory is empty.")
            return

        current = self.head
        while current is not None:
            print(f"Product: {current.name} | Code: {current.code} | Stock: {current.stock}")
            current = current.next

# Contoh penggunaan program
inventory = Inventory()

inventory.add_product("Laptop", "LP001", 10)
inventory.add_product("Smartphone", "SP001", 15)
inventory.add_product("Keyboard", "KB001", 5)

print("Inventory List:")
inventory.print_inventory()

inventory.remove_product("SP001")

print("\nInventory List after removal:")
inventory.print_inventory()
