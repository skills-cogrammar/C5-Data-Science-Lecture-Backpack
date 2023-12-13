# import math

# # Calculate permutations of 3 out of 5 items
# total_permutations = math.perm(5, 3)
# print("Total permutations:", total_permutations)

# # Calculate combinations of 3 out of 5 items
# total_combinations = math.comb(5, 3)
# print("Total combinations:", total_combinations)

# # Probability of a specific permutation
# prob_permutation = 1 / math.perm(5, 3)
# print("Probability of a specific permutation:", prob_permutation)

# # Probability of a specific combination
# prob_combination = 1 / math.comb(5, 3)
# print("Probability of a specific combination:", prob_combination)

# ------------------------------------------------------------

"""
NOTE: This code does not need to be understood, it is simply a good example and great indicator
of how much you learn over time, since you'll come back to this code and realise how simple it is
in the future.
"""

"""
Password Strength Evaluator

This script is designed to evaluate the strength of a given password based on the principles of
combinations and probabilities.
It is particularly relevant for students in both software engineering and data science fields.

Scenario:
- The script takes a password as input.
- It then considers various character sets: lowercase letters, uppercase letters, digits, and special
characters.
- For each length up to the length of the input password, the script calculates the total number of
possible combinations using these character sets.
- It evaluates the probability of guessing the password correctly on the first try, based on these
combinations.
- Finally, the script outputs an evaluation of the password strength (weak, moderate, or strong)
based on the calculated probability.

Purpose:
- For software engineering students, this script demonstrates a practical application of combinations
and probability in a software application.
- For data science students, it offers a clear example of applying statistical analysis and
probabilistic calculations in real-world scenarios.

Usage:
- Run the script and enter a password when prompted.
- The script will then evaluate and display the strength of the provided password.
"""

# # Import necessary modules
# import math
# import string
# from collections import Counter

# def calculate_combinations(total_chars, select_chars):
#     """
#     Calculate the number of ways to choose a subset of characters.

#     :param total_chars: Total number of characters in the set.
#     :param select_chars: Number of characters to select.
#     :return: Number of ways to choose the subset of characters.
#     """
#     return math.comb(total_chars, select_chars)

# def calculate_total_combinations(password, char_sets):
#     """
#     Calculate the total number of combinations for a given password.

#     :param password: The password to be evaluated.
#     :param char_sets: Dictionary of character sets with their corresponding characters.
#     :return: Total number of combinations.
#     """
#     char_count = Counter(password)
#     total_combinations = 1

#     for char_set, chars in char_sets.items():
#         set_size = len(chars)
#         count = sum(char_count[c] for c in chars)
#         if count > 0:
#             total_combinations *= calculate_combinations(set_size, count)

#     return total_combinations

# def calculate_probability(total_combinations):
#     """
#     Calculate the probability of guessing the password correctly on the first try.

#     :param total_combinations: Total number of combinations for the password length.
#     :return: Probability of correctly guessing the password.
#     """
#     # Calculate probability (inverse of total combinations)
#     return 1 / total_combinations if total_combinations > 0 else 0

# def evaluate_password_strength(password):
#     """
#     Evaluate the strength of the given password based on the probability of guessing it.

#     :param password: The password to be evaluated.
#     :return: A string indicating the password strength.
#     """
#     char_sets = {
#         'lowercase': string.ascii_lowercase,
#         'uppercase': string.ascii_uppercase,
#         'digits': string.digits,
#         'special_characters': string.punctuation
#     }

#     total_combinations = calculate_total_combinations(password, char_sets)
#     probability = calculate_probability(total_combinations)

#     if probability > 0.01:
#         return "You will be hacked, immediately! 🤕"
#     elif probability > 0.001:
#         return "Weak Password"
#     elif probability > 0.000001:
#         return "Moderate Password"
#     elif probability > 0.000000001:
#         return "Strong Password"
#     else:
#         return "Insanely Strong Password!"

# password = input("Enter your password to evaluate: ")
# strength = evaluate_password_strength(password)
# print(f"Password Strength: {strength}")

