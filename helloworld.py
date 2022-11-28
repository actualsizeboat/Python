import random
import time

## print('Type something alphanumeric and hit enter!')
## target_string = input()

target_string = 'Hello world!'
letter_index = 0
attempts = 0
curr_char = ''

start=time.time()

while letter_index <= len(target_string)-1:
    next_char = random.choice('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890!@#$%^&* ()')
    print(curr_char + next_char)
    attempts = attempts + 1
    time.sleep(.01)
    if target_string[letter_index] == next_char:
        curr_char = curr_char + next_char
        letter_index = letter_index + 1
print('Completed in ' + str(attempts) + ' iterations, totaling ' + str(round(time.time() - start, 5)) + ' seconds')