// importing the servo library for controlling
#include <Servo.h>

// m1 which is a motor and myservo which is a servo are both treated as servos
Servo m1;
Servo myservo;

// initializing the variable pos(position of servo)
int pos;

// setting up the arduino connectios
void setup()
{
m1.attach(4); // attach the motor to the pwm pin 4
m1.write(0); // write to the motor to have the value 0
delay(1000); // wait a second
myservo.attach(2); //attach the servo to pwm pin 2
m1.write(120); // writes the value 120 to the motor which is about 7V
}

void loop()
{
  for(pos = 0; pos < 180; pos += 1)  // servo goes from 0 to 180
  {                                  
    myservo.write(pos);  // write the value to the servo            
    delay(5);                       
  } 
  for(pos = 180; pos>=1; pos-=1) // servo goes from 180 to 0
  {                                
    myservo.write(pos); // write to the servo             
    delay(5);
  }
}  

