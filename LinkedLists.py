class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next


# traverse the linked list and "reverse" the pointer in each step
# 1 -> 2 -> 3 -> 4
# 1 <- 2 -> 3 -> 4
# 1 <- 2 <- 3 -> 4
# ....etc

def reverseLinkedList(linkL):
    prev = None
    curr = linkL.head
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    linkL.head = prev



# two pointers first one moves one step and second moves two steps the second will reach the end while the first will be
# at the middle
def findmiddle(linkL):
    if not linkL.head:
        return None

    first = linkL.head
    second = linkL.head

    while second and second.next:
        first = first.next
        second = second.next.next

    return first.data if first else None


# two pointers one moves one step the other moves two steps if they meet it means the list has a loop
def findLoop(linkL):
    first = linkL.head
    second = linkL.head
    while (first and second and second.next):
        # move one step
        first = first.next
        # two steps
        second = second.next.next
        # check if they meet
        if (first == second):
            return 1
    return 0


if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.push(4)
    linked_list.push(3)
    linked_list.push(2)
    linked_list.push(1)

    print("Original Linked List:")
    linked_list.printList()
    print()

    print("Reversed Linked List:")
    reverseLinkedList(linked_list)
    linked_list.printList()
    print()

    # Restore the linked list to its original state
    reverseLinkedList(linked_list)

    middle_element = findmiddle(linked_list)
    print(f"Middle Element: {middle_element}")
    print()

    loop_present = findLoop(linked_list)
    if loop_present:
        print("The linked list has a loop.")
    else:
        print("The linked list does not have a loop.")
    print()

    #Linked List with a loop
    linked_list_with_loop = LinkedList()
    linked_list_with_loop.push(3)
    linked_list_with_loop.push(2)
    linked_list_with_loop.push(1)
    linked_list_with_loop.push(5)

    # Create a loop by connecting the last node to the second node
    linked_list_with_loop.head.next.next.next.next = linked_list_with_loop.head.next

    print("Linked List with Loop:")
    loop_present = findLoop(linked_list_with_loop)
    if loop_present:
        print("The linked list has a loop.")
    else:
        print("The linked list does not have a loop.")
    print()

