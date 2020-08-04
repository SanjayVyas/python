'''
----------------------------------------------------------------------
File:      SingleLinkedList.py
Project:   SingleLinkedList
Author:    Sanjay Vyas

Description:
  Single Linked List implementation is python
----------------------------------------------------------------------
Revision History:
2020-Aug-05	[SV]: Created
----------------------------------------------------------------------
'''

from typing import Any

class node:
  def __init__(self, value: Any):
    self.prev = None
    self.value = value
    self.next = None

class linked_list:
  def __init__(self, *args):
    
    # Define head and tail to hold the list
    self.head = None
    self.tail = None

    # Initially add all the values to the end of the list
    for value in args:
      self.push_back(value)

  def push_back(self, value: Any):
    '''
    push a new value to the end of the linked list
    '''

    # Create a new node and add it beyond tail
    new_node = node(value)
    
    # If it's the first time, make it head and tail
    if self.head is None:
      self.head = new_node
    else:
      # Subsequent times, add it beyond the tail
      self.tail.next = new_node

    self.tail = new_node

    # fluent interface
    return self

  def print(self):
    current = self.head
    while current is not None:
      print(current.value)
      current=current.next

# If we are not running as a module, run the test code
if __name__ == "__main__":

  # Create a list with few initial values
  print("Initial list")
  my_list = linked_list(1, 2, 3)
  my_list.print()

  # test the push_back function
  print("After push_back(4)")
  my_list.push_back(4)
  my_list.print()