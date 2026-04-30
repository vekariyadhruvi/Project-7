import random
import string

# Random number
def random_number():
    return random.randint(1, 100)

# Random list
def random_list():
    return random.sample(range(1, 50), 5)

# Generate password
def generate_password(length=8):
    chars=string.ascii_letters + string.digits + "@#*$^"
    return "".join(random.choice(chars) for i in range(length))

# Random sampling from dataset
def random_sample(data):
    return random.sample(data, min(3, len(data)))

# Generate OTP
def generate_otp():
    return random.randint(100000, 999999)

# Simple game (dice)
def dice_game():
    return random.randint(1, 6)