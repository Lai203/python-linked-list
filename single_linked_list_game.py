class Item:
    def __init__(self, name, importance):
        self.name = name
        self.importance = importance
        self.next = None

class Backpack:
    def __init__(self):
        self.head = None

    def add_item(self, name, importance):
        new_item = Item(name, importance)
        if self.head is None:
            self.head = new_item
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_item

    def remove_item(self, name):
        if self.head is None:
            return

        if self.head.name == name:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current is not None:
            if current.name == name:
                prev.next = current.next
                return
            prev = current
            current = current.next

    def print_items(self):
        if self.head is None:
            print("No items in the backpack.")
            return

        current = self.head
        while current is not None:
            print(f"Name: {current.name} | Importance: {current.importance}")
            current = current.next

# Contoh penggunaan program
backpack = Backpack()

backpack.add_item("Health Potion", 5)
backpack.add_item("Sword", 10)
backpack.add_item("Shield", 8)

print("Items in the Backpack:")
backpack.print_items()

backpack.remove_item("Sword")

print("\nItems in the Backpack after removal:")
backpack.print_items()
