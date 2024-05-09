import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import random

bolsa =[] 
for i in range(50):
    bolsa.append(1) #1 = blanca
for i in range(50):
    bolsa.append(0) #0 = negra

print(bolsa)
while True:
    e1 = random.choice(bolsa)
    e2 = random.choice(bolsa)
    if e1 != e2:
        bolsa.pop(e1)
        bolsa.pop(e2)
        bolsa.append(1)
    elif e1==e2:
        bolsa.pop(e1)
        bolsa.pop(e2)
        bolsa.append(0)
    
    if len(bolsa) == 3:
        break

print(bolsa) #CONCLUSION: la ultima bola siempre es negra
