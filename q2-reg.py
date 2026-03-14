import random
import string
import re

def generate_password():

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = "!@#$%&*"

    all_chars = uppercase + lowercase + digits + special

    while True:

        password = ''.join(random.sample(all_chars, 16))

        pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=(?:.*\d){2,})(?=.*[!@#$%&*]).{16}$'

        if re.match(pattern, password):
            return password


print("Generated Password:", generate_password())