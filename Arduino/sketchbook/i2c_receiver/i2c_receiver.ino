#include <Wire.h>
#include <Servo.h>

#define SLAVE_ADDRESS 0x04
//make sure the i2c connection is at the right address

Servo s1;
Servo s2;
Servo s3;
int number;
int pos;
int pos2;
int x;
int y;
int state = 0;
//just setting up all the variables and servos

void setup(){
  pinMode(13,OUTPUT);
  Serial.begin(9600);
  Wire.begin(SLAVE_ADDRESS);
  //setting up the i2c connection with the arduino only acting as the slave
  
  Wire.onReceive(receiveData);
  //get the data from the rpi
  s1.attach(2);
  s2.attach(4);
  s3.attach(6);
  s1.write(105);
  s2.write(90);
  s3.write(30);
  //set up all the servos pins and initial positions


}

void loop(){
    delay(15000);
    s3.write(180);
    delay(500);
    s3.write(30);
    //every 15 seconds the 3rd servo lets go of the elestic band
}

void receiveData(int byteCount){ //recieve data from rpi
  while(Wire.available()){ //if it is available
    number=Wire.read(); //read the value
    if (number <= 100){ 
      x = number;
      pos = map(x, 79, 0, 90, 130);
      s1.write(pos);
      Serial.println(x);
      //if it is below 100, map it out to the servo and write the value to the servo
    }
    else{
      y = number - 100;
      pos2 = map(y, 59, 0, 100, 160);
      s2.write(pos2);
      Serial.print(y);
      //if it is above 100,takeaway 100 and map it out and write it to the servo
    }
  }
}


