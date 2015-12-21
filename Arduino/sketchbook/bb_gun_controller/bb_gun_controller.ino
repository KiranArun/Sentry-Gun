#include <Servo.h>

Servo m1;
Servo myservo;

int pos;
int s;

void setup()
{
m1.attach(4);
m1.write(0);
delay(1000);
myservo.attach(2);
m1.write(120);
}

void loop()
{
  for(pos = 0; pos < 180; pos += 1)  
  {                                  
    myservo.write(pos);              
    delay(5);                      
  } 
  for(pos = 180; pos>=1; pos-=1)     
  {                                
    myservo.write(pos);             
    delay(5);
  }
}  

