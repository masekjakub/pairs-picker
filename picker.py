import os
import random

def import_items(file_path) -> set:
    with open(file_path, 'r') as file:
        items = file.read().splitlines()
    return items

def pick():
    origItems = import_items('/home/masek/Projects/pairs-picker/items.txt')
    isPaired = False
    
    while not isPaired:
        pairs = []
        items = origItems.copy()
        notPicked = origItems.copy()
        for item in items:
            available = notPicked.copy()

            if item in available:
                available.remove(item)

            if len(available) == 1 and available[0] == item:
                break

            picked = random.choice(available)
            pairs.append([item, picked])
            notPicked.remove(picked)
        isPaired = True
    return pairs

if __name__ == "__main__":
    pairs = pick()
    for pair in pairs:
        print(f"{pair[0]} -> {pair[1]}")