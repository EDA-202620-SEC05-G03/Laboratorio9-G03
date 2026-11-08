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

def sink(my_heap, pos):
    elements = my_heap['elements']
    n = size(my_heap)
    while 2 * pos <= n:
        child_pos = 2 * pos
        if child_pos < n:
            left = al.get_element(elements, child_pos)
            right = al.get_element(elements, child_pos + 1)
            if not priority(my_heap, left, right):
                child_pos += 1
        parent = al.get_element(elements, pos)
        child = al.get_element(elements, child_pos)
        if priority(my_heap, parent, child):
            break
        exchange(my_heap, pos, child_pos)
        pos = child_pos
        
def remove(my_heap):
    if is_empty(my_heap):
        return None
    elements = my_heap['elements']
    n = size(my_heap)
    root = al.get_element(elements, 1)
    exchange(my_heap, 1, n)
    al.remove_last(elements)
    my_heap['size'] -= 1
    if not is_empty(my_heap):
        sink(my_heap, 1)
    return pqe.get_value(root)

def get_first_priority(my_heap):
    if is_empty(my_heap):
        return None
    root = al.get_element(my_heap["elements"], 1)
    return pqe.get_value(root)


def is_present_value(my_heap, value):
    elements = my_heap["elements"]
    for pos in range(1, size(my_heap) + 1):
        entry = al.get_element(elements, pos)
        if pqe.get_value(entry) == value:
            return pos
    return -1


def contains(my_heap, value):
    return is_present_value(my_heap, value) != -1


def improve_priority(my_heap, priority, value):
    pos = is_present_value(my_heap, value)
    if pos != -1:
        entry = al.get_element(my_heap["elements"], pos)
        pqe.set_priority(entry, priority)
        swim(my_heap, pos)
    return my_heap
            