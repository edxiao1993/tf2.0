#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import tensorflow as tf

mnist = tf.keras.datasets.mnist

# load data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# flat the date
x_train, x_test = x_train / 255.0, x_test / 255.0

# add sequential
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

# compile
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# start to train
model.fit(x_train, y_train, epochs=5)

# evaluate
model.evaluate(x_test, y_test)
