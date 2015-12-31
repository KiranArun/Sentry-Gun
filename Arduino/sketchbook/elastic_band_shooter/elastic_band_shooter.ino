#include <Servo.h>

Servo s1;
Servo s2;
Servo s3;

int pos;
int pos2;
int x;
int y;

void setup() 
{
s1.attach(2);
s2.attach(4);
s3.attach(6);
s1.write(90);
s2.write(90);
s3.write(30);
delay(5000);
}

void loop()
{
  x = rand() % 1000;
  pos = map(x, 0, 1000, 70, 110);
  s1.write(pos);
  y = rand() % 1000;
  pos2 = map(y, 0, 1000, 70, 110);
  
  s2.write(pos2);
  delay(500);
  s3.write(180);
  delay(500);
  s3.write(30);
  s1.write(90);
  s2.write(90);
  delay(13000);  
}

