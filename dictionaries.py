# dictionary exercises

######
# Define a dictionary that contains information about several members of your family.
# Use the following example as a template.

my_family = {'sister': {'name': 'Krista', 'age': 42 },
    'mother': {
        'name': 'Cathie',
        'age': 70
    }
}

# Using a dictionary comprehension, produce output that looks like the following example.

# Krista is my sister and is 42 years old
# Helpful hint: To convert an integer into a string in Python, it's str(integer_value)

for (relationship, info) in my_family.items():
  print('{} is my {} and is {} years old'.format(info['name'], relationship, info['age']))


######
# Make a function named word_count. It should accept a single argument which will be a string.
# The function needs to return a dictionary.
# The keys in the dictionary will be each of the words in the string, lowercased.
# The values will be how many times that particular word appears in the string.

# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# Lowercase the string to make it easier.

def word_count(string):
    new_dict = {}
    new_list = string.lower().split()
    for x in new_list:
        new_dict.update({x: new_list.count(x)})
    return new_dict

print(word_count("hello whitney hello whitney"))











