import multiprocessing
import numpy as np
import cv2
import keras as tf
import pyttsx3
import math
import os
from gpiozero import Button

btn = Button(14)

#from model_copy import *

DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def speak(speakQ, ):
    engine = pyttsx3.init()
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume)
    last_msg = ""
    while True:
        msg = speakQ.get()
        while not speakQ.empty():
            msg = speakQ.get()
        if msg != last_msg and msg != "Background":
            last_msg = msg
            engine.say(msg)
            engine.runAndWait()
        if msg == "Background":
            last_msg = ""


def main():
    labels_path = f"{DIR_PATH}/converted_keras/labels.txt"
    labelsfile = open(labels_path, 'r')

    classes = []
    line = labelsfile.readline()
    while line:
        classes.append(line.split(' ', 1)[1].rstrip())
        line = labelsfile.readline()
    labelsfile.close()

    model_path = f"{DIR_PATH}/converted_keras/keras_model.h5"
    model = tf.models.load_model(model_path, compile=False)

    cap = cv2.VideoCapture(0)

    frameWidth = 1024
    frameHeight = 768

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frameWidth)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frameHeight)
    # enable auto gain
    cap.set(cv2.CAP_PROP_GAIN, 0)
    
    # creating a queue to share data to speech process
    speakQ = multiprocessing.Queue()

    # creating speech process to not hang processor
    p1 = multiprocessing.Process(target=speak, args=(speakQ, ), daemon="True")

    # starting process 1 - speech
    p1.start()
    

    while True:

        # disable scientific notation for clarity
        np.set_printoptions(suppress=True)

        # Create the array of the right shape to feed into the keras model.
        # We are inputting 1x 224x224 pixel RGB image.
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        
        check, frame = cap.read()
        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

        
        margin = int(((frameWidth-frameHeight)/2))
        square_frame = frame[0:frameHeight, margin:margin + frameHeight]
        resized_img = cv2.resize(square_frame, (224, 224))
        model_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)

        image_array = np.asarray(model_img)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image_array

        predictions = model.predict(data)
        conf_threshold = 50
        confidence = []
        conf_label = ""
        threshold_class = ""
        per_line = 2  
        bordered_frame = cv2.copyMakeBorder(
            square_frame,
            top=0,
            bottom=30 + 15*math.ceil(len(classes)/per_line),
            left=0,
            right=0,
            borderType=cv2.BORDER_CONSTANT,
            value=[0, 0, 0]
        )

        for i in range(0, len(classes)):
            confidence.append(int(predictions[0][i]*100))
            if confidence[i] > conf_threshold:

                speakQ.put(classes[i])
                threshold_class = classes[i]
                print(threshold_class, " ", confidence[i], "%")
                
                conf_label = classes[i] + ": " + str(confidence[i]) + "%; "

                print(conf_label)
                
            cv2.putText(
                    bordered_frame, 
                    conf_label, 
                    (int(frameWidth-1024), int(frameHeight+5)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    2,
                    (255, 255, 255),
                    1,5
                )

            cv2.namedWindow('Capturing', cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty('Capturing', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow("Capturing", bordered_frame)
        if cv2.waitKey(1) & btn.is_pressed:
            break

    p1.terminate()


if __name__ == '__main__':
    main()