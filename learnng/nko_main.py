import math
import matplotlib
import statistics
import string
import random
import hashlib
import stdin
import uuid
import base64


mdp = input("Saisir mot de passe :")
print(mdp)
mdphach = hashlib.sha256(mdp.encode("utf-8"))

print("hachage mdp : ")
print(mdphach.name)
print(mdphach.digest_size)
print(mdphach.hexdigest())


salt = uuid.uuid4().hex
mdphach_s = hashlib.sha256(mdp.encode("utf-8")+salt.encode("utf-8")).hexdigest()
print("hachage mdp_s : ")
print(mdphach_s)


