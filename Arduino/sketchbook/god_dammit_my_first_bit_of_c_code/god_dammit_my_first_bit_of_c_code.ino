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

void loop() // go into a loop
{
  val = analogRead(potpin); //read the potpin which is connected to a potentiometer
  if (val <= 511) { // if the potentiometer is less then halfway, the motor is off
    s = 0;
  }
  else { // if the potentiometer is more then halfway, the motor is on
    s = 12; // this i measured so that it gave out about 7V, perfect for the motor in my BB gun
  }
  m1.write(s); // write whatever the output of teh loop is to the motor
}

