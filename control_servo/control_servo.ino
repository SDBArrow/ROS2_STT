#include<Servo.h>
Servo servoright;
Servo servoleft;
int time = 2000;
void setup(){
  servoright.attach(12);
  servoleft.attach(13);
  Serial.begin(9600);
}
void loop(){
  servoleft.writeMicroseconds(1500);
  servoright.writeMicroseconds(1500);
  delay(time);
  char c;
  if(Serial.available()>0)
  {
    c = Serial.read();
    switch(c){
      case 'R':
        servoleft.writeMicroseconds(1600);
        servoright.writeMicroseconds(1600);
        delay(time);
        break;
      case 'L':
        servoleft.writeMicroseconds(1400);
        servoright.writeMicroseconds(1400);
        delay(time);
        break;
      case 'B':
        servoleft.writeMicroseconds(1400);
        servoright.writeMicroseconds(1600);
        delay(time);
        break;
      case 'F':
        servoleft.writeMicroseconds(1600);
        servoright.writeMicroseconds(1400);
        delay(time);
        break;
    } 
  }
}


