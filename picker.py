import os
import random

def import_items(file_path):
    with open(file_path, 'r') as file:
        items = file.read().splitlines()
    return items

def pick():
    origItems = import_items('/home/masek/Projects/pairs-picker/items.txt')
    isPaired = False
    while not isPaired:
        items = origItems.copy()
        notPaired = origItems.copy()
        for item in items:
            picked = random.choice(notPaired)
            while picked is item:
                if len(notPaired) == 1:
                    isPaired = False
                    break
                picked = random.choice(notPaired)
            print(f"{item} -> {picked}")
            notPaired.remove(picked)
            isPaired = True

if __name__ == "__main__":
    pick()