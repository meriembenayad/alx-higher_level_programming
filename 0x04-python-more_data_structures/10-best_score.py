#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None

    high_score = max(a_dictionary.values())
    if a_dictionary:
        for key, value in a_dictionary.items():
            if value is high_score:
                return key
