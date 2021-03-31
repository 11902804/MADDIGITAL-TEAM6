//TrackerCode
#include <SPI.h>
#include <RH_RF95.h>

/* for feather m0 */ 
#define RFM95_CS 8
#define RFM95_RST 4
#define RFM95_INT 3
 
// Change to 434.0 or other frequency, must match RX's freq! 
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
 
int16_t packetnum = 0;  // packet counter, we increment per xmission
signed  uitkomst = 0;
int counter = 0;
void loop()
{
  delay(500); // Wait 0.5 second between transmits, could also 'sleep' here!
  Serial.println("Transmitting..."); // Send a message to rf95_server

  char radiopacket[3] = "ID1";
  itoa(packetnum++, radiopacket+13, 10);
  Serial.print("Sending "); Serial.println(radiopacket);
  radiopacket[19] = 0;
  Serial.println("Sending...");
  delay(10);
  rf95.send((uint8_t *)radiopacket, 20);
  rf95.waitPacketSent();

}
