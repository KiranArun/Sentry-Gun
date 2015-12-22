// importing the servo library for controlling
#include <Servo.h>

// i made m1 which is the motor be treated like a servo
Servo m1;

// initializing the variables
int potpin = 0;
int val;
int s;

// the setup for the arduino
void setup() 
{
m1.attach(2); //attaching the pwm pin to the motor to control it
m1.write(0); // starting the motor in a 0 position
delay(1000); // wait a second
}

void loop()
{
  val = analogRead(potpin); //read the potpin which is connected to a potentiometer
  s = map(val, 100, 1023, 121, 130); // evenly map out the values 100-1023 (potentiometer) to 120-130 (speed of motor)
  if (val < 100) { // if the value is less then 100,
    s = 0;         // s is 0
  }  
  m1.write(s); // write to the motor
}

