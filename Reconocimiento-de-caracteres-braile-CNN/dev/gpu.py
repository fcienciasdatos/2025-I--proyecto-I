import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf  
gpus = tf.config.list_physical_devices('GPU')
print(gpus)