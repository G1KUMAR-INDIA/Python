# To generate random 6 digit otp
from random import randint
print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep="")
# Or
print(randint(000000,999999))
# To generate 10 random otps
for i in range(10):
    print(randint(000000,999999))