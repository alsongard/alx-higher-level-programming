#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    symmetric_difference:
    We use the built-in symmetric_difference method of sets.
    This method returns a new set containing elements that are
    in either set_1 or set_2, but not in both.
    """
    return set_1.symmetric_difference(set_2)
