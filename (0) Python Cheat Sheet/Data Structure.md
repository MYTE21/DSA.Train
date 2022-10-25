# Data Structures

## List Methods

List is `mutable`, means - it can be changed.

Take a look at the empty list named, `my_list = []`.


| Method  | Usage                                | Functionality                                                                                              |
|---------|--------------------------------------|------------------------------------------------------------------------------------------------------------|
| append  | `my_list.append("Bangladesh")`       | Append an item to the end of the list.                                                                     |
| sort    | `my_list.sort()`                     | Sort the list.                                                                                             |
| reverse | `my_list.reverse()`                  | Reverse the list.                                                                                          |
| insert  | `my_list.insert(0, "mango")`         | Insert an item to the list at the specified index.                                                         |
| remove  | `my_list.remove("banana")`           | Remove the**first matching element** from the list with the specified value.                               |
| pop     | `my_list.pop()`<br/>`my_list.pop(2)` | Remove and return the last value from the list.<br/>Remove and return the given index value from the list. |
| extend  | `my_list.extend(list_two)`           | Add the **specified list elements (or any iterable)** to the end of the current list.                      |
| count   | `my_list.count(3)`                   | **Total count** of a given element in a list.                                                              |
| del     | `del(my_list)`<br/>`del(my_list[1])` | Delete entire list.<br/>Delete the item from the list at the specified index.                              |