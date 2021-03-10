# Voor de berekening van de hoek voor de servo hebben we een aantal berekeningen nodig
# De servo wordt aangestuurd met 2 hoeken:
# hoek alhpa zal zorgen voor de draai richting tussen de 0 en 360 graden
# hoek tetha zal zorgen voor de opwaardse beweging tussen 0 en 45 graden
# In deze code zal er manueel de coordinaat van de persoon ingegeven worden
# De servo hangt standaard vast op volgende coördinaat: (100, 200, 300)
import math

print("Hier gaan we de hoeken berekenen voor de servo aansturing")

servoX = 100
servoY = 200
servoZ = 300
persoonZ = 300

print("Geef de X-coordinaat in van de persoon:")
persoonX = int(input())
print("Geef de Y-coordinaat in van de persoon:")
persoonY = int(input())
print(persoonX, persoonY)

afstand= math.sqrt((persoonX - servoX)**2 + (persoonY - servoY)**2)
hoekAlpha = math.atan2(persoonY - servoY,persoonX - servoX )
hoekTheta = math.atan2(afstand,persoonZ)

hoekThetaGraden = math.degrees(hoekTheta)
hoekAlphaGraden = math.degrees(hoekAlpha)

print(afstand,hoekThetaGraden,hoekAlphaGraden)
