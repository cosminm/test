def dict_to_flat_list(dictionary_itervalues):
    if dictionary_itervalues is None:
        return []
    result = []
    for elem in dictionary_itervalues:
        if hasattr(elem, "__iter__") and not isinstance(elem, basestring):
            result.extend(dict_to_flat_list(elem.itervalues()))
        else:
            if type(elem) is int:
                result.append(elem)
    return result


def remove_duplicates(list_items):
    if list_items is None:
        return []
    return list(set(list_items))


def dict_to_list(dictionary):
    if dictionary is None:
        return []
    list_result = dict_to_flat_list(dictionary.itervalues())
    return remove_duplicates(list_result)

