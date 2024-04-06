from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
import numpy as np
import os

def extract_features(image_path, model):
    # Convert URL path to file system path if needed
    if image_path.startswith('/'):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        image_path = os.path.join(base_dir, image_path.strip("/"))

    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Extract features and predict
    features = model.predict(img_array)
    predicted_probabilities = features[0]

    # Debugging: Print extracted features
    print("Extracted Features:", features)

    # Debugging: Print probabilities
    print("Predicted probabilities:", predicted_probabilities)

    predicted_category = np.argmax(predicted_probabilities)

    # Debugging: Print predicted category
    print("Predicted category index:", predicted_category)

    return features, predicted_category

# Example usage
# if __name__ == '__main__':
#     image_path = 'C:/Users/dilna/OneDrive/Pictures/Saved Pictures/onam/DSC09906.jpg'
#     features = extract_features(image_path)
#     print(features)

