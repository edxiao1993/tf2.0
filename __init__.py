#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tensorflow as tf
import random as rd

print(tf.__version__)
print(tf.executing_eagerly())

x = rd.random() * 100
print(x)
