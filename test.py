
#https://www.youtube.com/watch?v=Fdk7ZKJHFcI&list=PLgH3sgdvgO4TQagjfi1FmPcdBjIlmk5s9

import argparse
import random
import re
import time
import matplotlib.pyplot as plt
import pygad
from collections import Counter

fingers_interface = {
  'left_pinky': 0,
  'left_ring': 1,
  'left_middle': 2,
  'left_index': 3,
  'thumb': 4,
  'right_index': 5,
  'right_middle': 6,
  'right_ring': 7,
  'right_pinky': 8
}




original_keyboard = "qa<wszedxrfctgvyhbujnikmol,pö.åä-¨'"

def init_population(pop_size):
    population = []
    for i in range(pop_size):
        keyboard = random.sample(original_keyboard, len(original_keyboard))
        keyboard_str = "".join(keyboard)
        population.append(keyboard_str)
    return population

def next_generation(population, pop_size):
    new_gen = []
    total_fitness = sum(eval(layout, evaluation_text) for layout in population)

    for _ in range(int(pop_size * 0.1)):
        selected_layout = wheel_selection(population, total_fitness)
        new_gen.append(selected_layout)

    for _ in range(int(pop_size / 2)):
        parent1 = wheel_selection(population, total_fitness)
        parent2 = wheel_selection(population, total_fitness)
        child = mate(parent1, parent2)
        new_gen.append(child)

    for _ in range(int(pop_size * 0.4)):
        keyboard = random.sample(original_keyboard, len(original_keyboard))
        keyboard_str = "".join(keyboard)
        new_gen.append(keyboard_str)

    return new_gen

def mate(keyboard1, keyboard2):
    const_length = len(keyboard1)
    child = ['_' for i in range(const_length)]

    for i in range(int(const_length/2)):
        child[i] = keyboard1[i]

    for i in range(len(child)):
        if child[i] == '_':
            key = keyboard2[i]
            if key not in child:
                child[i] = key

    for i in range(len(child)):
        if child[i] == '_':
            for j in range(len(keyboard2)):
                if keyboard2[j] not in child:
                    child[i] = keyboard2[j]
                    break

    prob = random.random()
    if prob > 0.9:
        point1 = random.randint(0, const_length-1)
        point2 = random.randint(0, const_length-1)
        allele1 = child[point1]
        allele2 = child[point2]
        child[point1] = allele2
        child[point2] = allele1

    child_str = "".join(child)
    return child_str

def wheel_selection(population, total_fitness):
    spin = random.uniform(0, total_fitness)
    cumulative_fitness = 0

    for layout in population:
        cumulative_fitness += eval(layout, evaluation_text)
        if cumulative_fitness >= spin:
            return layout

    return random.choice(population)

def eval(keyboard, text):
    distance = 0

    for i in range(len(text)):
        key_index = keyboard.find(text[i])
        key = original_keyboard[key_index]

        finger = finger_hey_relation(key)

        finger_pos = fingers_interface[finger]
        distance += euclidean_key_distance(finger_pos, key)

        fingers_interface[finger] = key

    return distance

def print_keyboard(keyboard):
    for i in range(len(keyboard) - 3):
        if i % 3 == 0:
            print(keyboard[i], end='')
    print(keyboard[29])

    print(" ", end='')

    keyboard = keyboard[1:] + keyboard[0]

    for i in range(len(keyboard) - 3):
        if i % 3 == 0:
            print(keyboard[i], end='')
    print(keyboard[29])

    print("  ", end='')

    keyboard = keyboard[1:] + keyboard[0]

    for i in range(len(keyboard) - 4):
        if i % 3 == 0:
            print(keyboard[i], end='')

    print()

