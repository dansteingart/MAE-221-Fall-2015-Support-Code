//Base Spark Code for Labs 1 & 2 (Weeks 1-4)
//MAE 221 Fall 2015 
//This code allows for all ports to be read simultaneously, while setting points one at a time or all at once
#include "Adafruit_MAX31855/Adafruit_MAX31855.h"
#include "math.h"

char publishString[200]; //a place holer for the publish string
int count = 0; //looper that allows us to have a control responsive photon while not flooding the cloud with data every 50 ms
int countto = 20; // wait 20 clicks before publishing data
int waiter = 50; //in ms
int samps = 50; //sampler counter for smooth smoothness

//MAX31855 requires 3 digital pins
int thermoDO = D6;
int thermoCS = D5;
int thermoCLK = D4;

Adafruit_MAX31855 thermocouple(thermoCLK, thermoCS, thermoDO); //define a MAX31855 structure called thermocouple

void setup() //run this loop just once upon start, or upon reset
{
  //This will send back the big data string
  Spark.variable("lab_data", &publishString, STRING);
  //We'll use these to send the digital state
  Spark.function("setOutput", setOutput);
  Spark.function("setOutputs", setOutputs);

  //set analog pins to input mode
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  pinMode(A4, INPUT);
  pinMode(A5, INPUT);
  pinMode(A6, INPUT);
  pinMode(A7, INPUT);
  
  //set digital pins not used by MAX31855 (4,5,6) to output mode
  pinMode(D0, OUTPUT);
  pinMode(D1, OUTPUT);
  pinMode(D2, OUTPUT);
  pinMode(D3, OUTPUT);
  pinMode(D7, OUTPUT); //led

}

void loop() //repeat this loop forever
{
    //declare pin labels as integers
    int a0 = 0;
    int a1 = 0;
    int a2 = 0;
    int a3 = 0;
    int a4 = 0;
    int a5 = 0;
    int a6 = 0;
    int a7 = 0;
    
    int d0;
    int d1;
    int d2;
    int d3;

    //average the readings at each port for stability
    for (int j = 0; j < samps; j++) //sum values samps times
   {
     a0 += analogRead(A0);  
     a1 += analogRead(A1);  
     a2 += analogRead(A2);  
     a3 += analogRead(A3);  
     a4 += analogRead(A4);  
     a5 += analogRead(A5);  
     a6 += analogRead(A6);  
     a7 += analogRead(A7);
     
   }
    // take the average
    a0 = a0/samps;
    a1 = a1/samps;
    a2 = a2/samps;
    a3 = a3/samps;
    a4 = a4/samps;
    a5 = a5/samps;
    a6 = a6/samps;
    a7 = a7/samps;
    
    d0 = digitalRead(0);
    d1 = digitalRead(1);
    d2 = digitalRead(2);
    d3 = digitalRead(3);
    //d4 = digitalRead(4);
    
    //wait countto clicks before sending publish data; blink the led every X to let us know how hard it's working
    if (count > countto )
    {
     float temp = thermocouple.readCelsius(); //read from MAX31855 TC chip
    if (isnan(temp)) 
    {
        temp=-42; //If no TC is connected, temperature whigs out. 
     } 
     sprintf(publishString,"{\"a0\": %d, \"a1\": %d, \"a2\": %d,\"a3\": %d,\"a4\": %d,\"a5\": %d,\"a6\": %d,\"a7\": %d,\"d0\": %d,\"d1\": %d,\"d2\": %d,\"d3\": %d,\"temp\": %f}",a0,a1,a2,a3,a4,a5,a6,a7,d0,d1,d2,d3,temp);
     Spark.publish("lab_data",publishString);
     count = 0;
    }
    
    else count +=1;
    digitalWrite(7,!digitalRead(7));
    delay(waiter);

}

//set one input
int setOutput(String potter)
{
  //break the input string down into two parts.  1st in the bit to control, second is the value.  e.g. 41 means 'pin 4 high', 30 means 'pin 3 low'
  digitalWrite(potter.charAt(0)-48,potter.charAt(1)-48); //subtract 48 to make sense of ascii (i.e. ascii(48) = 0)
  return potter.toInt();
}

//set all inputs at once
int setOutputs(String potter)
{
  //break the input string down into bit parts, update all.  e.g. 1001 sets 0 and 3 high, 1 and 2 low
  digitalWrite(0,potter.charAt(0)-48); //subtract 48 to make sense of ascii (i.e. ascii(48) = 0)
  digitalWrite(1,potter.charAt(1)-48); //subtract 48 to make sense of ascii (i.e. ascii(48) = 0)
  digitalWrite(2,potter.charAt(2)-48); //subtract 48 to make sense of ascii (i.e. ascii(48) = 0)
  digitalWrite(3,potter.charAt(3)-48); //subtract 48 to make sense of ascii (i.e. ascii(48) = 0)
  return potter.charAt(0);
}
