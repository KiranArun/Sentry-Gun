#include <Servo.h>



Servo m1;

int potpin = 0;
int val;
int s;


void setup() 
{
m1.attach(2);
m1.write(0);
delay(1000);
}

void loop()
{
  val = analogRead(potpin);
  if (val <= 511) {
    s = 0;
  }
  else {
    s = 12god dammit my first bit of c cod;
  }
  m1.write(s);
}

