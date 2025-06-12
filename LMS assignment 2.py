class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None  

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node  
        else:
            current = self.head
            while current.next:  
                current = current.next
            current.next = new_node  

    def print_list(self):
        if not self.head:
            print("List is empty.")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        try:
            if not self.head:
                raise IndexError("Cannot delete from an empty list.")

            if n <= 0:
                raise ValueError("Index must be a positive integer (1-based).")

            if n == 1:
                self.head = self.head.next
                print(f"Deleted node at position {n}.")
                return

            current = self.head
            count = 1

            while current and count < n - 1:
                current = current.next
                count += 1

            if not current or not current.next:
                raise IndexError("Index out of range.")

            deleted_data = current.next.data
            current.next = current.next.next
            print(f"Deleted node at position {n} with data '{deleted_data}'.")

        except (IndexError, ValueError) as e:
            print("Error:", e)

ll = LinkedList()

ll.add_node(10)
ll.add_node(20)
ll.add_node(30)
ll.add_node(40)

print("Original List:")
ll.print_list()

ll.delete_nth_node(2)

print("\nList after deleting 2nd node:")
ll.print_list()

ll.delete_nth_node(10)

empty_ll = LinkedList()
empty_ll.delete_nth_node(1)