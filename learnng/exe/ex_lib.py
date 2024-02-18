import math
import statistics
import string
import random
### utiliser une libraire standard (math)
#factoriel
print(math.factorial(9))
### développer par nous même
##nb = (int)(input("Factoriel de ? "))
##facto = 1
##for i in range(1,(nb+1)):
##    facto=facto*i
##print(facto)

# des ex.
print(statistics.mean([1, 3, 5, 7, 9, 11, 13]))
print(string.ascii_letters)
print(string.digits)
for i in range(3):  # une boucle pour justif. random
    print(random.random())

###https://www.w3schools.com/python/module_math.asp
###https://www.w3schools.com/python/module_statistics.asp
###https://www.w3schools.com/python/module_random.asp
###https://docs.python.org/3/library/string.html
###https://docs.python.org/3/library/random.html

import hashlib
m = hashlib.md5(b"mon mdp")
print(m.hexdigest()) # hex representation
m = hashlib.md5(b"abc def jkl bonjour")
print(m.hexdigest()) # hex representation
#exo d'application
###https://docs.python.org/fr/3/library/hashlib.html
###https://mkyong.com/python/python-md5-hashing-example/
###https://www.geeksforgeeks.org/md5-hash-python/
