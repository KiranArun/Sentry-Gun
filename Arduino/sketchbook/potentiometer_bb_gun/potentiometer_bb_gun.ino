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
  s = map(val, 100, 1023, 121, 130);
  if (val < 100) {
    s = 0;
  }  
  m1.write(s);
}

