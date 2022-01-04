# coding=UTF-8 
import rclpy 
import time
from rclpy.node import Node 
from std_msgs.msg import String
import speech_recognition as sr

class STT_pub(Node): 
    def __init__(self): 
        super().__init__('STT_pub')
        # 定義節點包含一個發送端 
        self.publisher_ = self.create_publisher(String, 'STT', 10) 
        self.timer = self.create_timer(1, self.timer_callback) 
    def timer_callback(self): 
        r=sr.Recognizer()
        msg = String()
        msg.data = "no word" 
        with sr.Microphone() as source:
            print("Please wait. Calibrating microphone...")
            r.adjust_for_ambient_noise(source, duration=2)
            print("Say something!")
            try: 
                audio=r.listen(source) 
                msg.data = r.recognize_google(audio, language = "zh-TW")
                print (msg.data)
            except sr.UnknownValueError:
                print("Google Speech Recongnition could not understand audio")
            except sr.RequestError as e:
                print("No response from Google Speech Recognition servcie: {0}".format(e))    
        # 由於是物件導向，訊息也是字串物件裡面的一個屬性
        # 呼叫發送端發送訊息
        self.publisher_.publish(msg) 

if __name__ == '__main__': 
    rclpy.init() 
    STT_publisher = STT_pub() 
    rclpy.spin(STT_publisher) 
    STT_publisher.destroy_node() 
    rclpy.shutdown()