# Use a Pre-trained Image Classifier to Identify Dog Breeds

This project uses pre-trained Convolutional Neural Networks (CNNs) to classify pet images, specifically dogs. It allows evaluating and comparing the performance of different models in image classification, providing detailed statistics about classification accuracy.

---

## Project Structure

### Main Files

- **check_images.py**: 
  - Main script that manages the entire classification workflow.
  - Extracts image labels from their filenames.
  - Uses pre-trained CNN models to classify the images.
  - Generates statistics about the model's performance.

- **print_results.py**: 
  - Prints the results of the classification analysis.
  - Displays key statistics such as match percentages and correct classifications.
  - Allows printing details of misclassified images (dogs and breeds).

### Folders

- **pet_images/**: Contains the provided images to be analyzed.
- **uploaded_images/**: Contains collected images to be analyzed.

---

## System Requirements

- Python 3.7 or higher.
- Required packages:
  - `numpy`
  - `argparse`
  - Other packages specified in the code.

---

## Execution

### Basic Usage

1. Place the images in the `pet_images/` folder.
2. Run the main script from the terminal:
   ```bash
   python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt
   ```
   - **`--dir`**: Directory containing the images.
   - **`--arch`**: CNN model to use (`resnet`, `alexnet`, `vgg`).
   - **`--dogfile`**: File containing the recognized dog breed names.

### Example Results

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

## Customization

If you need to adjust the format of the results or the parameters:

1. Open `print_results.py`.
2. Edit the lines that format the output statistics. For example:
   ```python
   print("The PTC Correct Dogs: {:.1f}%".format(results_stats_dic['pct_correct_dogs']))
   ```
   This will adjust the displayed percentages to one decimal place.

---

## Notes

- Ensure that the images are in a compatible format (JPG).
- Verify that file paths and names are correct.
- Check that the model specified in `--arch` is valid.

---

## Author
**Joanna Alexandra Carrión Pérez**: Bachelor of Electronic Engineering. Passionate about Data Science and Artificial Intelligence. [LinkedIn](https://www.linkedin.com/in/joanna-carrion-perez/)

## Contact
For any questions or suggestions, feel free to reach out via **joannacarrion14@gmail.com**.

## Contributions
Contributions are welcome! If you have ideas or improvements, feel free to fork the repository and submit a pull request.


