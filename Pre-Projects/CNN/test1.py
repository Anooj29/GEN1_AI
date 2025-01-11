import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.callbacks import ReduceLROnPlateau, EarlyStopping, ModelCheckpoint

image_size = (224, 224, 3)
plant_type_output = 10
disease_type_output = 55

data_dir = r'C:\Project\Dataset\pythonProject'  # Annoj tuzaya file chi location taak

x_batch = np.load(os.path.join(data_dir, 'x_batch.npy'))
y_batch = np.load(os.path.join(data_dir, 'y_batch.npy'), allow_pickle=True)

plant_type_labels = y_batch.item()['plant_type']
disease_type_labels = y_batch.item()['disease_type']



def create_resnet50_multitask_model():
    input_layer = layers.Input(shape=image_size)

    base_model = ResNet50(weights='imagenet', include_top=False, input_shape=image_size)
    base_model.trainable = True

    x = base_model(input_layer)
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dropout(0.5)(x)

    shared_features = layers.Dense(512, activation='relu')(x)
    shared_features = layers.BatchNormalization()(shared_features)

    plant_type_features = layers.Dense(256, activation='relu')(shared_features)
    plant_type_output_layer = layers.Dense(plant_type_output, activation='softmax', name='plant_type')(plant_type_features)

    disease_type_features = layers.Dense(256, activation='relu')(shared_features)
    disease_type_output_layer = layers.Dense(disease_type_output, activation='sigmoid', name='disease_type')(disease_type_features)

    model = models.Model(inputs=input_layer, outputs=[plant_type_output_layer, disease_type_output_layer])
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
        loss={
            'plant_type': 'categorical_crossentropy',
            'disease_type': 'binary_crossentropy'
        },
        metrics={
            'plant_type': ['accuracy'],
            'disease_type': ['accuracy']
        }
    )
    return model

model = create_resnet50_multitask_model()

model.summary()

callbacks = [
    ReduceLROnPlateau(monitor='loss', factor=0.2, patience=3, min_lr=1e-6, verbose=1),
    EarlyStopping(monitor='loss', patience=5, restore_best_weights=True, verbose=1),
    ModelCheckpoint('./best_model.keras', monitor='loss', save_best_only=True, verbose=1)
]

history = model.fit(
    x_batch,
    {'plant_type': plant_type_labels, 'disease_type': disease_type_labels},
    epochs=5,
    batch_size=32,
    callbacks=callbacks
)

model_save_path = './resnet50_multitask_model.keras'
model.save(model_save_path)
print(f"Final model saved to {model_save_path}")

weights_save_path = './resnet50_multitask_weights.h5'
model.save_weights(weights_save_path)
print(f"Weights saved to {weights_save_path}")