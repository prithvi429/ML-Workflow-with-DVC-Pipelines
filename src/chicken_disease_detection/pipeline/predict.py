import os
import sys
import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing import image  


# Disable oneDNN optimizations warning
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

print("Using interpreter:", sys.executable)

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        try:
            # Construct model path
            model_path = os.path.join("artifacts", "training", "model.h5")
            print(f"Trying to load model from: {model_path}")
            if not os.path.exists(model_path):
                raise FileNotFoundError(f"Model file not found at {model_path}")
            
            # Load model
            model = load_model(model_path)
            print("Model loaded successfully.")

            # Load and preprocess image
            imagename = self.filename
            print(f"Trying to load image from: {imagename}")
            if not os.path.exists(imagename):
                raise FileNotFoundError(f"Image file not found at {imagename}")

            test_image = image.load_img(imagename, target_size=(224, 224))
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis=0)

            # Make prediction
            prediction_probs = model.predict(test_image)
            result = np.argmax(prediction_probs, axis=1)
            print("Prediction result:", result)

            # Interpret result
            if result[0] == 1:
                prediction = 'Healthy'
            else:
                prediction = 'Coccidiosis'

            return [{ "image": prediction }]
        
        except Exception as e:
            print("An error occurred during prediction:", str(e))
            return [{ "error": str(e) }]
