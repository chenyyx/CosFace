#!usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

from datetime import datetime
import os.path
import os
import time
import sys

import tensorflow as tf

w = tf.Variable(tf.random_normal([1], -1, 1))
b = tf.Variable(tf.zeros([1]))

sess = tf.Session()
saver = tf.train.Saver()
saver.restore(sess, '/Users/Documents/tf_cosface_models/model-20180626-205832.ckpt-60000.data-00000-of-00001')
print(sess.run(w))
print(sess.run(b))