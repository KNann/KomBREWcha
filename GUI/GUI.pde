PFont f;
PImage img;
import java.io.*;
import java.util.*;
import processing.serial.*;

boolean takeOver = false;
boolean newOver = false;
color statusColor;
String picpath;

void setup () {
//setup the size of the GUI to be the size of the touchscreen
size (800, 480); 

//status indicator starts out red
statusColor = color(247,19,19);

//path for the batch progress graph
picpath = "/home/pi/KomBREWcha/Batch_Progress_Graphs/";

// Create font for text
//printArray(PFont.list());
f = createFont("Times New Roman", 24);
textFont(f);
}

void draw () {
  //gray background
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
 
  //read first line from colorsLog.txt and extract timestamp
  String log[] = loadStrings("/home/pi/KomBREWcha/colorsLog.txt");
  String init = log[0];
  init = init.substring(0,19);
  
  //create graph title from timestamp
  String title = "Batch Started: "+init+".png";
  String fullpath = picpath+title;
  
  //load image of graph onto GUI on the rigth hand side
  img = loadImage(fullpath);
  image(img, 420, 50, width/2.2, height/1.3);
  
  //Screen text in function below
  textAlign(CENTER);
  drawType(width * 0.5);
  
  //mouse button update function is coded below text function
  update(mouseX,mouseY);


}

void drawType(float x) {
  //line(x, 0, x, 65);
  //line(x, 220, x, height);
  fill(0); //black text
  text("KomBREWcha",x-200,50); //title at top of left hand side
  text("Take Measurement",x-200,156); //take measurement button
  text("Batch Status:",280,260); //title oabove batch status inidicator
  text("Start New",85,340); //start new batch button
  text("Batch",85,370); //start new batch button
  
}

//sense if mouse is over the button
void update(int x, int y) {
  //overRect function coded below
  //Mouse is over the Take Measurement button
  if ( overRect(20,100,360,100)) {
    takeOver = true;
    newOver = false;
    
  //Mouse is over the Start New Batch button
  } else if ( overRect(20,285,130,130)) {
    takeOver = false;
    newOver = true;
    
  //Mouse is not over a button anywhere else
  } else {
    takeOver = false;
    newOver = false;
  }
}

//take action if mouse was pressed over a button
void mousePressed() {
  String Readystr = "1"; //compare against the contents of complete.txt later
  
  //run driver.sh if Take Measurement is pressed
  if (takeOver) {
    statusColor = color(237,226,30); //yellow status while code is running
    fill(statusColor);
    ellipse(275,350,130,130); //yellow status inidcator while code is running
    exec("/home/pi/KomBREWcha/driver.sh");
    delay(30000); //wait 30 seconds for code to run
    
    //change status indicator color based on result of analysis from driver.sh
    String done[] = loadStrings("/home/pi/KomBREWcha/complete.txt");
    
    //complete.txt will read "1" if the brew is ready
    if (Readystr.equals(done[0]) == true) {
      statusColor = color(34,237,30); //green
    } else {
      statusColor = color(247,19,19); //red
    }
    //status color will be updated in the next iteration of the draw function
  }
  
  //run new-batch.sh if Start New Batch is pressed, same procedure as
  //take measurement button but executing new_batch.sh instead of driver.sh
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

//returns a true or false value whether or not the mouse is in the area indicated by the inputs
boolean overRect(int x, int y, int w, int h) {
  if (mouseX >= x && mouseX <= x+w &&
      mouseY >= y && mouseY <= y+h) {
    return true;
  } else {
    return false;
  }  
}

//forces the code to wait 
void delay(int delay) {
  int time = millis();
  while(millis() - time <= delay);
}