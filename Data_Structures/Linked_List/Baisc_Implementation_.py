#Very Baisc Linked List Implementation


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
        
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node

my_node = Node(44)


class LinkedList:
    def __init__(self,value=None):
        self.head_node = Node(value)
        
    def get_head_node(self):
        return self.head_node
    
    def insert_beginning(self,new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
        
    def stringify_list(self):
        string_list = ""
        current_node = self.head_node
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list
    
    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node() #switches it to the next value
        else:
            next_node = current_node.get_next_node()
            if next_node.get_value() == value_to_remove:
                current_node.set_next_node(next_node.get_next_node()) #sets next node's value to the preceeding node
                current_node = None #set to None to exit the loop
            else:
                current_node = next_node
    
# #test
ll = LinkedList(5)
ll.insert_beginning(74)
ll.insert_beginning(2568)
ll.remove_node(5)
print(ll.stringify_list())


