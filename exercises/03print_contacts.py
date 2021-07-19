# Write a function called `print_contacts` that takes a
# dictionary of key-value pairs for names and phone numbers,
# then outputs the `name` with the contact info.
#
# Try iterating over a dictionary with a for loop and printing
# out what values come back.
#
# Example function call:
#
# print_contacts(contacts)
#
# > Brian has a phone number of 333-333-3333
# > Lenny has a phone number of 444-444-4444
# > Daniel has a phone number of 777-777-7777
#
# Use the contacts below

contacts = {
    'Brian': '333-333-3333',
    'Lenny': '444-444-4444',
    'Daniel': '777-777-7777'
}

# def print_contacts(dict):
#     for i in dict:
#         # .format() old method
#         print("{} has a phone number of {}".format(i, dict[i]))
#         # formatted string literals
#         print(f"{i} has a phone number of {dict[i]}")

# def print_contacts(dict):
#     for name, number in dict.items():
#         print(f"{name} has a number of {number}")

# print_contacts(contacts)

print(contacts.items())
