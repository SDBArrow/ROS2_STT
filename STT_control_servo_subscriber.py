# coding=UTF-8 
import rclpy 
from rclpy.node import Node 
from std_msgs.msg import String 
import serial
import time

port = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=3.0)

class STT_sub(Node): 
    def __init__(self): 
        super().__init__('STT_sub') 
        self.subscription = self.create_subscription(String,"STT",self.listener_callback,10) 
        self.subscription #prevent unused variable warning 

    def listener_callback(self, msg): 
        self.get_logger().info('I heard: "%s"' % msg.data) 
        if msg.data == "往前":
            port.write('F'.encode('ascii'))
        elif msg.data == "後退":
            port.write('B'.encode('ascii'))
        elif msg.data == "右轉":
            port.write('R'.encode('ascii'))
        elif msg.data == "左轉": 
            port.write('L'.encode('ascii'))
        else:
            print("try agin")

if __name__ == '__main__': 
    rclpy.init() 
    STT_subscriber = STT_sub() 
    rclpy.spin(STT_subscriber) 
    STT_subscriber.destroy_node() 
    rclpy.shutdown()
