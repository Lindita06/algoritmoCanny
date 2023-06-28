El algoritmo Canny es un algoritmo de procesamiento de imágenes que se utiliza para detectar bordes en imágenes. Fue desarrollado por John F. Canny en 1986 y es uno de los algoritmos más utilizados para la detección de bordes en imágenes.

El algoritmo Canny consta de varios pasos:

1. Suavizado de la imagen: se aplica un filtro gaussiano para suavizar la imagen y reducir el ruido.

2. Cálculo del gradiente de la imagen: se calcula el gradiente de la imagen para determinar la dirección y la magnitud del cambio de intensidad en cada píxel.

3. Supresión de no máximos: se elimina cualquier píxel que no sea un máximo local en la dirección del gradiente.

4. Umbralización: se aplican dos umbrales para determinar qué píxeles se consideran bordes y cuáles no. Los píxeles con una magnitud de gradiente por encima del umbral superior se consideran bordes, mientras que los píxeles con una magnitud de gradiente por debajo del umbral inferior se consideran no bordes. Los píxeles con una magnitud de gradiente entre los dos umbrales se consideran bordes si están conectados a píxeles por encima del umbral superior.

La combinación de estos pasos permite detectar bordes precisos y reducir el ruido y las falsas detecciones de bordes en la imagen.

Articulo:
https://repositorioacademico.upc.edu.pe/bitstream/handle/10757/655225/LopezP_J.pdf?sequence=3&isAllowed=y

Resumen:
 El proyecto propone un modelo tecnológico para optimizar el proceso 
de detección de leucemia mediante la microscopía digital. Este modelo utiliza el algoritmo 
de Canny, y un banco de imágenes de Glóbulos Blancos y Rojos, para la identificación de 
células microscópicas, que finalmente serán analizadas por un especialista en salud para 
brindar el diagnóstico final. El modelo propuesto incluye la captura, digitalización y análisis 
de muestras microscópicas, y está compuesto por las siguientes 5 fases: 1. Recolección de 
datos; 2. Captura de datos; 3. Procesamiento de imágenes; 4. Clasificación celular; 5. 
Visualización de resultados.

Referencias:
[1] Mariella Sausa. “En el Perú cada año mueren 350 niños a consecuencia del cáncer 
[INFORME]” Perú 21 [En línea] Disponible: https://peru21.pe/peru/cifras-cancer-peru-anomueren-350-ninos-consecuencia-enfermedad-395940
[2] Biblioteca Nacional de Medicina de los EEUU, MedlinePlus, “Leucemia”, Disponible: 
https://medlineplus.gov/spanish/ency/article/001299.htm
[3] Biblioteca Nacional de Medicina de los EEUU, MedlinePlus, “Leucemia linfocítica 
aguda”, Disponible: https://medlineplus.gov/spanish/ency/article/000541.htm
[4] Biblioteca Nacional de Medicina de los EEUU, MedlinePlus, “Leucemia mielógena 
aguda”, Disponible: https://medlineplus.gov/spanish/ency/article/000542.htm
[5] Biblioteca Nacional de Medicina de los EEUU, MedlinePlus, “Leucemia linfocítica
crónica”, Disponible: https://medlineplus.gov/spanish/ency/article/000532.htm
[6] Biblioteca Nacional de Medicina de los EEUU, MedlinePlus, “Leucemia miélogena 
crónica”, Disponible: https://medlineplus.gov/spanish/ency/article/000570.htm 
[7] CCM Salud, “Hematología y definición”, Disponible: https://salud.ccm.net/faq/9089-
hematologia-definicion

