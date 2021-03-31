//recieverOverUSB
#include <SPI.h>
#include <RH_RF95.h>

/* for feather m0 */ 
#define RFM95_CS 8
#define RFM95_RST 4
#define RFM95_INT 3
 
// Change to 434.0 or other frequency, must match RX's freq! 
//DEZE AANPASSEN VOOR NAUWKEURIGHEID
#define RF95_FREQ 434.0
 
// Singleton instance of the radio driver
RH_RF95 rf95(RFM95_CS, RFM95_INT); 

void setup() 
{
  pinMode(RFM95_RST, OUTPUT);
  digitalWrite(RFM95_RST, HIGH);
 
  Serial.begin(115200);
  Serial1.begin(115200);
  
  delay(100);
 
  Serial.println("Feathers LoRa TX Test!");
 
  // manual reset
  digitalWrite(RFM95_RST, LOW);
  delay(10);
  digitalWrite(RFM95_RST, HIGH);
  delay(10);
 
  while (!rf95.init()) {
    Serial.println("LoRa radio 1 init failed");
    while (1);
  } 
  Serial.println("LoRa radio 1 init OK!");
 
  // Defaults after init are 434.0MHz, modulation GFSK_Rb250Fd250, +13dbM
  if (!rf95.setFrequency(RF95_FREQ)) {
    Serial.println("setFrequency failed");
    while (1);
  }
  Serial.print("Set Freq to: "); Serial.println(RF95_FREQ); 
  rf95.setTxPower(23, false);
}

signed RSSI = 0;
int counter = 0;

void loop()
{ 
  delay(500); // Wait 0.5 second between transmits, could also 'sleep' here!

  // Now wait for a reply
  uint8_t buf[RH_RF95_MAX_MESSAGE_LEN];
  uint8_t len = sizeof(buf);

  //wacht op een 
  if (rf95.waitAvailableTimeout(1000))
  {     
    //   
   if (rf95.recv(buf, &len))
   {
      RSSI = rf95.lastRssi();
      String data = Serial1.readStringUntil('\n');
      Serial.print("[ID1:");
      Serial.print(RSSI);
      Serial.println(data);
    }
    else
    {
      Serial.println("Receive failed");
    }
  }
  else
  {
    Serial.println("No reply, is there a listener around?");
  }
}
