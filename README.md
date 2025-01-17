# Use a Pre-trained Image Classifier to Identify Dog Breeds

Este proyecto utiliza redes neuronales convolucionales (CNN) preentrenadas para clasificar imágenes de mascotas, específicamente perros. Permite evaluar y comparar el rendimiento de diferentes modelos en la clasificación de imágenes, proporcionando estadísticas detalladas sobre la precisión de las clasificaciones.

---

## Estructura del Proyecto

### Archivos Principales

- **check_images.py**: 
  - Script principal que gestiona el flujo completo de la clasificación.
  - Extrae etiquetas de las imágenes a partir de sus nombres de archivo.
  - Utiliza modelos CNN preentrenados para clasificar las imágenes.
  - Genera estadísticas sobre el rendimiento del modelo.

- **print_results.py**: 
  - Imprime los resultados del análisis de clasificación.
  - Muestra estadísticas clave como porcentajes de coincidencias y clasificaciones correctas.
  - Permite imprimir detalles de imágenes mal clasificadas (perros y razas).

### Carpetas

- **pet_images/**: Contiene las imágenes brindadas que serán analizadas.
- **uploaded_images/**: Contiene mis imágenes recolectadas que serán analizadas.

---

## Requisitos del Sistema

- Python 3.7 o superior.
- Paquetes necesarios:
  - `numpy`
  - `argparse`
  - Otros paquetes especificados en el código.

Instala las dependencias ejecutando:
```bash
pip install -r requirements.txt
```

---

## Ejecución

### Uso Básico

1. Coloca las imágenes en la carpeta `images/`.
2. Ejecuta el script principal desde la terminal:
   ```bash
   python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt
   ```
   - **`--dir`**: Directorio con las imágenes.
   - **`--arch`**: Modelo CNN a utilizar (`resnet`, `alexnet`, `vgg`).
   - **`--dogfile`**: Archivo con los nombres de las razas reconocidas.

### Ejemplo de Resultados

```
Model that you want to use: resnet
The Number of Images: 40 
The Number of Dog Images: 30 
The Number of Not-a Dog Images: 10
The PTC Match: 75.0
The PTC Correct Dogs: 100.0
The PTC Correct Breed: 80.0
The PTC Correct NotDogs: 100.0
```

---

## Personalización

Si necesitas ajustar el formato de los resultados o los parámetros:

1. Abre `print_results.py`.
2. Edita las líneas que formatean las salidas de las estadísticas. Por ejemplo:
   ```python
   print("The PTC Correct Dogs: {:.1f}%".format(results_stats_dic['pct_correct_dogs']))
   ```
   Esto ajustará los porcentajes mostrados a un solo decimal.

---

## Notas

- Asegúrate de que las imágenes estén en un formato compatible (JPG).
- Verifica que las rutas y nombres de los archivos sean correctos.
- Revisa que el modelo especificado en `--arch` sea válido.

---

## Autor
**Joanna Alexandra Carrión Pérez**: Bachiller de Ingeniería Electrónica. Apasionada por la Ciencia de Datos y la Inteligencia Artificial. [LinkedIn](https://www.linkedin.com/in/joanna-carrion-perez/)

## Contacto
Para cualquier duda o sugerencia, contáctame a través de **joannacarrion14@gmail.com**.

## Contribuciones
¡Contribuciones son bienvenidas! Si tienes ideas o mejoras, no dudes en hacer un fork del repositorio y enviar un pull request. 

