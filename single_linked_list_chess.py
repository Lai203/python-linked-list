class Participant:
    def __init__(self, name, ranking):
        self.name = name
        self.ranking = ranking
        self.next = None

class Tournament:
    def __init__(self):
        self.head = None

    def register_participant(self, name, ranking):
        new_participant = Participant(name, ranking)
        if self.head is None:
            self.head = new_participant
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_participant

    def eliminate_participant(self, name):
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

    def print_participants(self):
        if self.head is None:
            print("No participants in the tournament.")
            return

        current = self.head
        while current is not None:
            print(f"Name: {current.name} | Ranking: {current.ranking}")
            current = current.next

# Contoh penggunaan program
tournament = Tournament()

tournament.register_participant("Alice", 1500)
tournament.register_participant("Bob", 1700)
tournament.register_participant("Charlie", 1300)

print("Participants in the Tournament:")
tournament.print_participants()

tournament.eliminate_participant("Bob")

print("\nParticipants in the Tournament after elimination:")
tournament.print_participants()
