#define button 2
#define green_led 12
#define yellow_led 11
#define red_led 10
bool red_or_green = false;
int button_current;
int button_previous = LOW;

int green_state = LOW;
int yellow_state = LOW;
int red_state = LOW;

void setup() {
  pinMode(button,INPUT);
  pinMode(green_led,OUTPUT);
  pinMode(yellow_led,OUTPUT);
  pinMode(red_led,OUTPUT);
}

void loop() {
  button_current = digitalRead(button); 
  if(button_current == HIGH && button_previous == LOW){

  if(green_state==LOW && yellow_state==LOW && red_state==LOW){
    green_state=HIGH;
  }
  else if(green_state==HIGH){
    green_state=LOW;
    yellow_state=HIGH;
    red_or_green = true;
  }
  else if(red_state==HIGH){
    red_state=LOW;
    yellow_state=HIGH;
    red_or_green = false;
  }
  else if(yellow_state==HIGH){
    if(red_or_green == true){
    yellow_state=LOW;
    red_state=HIGH;
    }
    else{
    yellow_state=LOW;
    green_state=HIGH;
    }
  }
  }
  digitalWrite(green_led,green_state);
  digitalWrite(yellow_led,yellow_state);
  digitalWrite(red_led,red_state);
  button_previous = button_current;
  delay(10);
}

