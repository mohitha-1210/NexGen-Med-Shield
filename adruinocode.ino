#include <Servo.h>
#include "HX711.h"

// PIN CONFIGURATION

const int s0 = 4, s1 = 5, s2 = 6, s3 = 7, sensorOut = 8; // Color Sensor
const int irPin = 2;                     
  // Entry Sensor
const int servoPin = 3;
                                  // Sorting Gate
const int motorPin = 10;
                                 // BO Shredder Motor
const int hx711_dt = A0, hx711_sck = A1;
                 // Weight Scale
HX711 scale;
Servo gate;

void setup(){
   Serial.begin(9600);    
   
   // Color Sensor Pins  
   pinMode(s0, OUTPUT); pinMode(s1, OUTPUT);  
   pinMode(s2, OUTPUT); pinMode(s3, OUTPUT);  
   pinMode(sensorOut, INPUT);  
   digitalWrite(s0, HIGH); digitalWrite(s1, LOW); // Frequency scaling to 20%  
   
   pinMode(irPin, INPUT);  
   pinMode(motorPin, OUTPUT);    
   
   gate.attach(servoPin);
   gate.write(0);   // Start at Closed position  
   // Weight Sensor Calibration  
   scale.begin(hx711_dt, hx711_sck);  
   scale.set_scale(420.0); // Adjust this number for calibration  
   scale.tare();           // Reset to zero    
   
   Serial.println("SYSTEM_READY"); // Tells Python the connection is live
   }
   
   void loop() {  
    // 1. Detect Entry (IR Sensor goes LOW when pill passes)  
    if (digitalRead(irPin) == LOW) {  
        delay(1000); // Wait for pill to settle on the Load Cell    
        // 2. Read Color (Simplified Logic)    
        digitalWrite(s2, LOW); digitalWrite(s3, LOW);    
        int red = pulseIn(sensorOut, LOW);    
        digitalWrite(s2, HIGH); digitalWrite(s3, HIGH);    
        int green = pulseIn(sensorOut, LOW);        
        
        String status = (red < green) ? "Authentic" : "Fake";    
        
        // 3. Read Weight    
        float weight = scale.get_units(5); // Average of 5 readings    
        if (weight < 0) weight = 0.0;    
        // 4. SEND DATA TO PYTHON (Crucial Format!)    
        // Python expects: 
        //STATUS:Value,WEIGHT:Value    
        Serial.print("STATUS:");    
        Serial.print(status);    
        Serial.print(",WEIGHT:");    
        Serial.println(weight);
        Serial.flush();
        delay(100);    
        
        // 5. Actuators - Sequential to prevent power spikes    
        if (status == "Authentic") {     
           gate.write(90); // Move to "Valid" bin     
            delay(2000);     
             gate.write(0);    
             } else {      // It's "Fake" - activate shredder      
             digitalWrite(motorPin, HIGH);       
             delay(3000);       
             digitalWrite(motorPin, LOW);    
             }    
             
             scale.tare(); // Reset for the next pill    
             delay(1000);  // Cooldown  
             }
}