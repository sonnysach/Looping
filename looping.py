name = input("What's your name?: ")

# TODO: Ask the user by name if they understand Python while loops
understand = input("{}, do you understand While loops in Python? (Yes/No): ".format(name))


# TODO: Write a while statement that checks if the user doesn't understand while loops
# TODO: Since the user doesn't understand while loops, let's explain them.
# TODO: Ask the user again, by name, if they understand while loops.
while understand.lower() == 'no':
    print("{}, While loops continue to run repeat until a certail Boolean condition is met.".format(name))
    understand = input("{}, now do you understand While loops? (Yes/No): ".format(name))
    
# TODO: Outside the while loop, congratulate the user for understanding while loops
print("That's great {}. I'm glad that you understand While loops. That was getting repetitive.".format(name))