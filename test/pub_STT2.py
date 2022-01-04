# coding=UTF-8 
import rclpy 
import time
from rclpy.node import Node 
from std_msgs.msg import String
import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as source:
    print("Please wait. Calibrating microphone...")
    r.adjust_for_ambient_noise(source, duration=2)
    print("Say something!")
    audio=r.listen(source, timeout=3)
try:
    result = r.recognize_google(audio, language = "zh-TW")
    print(result)
    if result == "前進":
        print("front")
    elif result == "後退":
        print("back")
    elif result == "右轉":
        print("right")
    elif result == "左轉": 
        print("left")
    else:
        print("try agin")
except sr.UnknownValueError:
    print("Google Speech Recongnition could not understand audio")
except sr.RequestError as e:
    print("No response from Google Speech Recognition servcie: {0}".format(e))