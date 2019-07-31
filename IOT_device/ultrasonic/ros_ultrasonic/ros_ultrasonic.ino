#include <Ultrasonic.h>

/*
 * https://github.com/ErickSimoes/Ultrasonic
 * https://www.arduinolibraries.info/libraries/ultrasonic
 * The circuit:
 * * Module HR-SC04 (four pins) or PING))) (and other with
 *   three pins), attached to digital pins as follows:
 * ---------------------    --------------------
 * | HC-SC04 | Arduino |    | 3 pins | Arduino |
 * ---------------------    --------------------
 * |   Vcc   |   5V    |    |   Vcc  |   5V    |
 * |   Trig  |   11    | OR |   SIG  |   13    |
 * |   Echo  |   12    |    |   Gnd  |   GND   |
 * |   Gnd   |   GND   |    --------------------
 * ---------------------
 */
Ultrasonic ultrasonic(11, 12);
int distance;
char *result = malloc(4);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  ultrasonic.setTimeout(40000UL);
  //Using a 40ms timeout should give you a maximum range of approximately 6.8m
}

void loop() {
  // put your main code here, to run repeatedly:
  distance = ultrasonic.read();
  if(distance > 999){distance = 999;}
  sprintf(result, "%03d", distance);
  Serial.print("S");
  Serial.print("U");
  Serial.print(result);
  Serial.print("E");
  delay(1000);
}
