#!/usr/bin/env python3

# Author: Vanshika Dawar
# Author ID: 152288221
# Date Created: 2025/02/03
# Set the initial value of the timer
#timer = 10
# Loop until timer reaches 0
#while timer > 0:
    #print(timer)
    #timer -= 1  # Decrement the timer by 1
# Print "blast off!" after the loop ends
#print("blast off!")chmod 777

#!/usr/bin/env python3

# Author: Vanshika Dawar
# Author ID: 152288221
# Date Created: 2025/02/03

#import sys
# Check if exactly 1 argument is provided
#if len(sys.argv) != 2:
 #   print("Usage: " + sys.argv[0] + " <timer_value>")
  #  sys.exit(1)  # Exit the script with an error code
# Assign the first argument to the timer object
#timer = int(sys.argv[1])
# Loop until timer reaches 0
#while timer > 0:
 #   print(timer)
  #  timer -= 1  # Decrement the timer by 1
# Print "blast off!" after the loop ends
#print("blast off!")

#!/usr/bin/env python3

# Author: Vanshika Dawar
# Author ID: 152288221
# Date Created: 2025/02/03

import sys

# Check if an argument was provided
if len(sys.argv) == 1:
    # No argument provided, set timer to 3
    timer = 3
else:
    # Argument provided, use it as the timer value
    timer = int(sys.argv[1])

# Loop until timer reaches 0
while timer > 0:
    print(timer)
    timer -= 1  # Decrement the timer by 1

# Print "blast off!" after the loop ends
print("blast off!")