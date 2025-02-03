#!/usr/bin/env python3
#print('Hi ' + name + ', you are ' + str(age) + ' years old.')
# Prompt the user for their name
#name = input("Name: ")
# Prompt the user for their age
#age = input("Age: ")
# Print the output
#print("Hi " + name + ", you are " + age + " years old.")

#!/usr/bin/env python3

import sys

# Assign command line arguments to variables
name = sys.argv[1]
age = int(sys.argv[2])  # Convert age to an integer

# Print the output
print("Hi " + name + ", you are " + str(age) + " years old.")
