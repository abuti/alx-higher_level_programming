#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_score = int()
    for k, v in a_dictionary.items():
        if max_score < v:
            max_score = v
            name = k
    return name
