import time
import keras
from keras.preprocessing import image
import os
import glob

model = keras.models.load_model('/models')

while(True):

    # Get set of all current images
    image_paths = glob.glob('*.jpg')

    # Fetch the most recent images
    image_dataset = image.image_dataset_from_directory('/final/images')
    
    # Predict the piece
    predictions = model.predict_classes(image_dataset)
    print(predictions)

    # Only update every quarter second
    #time.sleep(0.25)

    break