#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""

message = 'P.S. '

# wrap connection in a float() to accept decimals as numbers
numscore = float(input("What is your numeric score between 1 to 100?"))


#if numscore > 100:
   # message = message + 'Please enter a numeric score less than 100.'
#if numscore <= 100:
   # message = message + 'Your letter grade associatd with this number is A.'

# if input value was higher or equal to 90
if numscore >= 90:
    message = message + 'Your letter grade associated with this number is A.'
elif numscore >= 80:
    message = message + 'Your letter grade associated with this number is B.'
elif numscore >= 70:
    message = message + 'Your letter grade associated with this number is C.'
elif numscore >= 60:
    message = message + 'Your letter grade associated with this number is D.'
elif numscore >= 50:
    message = message + 'Your letter grade associated with this number is E.'
elif numscore <= 49:
    message = message + 'Your letter grade associated with this number is F.'
else:
    message = message + 'Please enter a valid numeric score between 1 to 100.'
print(message)
