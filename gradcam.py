import tensorflow as tf
import numpy as np

def grad_cam(model, img, layer_name="conv2d_2"):

    grad_model = tf.keras.models.Model(
        [model.inputs],
        [model.get_layer(layer_name).output, model.output]
    )

    with tf.GradientTape() as tape:
        conv_output, pred = grad_model(img)
        loss = pred[:,0]

    grads = tape.gradient(loss, conv_output)
    pooled = tf.reduce_mean(grads, axis=(0,1,2))

    heatmap = tf.reduce_sum(conv_output[0] * pooled, axis=-1)
    heatmap = tf.maximum(heatmap,0)
    heatmap /= tf.reduce_max(heatmap)

    return heatmap.numpy()
