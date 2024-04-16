from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.applications import VGG16
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import numpy as np

def train_model(dataset_path, save_path):
    # Load the pre-trained VGG16 model
    base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

    # Freeze the pre-trained layers
    for layer in base_model.layers:
        layer.trainable = False

    # Add new layers for recommendation
    x = Flatten()(base_model.output)
    x = Dense(512, activation='relu')(x)
    output = Dense(5, activation='softmax')(x)  # Use 3 units for multi-class classification

    # Create the final model
    model = Model(inputs=base_model.input, outputs=output)

    # Compile the model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Prepare the dataset
    datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest',
        validation_split=0.2  # Split the data into 80% training and 20% validation
    )

    # Define the train_generator and validation_generator
    train_generator = datagen.flow_from_directory(
        dataset_path,
        target_size=(224, 224),
        batch_size=32,
        class_mode='categorical',
        classes=['Anarkali_Suit', 'Gown', 'Lehanga', 'Not_found', 'No_outfit_detected'],
        shuffle=True,
        interpolation='nearest',
        seed=42,
        subset='training'
    )

    validation_generator = datagen.flow_from_directory(
        dataset_path,
        target_size=(224, 224),
        batch_size=32,
        class_mode='categorical',
        classes=['Anarkali_Suit', 'Gown', 'Lehanga', 'Not_found', 'No_outfit_detected'],
        shuffle=False,
        interpolation='nearest',
        seed=42,
        subset='validation'
    )

    # Train the model
    history = model.fit(train_generator, epochs=20, validation_data=validation_generator)

    # Evaluate the model
    val_predictions = model.predict(validation_generator)
    val_labels = np.argmax(val_predictions, axis=1)
    true_labels = validation_generator.classes
    conf_matrix = confusion_matrix(true_labels, val_labels)
    accuracy = accuracy_score(true_labels, val_labels)
    report = classification_report(true_labels, val_labels, target_names=['Anarkali_Suit', 'Gown', 'Lehanga', 'Not_found', 'No_outfit_detected'])

    print("Confusion Matrix:\n", conf_matrix)
    print("Accuracy:", accuracy)
    print("Classification Report:\n", report)

    # Save the trained model
    model.save(save_path)

# Example usage
if __name__ == '__main__':
    dataset_path = 'C:/Users/dilna/OneDrive/Desktop/seminar/dataset/img'
    save_path = 'C:/Users/dilna/OneDrive/Desktop/seminar/dataset/model.h5'
    train_model(dataset_path, save_path)
