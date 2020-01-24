#!/usr/bin/python3
# secret_word = "giraffe"
# guess = []
# guess_limit = 3
# count = 0
# out_of_guesses = False
#
#
# while guess != secret_word and not(out_of_guesses):
#     if count < guess_limit:
#         guess = input("Guess the word: ")
#         count += 1
#     else:
#         out_of_guesses = True
#
# if out_of_guesses:
#     print("You lose")
# else:
#     print("success")


def school(name, title, **projects):
    print("name :", name)
    print("Title :", title)
    print("projects :", projects)
    for key, value in projects.items():
        print(key, ':', value)


school('Alvin', 'Engineer', kilifi='interiors', machakos='webdev')
