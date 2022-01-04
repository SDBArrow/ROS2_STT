# coding=UTF-8 
import rclpy 
from rclpy.node import Node 
from std_msgs.msg import String 
import serial
import time
import epd2in9
from PIL import Image,ImageDraw,ImageFont
import sys

epd = epd2in9.EPD()
epd.init(epd.lut_full_update)
port = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=3.0)

class STT_sub(Node): 
    def __init__(self): 
        super().__init__('STT_sub') 
        self.subscription = self.create_subscription(String,"STT",self.listener_callback,10) 
        self.subscription #prevent unused variable warning 

    def servoimgaechange(self, msg): 
        port.write(msg.data.encode('ascii'))
        image = Image.open('./image/' + msg.data + '.bmp')
        epd.set_frame_memory(image, 0, 0)
        epd.display_frame()
        
    def listener_callback(self, msg): 
        self.get_logger().info('I heard: "%s"' % msg.data) 
        if msg.data == "往前":
            msg.data = 'F'
            self.servoimgaechange(msg)
        elif msg.data == "後退":
            msg.data = 'B'
            self.servoimgaechange(msg)
        elif msg.data == "右轉":
            msg.data = 'R'
            self.servoimgaechange(msg)
        elif msg.data == "左轉": 
            msg.data = 'L'
            self.servoimgaechange(msg)
        elif msg.data == "結束": 
            msg.data = 'C'
            self.servoimgaechange(msg)
            STT_subscriber.destroy_node()
            rclpy.shutdown()
            sys.exit()
        else:
            print("try agin")

if __name__ == '__main__': 
    rclpy.init() 
    STT_subscriber = STT_sub() 
    rclpy.spin(STT_subscriber) 
    STT_subscriber.destroy_node() 
    rclpy.shutdown()
