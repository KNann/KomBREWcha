#include <Adafruit_CircuitPlayground.h>

int complete=1;

void setup() {
  // put your setup code here, to run once:
CircuitPlayground.begin();

if (complete) {
CircuitPlayground.setPixelColor(2,0,200,0);
CircuitPlayground.playTone(650, 500);
delay(750);
CircuitPlayground.playTone(650, 500);
delay(750);
CircuitPlayground.playTone(650, 500);
delay(750);
delay(2000);}
else {
CircuitPlayground.setPixelColor(2,200,0,0);
delay(2000);}
CircuitPlayground.clearPixels();
}

void loop() {
  // put your main code here, to run repeatedly:

}
