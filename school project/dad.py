# Singly Linked list using Python
# Node Creation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail=None
# Insert element at the beginning
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
# Insert element after a node
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must in LinkedList.")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
# Insert element at the end
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node
# Delete an element at the top
    def deleteNode(self, position):
        temp = self.head
        if (temp is not None):
            if (temp.data == position):
                self.head = temp.next
                temp = None
                return
# Search an element
    def search(self, key):
        current = self.head
        while current is not None:
            if int(current.data) == int(key):
                return True
            current = current.next
        return False
# Sorting the elements list
    def sortLinkedList(self,head):
        current = self.head
        index = None
        if self.head is None:
            print("List is empty");
            return
        else:
            while current is not None:
                index = current.next
                while index is not None:
                    if int(current.data) > int(index.data):
                        temp=current.data
                        current.data = index.data
                        index.data=temp
                    index = index.next
                current = current.next
# Printing the elements presents in the linked list
    def printList(self):
        temp = self.head
        while (temp is not None):
            print( str(temp.data) + "-->", end="")
            temp = temp.next
        print("")
# Adding the elements to the linked list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
if __name__ == '__main__':
    llist = LinkedList()
    llist.push(7)
    llist.push(9)
    llist.push(3)
    llist.push(6)
    print("Elements presents in the Singly Linked List are: ")
    llist.printList()
    end_element=input("\nEnter the elements to be inserted at the end of the list: ")
    llist.insertAtEnd(end_element)
    llist.printList()
    beg_element=input("\nEnter the elements to be inserted at the Beginning of the list: ")
    llist.insertAtBeginning(beg_element)
    llist.printList()
    middle_element=input("\nEnter the elements to be inserted at the specified place of the list: ")
    llist.insertAfter(llist.head.next, middle_element)
    llist.printList()
    delete_element=input("\nEnter the elements to be removed from the top list: ")
    llist.deleteNode(delete_element)
    print("\nAfter deleting an element: ")
    llist.printList()
    search_element =input("\nSearch an element from the List: ")
    if llist.search(search_element):
        print("Element " + search_element + " present in the list")
    else:
        print("Element " + search_element + " is not found")
    llist.sortLinkedList(llist.head)
    print("\nSorted List: ")
    llist.printList()
    print()

    
