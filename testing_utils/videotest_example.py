import keras
import pickle
from videotest import VideoTest

import sys
sys.path.append("..")
from ssd import SSD300 as SSD

input_shape = (300,300,3)

# Change this if you run with other classes than VOC
class_names = ["car"]
NUM_CLASSES = 2

model = SSD(input_shape, num_classes=NUM_CLASSES)

# Change this path if you want to use your own trained weights
model.load_weights('../weights99-4-98.hdf5')
        
vid_test = VideoTest(class_names, model, input_shape)

# To test on webcam 0, remove the parameter (or change it to another number
# to test on that webcam)
vid_test.run('./inputs/Corvette-35266.mp4')
