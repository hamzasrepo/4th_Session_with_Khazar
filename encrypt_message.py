import string

# TODO-1: Create a function called 'encrypt()' that takes 
# 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter 
# of the 'original_text' forwards in the alphabet 
# by the shift amount and print the encrypted text.

# TODO-3: Call the 'encrypt()' function and pass in 
# the user inputs. You should be able to test the code 
# and encrypt a message.

# TODO-4: What happens if you try to shift z forwards by 9? 
# Can you fix the code?

alphabets = list(string.ascii_lowercase)

def encrypt(original_text, shift_amount):
    output_text = ""

    print(f"Here is the encoded result: {output_text}")

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

print(encrypt(text, shift))