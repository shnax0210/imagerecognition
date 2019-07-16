from keras.preprocessing import image as image_utils
from image_utils import decode_predictions
from image_utils import preprocess_input
from vgg19 import VGG19
import numpy as np

model = VGG19(weights="imagenet")


def predict(file):
    image = image_utils.load_img(file, target_size=(224, 224))
    image = image_utils.img_to_array(image)

    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)

    preds = model.predict(image)
    (inID, label) = decode_predictions(preds)[0]

    return label

