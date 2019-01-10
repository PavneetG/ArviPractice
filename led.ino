const int led = 13; 

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led, OUTPUT)

}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available())
  {
    data = Serial.read();
  }

  if (data == '1')
  {
    digitalWrite(led, HIGH); 
  }
}
