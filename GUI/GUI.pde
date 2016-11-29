PFont f;
PImage img;
import java.io.*;
import java.util.*;
import processing.serial.*;

boolean takeOver = false;
boolean newOver = false;
color statusColor;

void setup () {
size (800, 480); 
statusColor = color(247,19,19);

// Create font for text
//printArray(PFont.list());
f = createFont("Times New Roman", 24);
textFont(f);
}

void draw () {
  background(204);
  
  //Take Measurement button
  fill(66,182,244);
  rect(20,100,360,100);
  
  //Status Indicator
  fill(statusColor);
  ellipse(275,350,130,130);
  
  //New batch button
  fill(66,182,244);
  rect(20,285,130,130);
  
  
  String picpath = "/home/pi/KomBREWcha/Batch_Progress_Graphs/Batch Started: 2016-11-17 01:24:09.png";
  String log[] = loadStrings("/home/pi/KomBREWcha/colorsLog.txt");
  String init = log[0];
  String t0 = split(init,'|');
  img = loadImage(picpath);
  image(img, 420, 50, width/2.2, height/1.3);
  
  //Screen text in function below
  textAlign(CENTER);
  drawType(width * 0.5);
  
  //mouse button
  update(mouseX,mouseY);


}

void drawType(float x) {
  //line(x, 0, x, 65);
  //line(x, 220, x, height);
  fill(0);
  text("KomBREWcha",x-200,50);
  text("Take Measurement",x-200,156);
  text("Batch Status:",280,260);
  text("Start New",85,340);
  text("Batch",85,370);
  
}

//sense if mouse is over the button
void update(int x, int y) {
  
  //Take Measurement button
  if ( overRect(20,100,360,100)) {
    takeOver = true;
    newOver = false;
    
  //Start New Batch button
  } else if ( overRect(20,285,130,130)) {
    takeOver = false;
    newOver = true;
    
  //anywhere else
  } else {
    takeOver = false;
    newOver = false;
  }
}

void mousePressed() {
  String Readystr = "1";
  //String Waitstr = "Not Ready";
  //run driver.sh if Take Measurement is pressed
  if (takeOver) {
    statusColor = color(237,226,30); //yellow
    fill(statusColor);
    ellipse(275,350,130,130);
    exec("/home/pi/KomBREWcha/driver.sh");
    delay(30000);
    
    //change status indicator color based on result
    String done[] = loadStrings("/home/pi/KomBREWcha/complete.txt");
    if (Readystr.equals(done[0]) == true) {
      statusColor = color(34,237,30); //green
    } else {
      statusColor = color(247,19,19); //red
    }
  }
  //run new-batch.sh if Start New Batch is pressed
  if (newOver) {
    statusColor = color(237,226,30); //yellow
    fill(statusColor);
    ellipse(275,350,130,130);
    exec("/home/pi/KomBREWcha/new-batch.sh");
    delay(30000);
    
    //change status indicator color based on result
    String done[] = loadStrings("/home/pi/KomBREWcha/complete.txt");
    if (Readystr.equals(done[0]) == true) {
      statusColor = color(34,237,30); //green
    } else {
      statusColor = color(247,19,19); //red
    }
  }
  
  
}

boolean overRect(int x, int y, int w, int h) {
  if (mouseX >= x && mouseX <= x+w &&
      mouseY >= y && mouseY <= y+h) {
    return true;
  } else {
    return false;
  }  
}

void delay(int delay) {
  int time = millis();
  while(millis() - time <= delay);
}