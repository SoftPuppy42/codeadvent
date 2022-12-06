#include <Arduino.h>
#include <LiquidCrystal.h>
#define LCD_RS 8
#define LCD_ENABLE 9
#define LCD_DB4 4
#define LCD_DB5 5
#define LCD_DB6 6
#define LCD_DB7 7
#define LCD_Backlight 10
LiquidCrystal lcd(LCD_RS, LCD_ENABLE, LCD_DB4, LCD_DB5, LCD_DB6, LCD_DB7);

int data[] = {

};


void setup() {
  pinMode(LCD_Backlight, OUTPUT); 
  analogWrite(LCD_Backlight, 128);
  lcd.begin(16, 2);
  lcd.home();
  lcd.print("Test");

}

void loop() {
  // put your main code here, to run repeatedly:

}