def euclidean_key_distance(key1, key2):
    keyboard = [
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'å'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ö', 'ä'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.']
    ]

    for row in keyboard:
        if key1 in row:
            key1_row = keyboard.index(row)
            key1_col = row.index(key1)
        if key2 in row:
            key2_row = keyboard.index(row)
            key2_col = row.index(key2)

    distance = ((key1_row - key2_row)**2 + (key1_col - key2_col)**2)**0.5

    return distance

def finger_hey_relation(key, fingers=4):
    if fingers == 4:
        relations = {
            'left_pinky': ['q', 'a', 'z'],
            'left_ring': ['w', 's', 'x'],
            'left_middle': ['e', 'd', 'c'],
            'left_index': ['r', 'f', 'v', 't', 'g', 'b'],
            'right_index': ['y', 'h', 'n', 'u', 'j', 'm'],
            'right_middle': ['i', 'k', ','],
            'right_ring': ['o', 'l', '.'],
            'right_pinky': ['p', 'å', 'ä', 'ö']
        }
    elif fingers == 3:
        relations = {
            'left_index': ['r', 'f', 'v', 't', 'g', 'b'],
            'left_middle': ['e', 'd', 'c'],
            'left_ring': ['w', 's', 'x'],
            'right_index': ['u', 'h', 'j', 'y', 'n', 'm'],
            'right_middle': ['i', 'k', 'o', 'l', 'ö', 'ä', 'å', '.', ','],
        }
    elif fingers == 1:
        relations = {
            'left_index': ['q', 'a', 'z', 'w', 's', 'x', 'e', 'd', 'c', 'r', 'f', 'v', 't', 'g', 'b'],
            'right_index': ['u', 'h', 'j', 'y', 'n', 'm', 'i', 'k', 'o', 'l', 'ö', 'ä', 'å', '.', ','],
        }

    for finger in relations:
        if key in relations[finger]:
            return fingers_interface[finger]

def main():
  # command line arguments
  parser = argparse.ArgumentParser()
  parser.add_argument("-t", "--text", help="text to be typed")
  parser.add_argument("-e", "--example", help="run a simple example", action="store_true")
  parser.add_argument("-g", "--generations", help="number of generations", type=int)
  parser.add_argument("-p", "--population", help="population size", type=int)
  args = parser.parse_args()

    Content_All = content.lower()

    print(Counter(Content_All))

    target_chars = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[{', ']}',
                    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ':;', "@'", '~#',
                    '|\\', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '<,', '.>','?']
    Keyboard_Layout_str = "qwertyuiop[]asdfghjkl;'#\\zxcvbnm,./"

    pos_value = {
        frozenset([0, 1, 2, 3, 7, 8, 9]): 1.032,
        frozenset([4, 10]): 1.247,
        frozenset([5]): 1.605,
        frozenset([11]): 2.236, 
        frozenset([12, 13, 14, 15, 18, 19, 20, 21]): 0,
        frozenset([16,17,22]): 1,
        frozenset([23]): 2,
        frozenset([24, 25, 26, 27, 29, 30, 31, 32]): 1.118,
    }

    char_to_effort = {}

    for i, char in enumerate(target_chars):
        for key, value in pos_value.items():
            if i in key:
                char_to_effort[char] = value

    for char, effort in char_to_effort.items():
        print(f"Character '{char}' has effort {effort}")

    num_generations = 100
    num_parents_mating = 5

    initial_population = [list(original_keyboard) for _ in range(pop_size)]

    ga_instance = pygad.GA(initial_population=initial_population,
                           fitness_func=fitness_func,
                           num_parents_mating=num_parents_mating,
                           num_generations=num_generations,
                           gene_space=target_chars,
                           num_genes=len(original_keyboard),
                           parent_selection_type="roulette")

    ga_instance.run()

    best_solution = ga_instance.best_solution()

    print("\nBest keyboard (PyGAD):")
    print_keyboard("".join(best_solution.gene))

    plt.plot(ga_instance.best_solutions_fitness, color="blue")
    plt.savefig(f"./images/pygad_plot.png")
    plt.show()

if __name__ == "__main__":
    main()
