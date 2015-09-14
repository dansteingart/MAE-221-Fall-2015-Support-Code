//Base Spark Code for Labs 1 & 2 (Weeks 1-4)
//MAE 221 Fall 2015 
//This code allows for all ports to be read simultaneously, while setting points one at a time.
//PERHAPS FOR FUTURE: Set pots at once (e.g. 1111 sets D0-D3 to high, 0101 does what it should)


char publishString[200]; //a place holer for the publish string

void setup()
{
  //This will send back the big data string
  Spark.variable("lab_data", &publishString, STRING);

  //We'll use this to send the digital state
  Spark.function("setOutput", setOutput);

  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  pinMode(A4, INPUT);
  pinMode(A5, INPUT);
  pinMode(A6, INPUT);
  pinMode(A7, INPUT);
  pinMode(D0, OUTPUT);
  pinMode(D1, OUTPUT);
  pinMode(D2, OUTPUT);
  pinMode(D3, OUTPUT);
  pinMode(D4, OUTPUT);


}

void loop()
{
  // Keep reading the sensor value so when we make an API
  // call to read its value, we have the latest one
    
    
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
    int d4;


    //sample each port samps times and then average
   int samps = 50;
   for (int j = 0; j < samps; j++) 
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
   
   a0 = a0/samps;
   a1 = a1/samps;
   a2 = a2/samps;
   a3 = a3/samps;
   a4 = a4/samps;
   a5 = a5/samps;
   a6 = a6/samps;
   a7 = a7/samps;


   //read the DIO states
   d0 = digitalRead(0);
   d1 = digitalRead(1);
   d2 = digitalRead(2);
   d3 = digitalRead(3);
   d4 = digitalRead(4);

   //send the state of the state
   sprintf(publishString,"{\"a0\": %d, \"a1\": %d, \"a2\": %d,\"a3\": %d,\"a4\": %d,\"a5\": %d,\"a6\": %d,\"a7\": %d,\"d0\": %d,\"d1\": %d,\"d2\": %d,\"d3\": %d}",a0,a1,a2,a3,a4,a5,a6,a7,d0,d1,d2,d3);
   Spark.publish("lab_data",publishString);

  //wait a second (or whatever)
  delay(1000);

}


int setOutput(String potter)
{
  //break the input string down into two parts.  1st in the bit to control, second is the value.  e.g. 41 means 'pin 4 high', 30 means 'pin 3 low'
  digitalWrite(potter.charAt(0)-48,potter.charAt(1)-48); //subtract 48 to make sense of ascii (i.e. ascii(48) = 0)
  return potter.toInt();
}
