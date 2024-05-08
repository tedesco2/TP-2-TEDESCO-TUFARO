import numpy as np 
from PIL import Image
import matplotlib.pyplot as plt




image = Image.open("baboon.jpg")

print(image.format)
print(image.size)
print(image.mode)

#
img = np.array(image)
print(img.shape)

plt.imshow(img)

nueva_imagen = np.pad(img, ((50, 50), (50, 50),(0,0)), mode='edge') #padding de la imagen (extiendo los bordes)
plt.imshow(nueva_imagen)
print('jjjj',nueva_imagen.shape)

def kuwahara_filter(image):
    height, width = image.shape[0], image.shape[1]
    result = np.zeros_like(image)

    for fil in range(2, height - 2):
        for col in range(2, width - 2):
            a = image[fil-2:fil+1 , col-2:col+1]
            b = image[fil-2:fil+1 , col:col+3]
            c = image[fil:fil+3 , col-2:col+1]
            d = image[fil:fil+3 , col:col+3]

            # Calcular las varianzas de los canales RGB
            variances = [np.var(a), np.var(b), np.var(c), np.var(d)]
        
            # Encontrar el cuadrante con la menor suma de varianzas
            min_variance_index = np.argmin(variances)

            # Calcular el promedio de cada canal en el cuadrante seleccionado
            selected_quadrant = [a, b, c, d][min_variance_index]
            avg_color = np.mean(selected_quadrant, (0, 1))

            result[fil, col] = avg_color

    return result

img = Image.open("baboon.jpg")
img_arr = np.array(img)
nueva_imagen = np.pad(img_arr, ((2, 2), (2, 2),(0,0)), mode='edge')

img_filtro = kuwahara_filter(nueva_imagen)
plt.imshow(img_filtro)