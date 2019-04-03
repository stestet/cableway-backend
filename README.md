# Cableway

## Intro

Das ist das Bastelprojekt für meinen Sohn bei dem es um die Fernsteuerung einer Holzspielzeug-Seilbahn geht.
Die Holzspielzeug-Seilbahn hat 2 Kabinen bei welchen das Zugseil 'bergseitig' via 2 Rollen umgelenkt wird.
Via diese Rollen kann die Seilbahn manuell angetrieben werden. Diese beide Rollen werden neu durch 2 Gleichstrommotor-getriebene Exemplare ersetzt.

Zum Einsatz kommen:

- Holzspielzeug-Seilbahn
- 2 Getriebemotoren mit Rad (https://www.reichelt.de/getriebemotor-mit-rad-3-9-v-welle-3-5-mm-com-motor-rad-p219038.html)
- Raspberry Pi Model 3 B
- RPi Motor Driver Board (https://www.waveshare.com/rpi-motor-driver-board.htm)
- Powerbank (https://www.manualslib.com/manual/1192439/Tecxus-Tp-10000.html)
- altes Smartphone

## Lösungsansatz

Der Raspberry Pi ist als WiFi-Access-Point aufgesetzt auf dem eine python-basierte Webapplikation gehostet wird (Angular-Frontend mit CherryPy-Backend).
Das Smartphone greift via WiFi auf die Webapplikation zu und zeigt im Browser des Smartphones die Bedienoberfläche der Seilbahn an.
Steuerbefehle vom Smartphone (z.B. Start, Stopp) werden vom CherryPy-Backend via RPi Motor Driver Board an die Motoren weitergeleitet.

## Screenshots

![Screenshot](screenshots/screenshot-1.png)
