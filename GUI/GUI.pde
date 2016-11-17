PFont f;
import java.io.*;
import processing.serial.*;

boolean takeOver = false;
boolean newOver = false;
boolean seeOver = false;
color statusColor;

void setup () {
size (800, 480); 
statusColor = color(247,19,19);

// Create font for text
printArray(PFont.list());
f = createFont("Times New Roman", 24);
textFont(f);
}

void draw () {
  background(204);
  
  //Take Measurement button
  fill(66,182,244);
  rect(200,100,400,100);
  
  //Status Indicator
  fill(statusColor);
  ellipse(400,350,130,130);
  
  //New batch button
  fill(66,182,244);
  rect(105,285,130,130);
  
  //See batch progress button
  fill(66,182,244);
  rect(565,285,130,130);
  
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
  text("KomBREWcha",x,50);
  text("Take Measurement",x,156);
  text("Batch Status:",x,260);
  text("Start New",x-230,340);
  text("Batch",x-230,370);
  text("See Batch",x+230,340);
  text("Progress",x+230,370);
  
}

//sense if mouse is over the button
void update(int x, int y) {
  
  //Take Measurement button
  if ( overRect(200,100,400,100)) {
    takeOver = true;
    newOver = false;
    seeOver = false;
    
  //Start New Batch button
  } else if ( overRect(105,285,130,130)) {
    takeOver = false;
    newOver = true;
    seeOver = false;
    
  //See Batch Progress button
  } else if ( overRect(565,285,130,130)) {
    takeOver = false;
    newOver = false;
    seeOver = true;
    
  //anywhere else
  } else {
    takeOver = newOver = seeOver = false;
  }
}

void mousePressed() {
  File workingDir = new File("/home/pi/KomBREWcha");
  if (takeOver) {
    statusColor = color(237,226,30);
    
    //try to run driver!
    try {
    Process p = Runtime.getRuntime().exec("./driver.sh", null, workingDir);
    }
    
    catch (Exception e) {
      println("Error running command!");
      println(e);
    }
  }
  if (newOver) {
    statusColor = color(34,237,30);
  }
  if (seeOver) {
    statusColor = color(247,19,19);
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