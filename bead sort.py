"""

        a = ("John", "Charles", "Mike")
        b = ("Jenny", "Christy", "Monica")

        list(zip(a, b)) = [('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica')]

"""
from copy import copy, deepcopy


def bead_sort(sequence):
    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)):
            if sequence[i] > sequence[j]:
                temp = sequence[i]
                sequence[i] = sequence[j]
                sequence[j] = temp
    return sequence


print(bead_sort([2, 9, 6, 5, 9, 3, 10, -1, 8, 7, -3, -5]))
