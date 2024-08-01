#!/usr/bin/python3
"""
Lockboxes challenge
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Parameters
    ----------
    boxes : list of lists
        A list where each index contains a list of keys available in that box.

    Returns
    -------
    bool
        True if all boxes can be opened, else False.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]  

    while keys:
        new_key = keys.pop()
        for key in boxes[new_key]:
            if 0 <= key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)
    
    return all(unlocked)