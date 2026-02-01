import tensorflow as tf
import tensorflow as tf
layers = tf.keras.layers
models = tf.keras.models

def build_cnn():

    model = models.Sequential([

        layers.Input(shape=(128,128,1)),

        layers.Conv2D(32,3,activation="relu"),
        layers.MaxPooling2D(),

        layers.Conv2D(64,3,activation="relu"),
        layers.MaxPooling2D(),

        layers.Conv2D(128,3,activation="relu"),
        layers.MaxPooling2D(),

        layers.Flatten(),
        layers.Dense(128,activation="relu"),
        layers.Dropout(0.4),

        layers.Dense(1,activation="sigmoid")
    ])

    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )

    return model
