from DataStructures.List import array_list as al
from DataStructures.Priority_queue import pq_entry as pqe


def default_compare_higher_value(father_node, child_node):
    if pqe.get_priority(father_node) >= pqe.get_priority(child_node):
        return True
    return False


def default_compare_lower_value(father_node, child_node):
    if pqe.get_priority(father_node) <= pqe.get_priority(child_node):
        return True
    return False


def new_heap(is_min_pq=True):
    if is_min_pq:
        cmp_function = default_compare_lower_value
    else:
        cmp_function = default_compare_higher_value

    heap = {
        "elements": al.new_list(),
        "size": 0,
        "cmp_function": cmp_function,
    }
    al.add_last(heap["elements"], None)
    return heap


def priority(my_heap, parent, child):
    return my_heap["cmp_function"](parent, child)


def exchange(my_heap, i, j):
    elements = my_heap["elements"]
    elem_i = al.get_element(elements, i)
    elem_j = al.get_element(elements, j)
    al.change_info(elements, i, elem_j)
    al.change_info(elements, j, elem_i)


def size(my_heap):
    return my_heap["size"]


def is_empty(my_heap):
    return size(my_heap) == 0


def swim(my_heap, pos):
    elements = my_heap["elements"]
    while pos > 1:
        parent_pos = pos // 2
        parent = al.get_element(elements, parent_pos)
        child = al.get_element(elements, pos)
        if priority(my_heap, parent, child):
            break
        exchange(my_heap, parent_pos, pos)
        pos = parent_pos


def insert(my_heap, priority, value):
    entry = pqe.new_pq_entry(priority, value)
    al.add_last(my_heap["elements"], entry)
    my_heap["size"] += 1
    swim(my_heap, my_heap["size"])
    return my_heap