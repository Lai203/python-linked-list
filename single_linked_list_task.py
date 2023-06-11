class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.next = None

class TaskList:
    def __init__(self):
        self.head = None


    #Fungsi Menambah Tugas ke dalam list
    def add_task(self, description, priority):
        new_task = Task(description, priority)
        if self.head is None:
            self.head = new_task
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_task

    #Fungsi menghapus tugas dalam list
    def remove_task(self, description):
        if self.head is None:
            return

        if self.head.description == description:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current is not None:
            if current.description == description:
                prev.next = current.next
                return
            prev = current
            current = current.next

    def print_tasks(self):
        if self.head is None:
            print("Tidak ada tugas dalam list.")
            return

        current = self.head
        while current is not None:
            print(f"Deskripsi: {current.description} | Prioritas: {current.priority}")
            current = current.next

# Contoh penggunaan program
task_list = TaskList()

task_list.add_task("Mengerjakan tugas", 3)
task_list.add_task("Belanja bahan makanan", 2)
task_list.add_task("Memeriksa email", 1)

print("Daftar Tugas:")
task_list.print_tasks()

task_list.remove_task("Belanja bahan makanan")

print("\nDaftar Tugas setelah menghapus:")
task_list.print_tasks()
