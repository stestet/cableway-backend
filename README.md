# Cableway Toy Project

## Einführung / Intro

Das ist das Bastelprojekt für meinen Sohn bei dem es um die Fernsteuerung seiner Holzspielzeug-Seilbahn geht.
Die Holzspielzeug-Seilbahn hat 2 Kabinen bei welchen das Zugseil 'bergseitig' via 2 Rollen umgelenkt wird.
Via dieser Rollen kann die Seilbahn manuell angetrieben werden. Eine dieser Rolle wird neu durch ein Gleichstrommotor-getriebenes Exemplar ersetzt.

This is the tinkering project for my son which is about the remote control of his wooden toy cableway.
The wooden toy cableway has 2 cabins with which the pull cable is deflected 'uphill' via 2 pulleys.
The cableway can be driven manually via these pulleys. One of these pulleys is now replaced by a DC motor-driven model.

Was braucht's / What's it take:

- Holzspielzeug-Seilbahn / Wooden toy cableway
- [Getriebemotor mit Rad](https://www.reichelt.de/getriebemotor-mit-rad-3-9-v-welle-3-5-mm-com-motor-rad-p219038.html) / [DC motor with wheel](https://www.reichelt.de/getriebemotor-mit-rad-3-9-v-welle-3-5-mm-com-motor-rad-p219038.html)
- Raspberry Pi Model 3 B
- [RPi Motor Driver Board](https://www.waveshare.com/rpi-motor-driver-board.htm)
- [Powerbank](https://www.manualslib.com/manual/1192439/Tecxus-Tp-10000.html)
- altes Smartphone / old Smartphone

## Lösungsansatz / Solution approach

Der Raspberry Pi ist als WiFi-Access-Point aufgesetzt auf dem eine python-basierte Webapplikation gehostet wird (Angular-Frontend mit CherryPy-Backend).
Das Smartphone greift via WiFi auf die Webapplikation zu und zeigt im Browser des Smartphones die Bedienoberfläche der Seilbahn an.
Steuerbefehle vom Smartphone (z.B. Start, Stopp) werden vom CherryPy-Backend via RPi Motor Driver Board an den Motor weitergeleitet.
Die Motor-Bewegungen (links/rechts) sind zeitlich (5s) beschränkt, sprich nach dieser Zeit hört der Motor auf sich zu drehen. Dabei geht es darum, Motorbeschädigungen (z.B. durch Überhitzen) bei Fehlbedienung zu verhindern.

The Raspberry Pi is set up as a WiFi access point on which a python-based web application is hosted (angular frontend with CherryPy backend).
The smartphone accesses the web application via WiFi and displays the user interface of the cable way in the smartphone's browser.
Control commands from the smartphone (e.g. start, stop) are forwarded from the CherryPy backend to the motor via the RPi Motor Driver Board.
The motor movements (left/right) are limited in time (5s), i.e. after this time the motor stops turning. The aim is to prevent motor damage (e.g. due to overheating) due to operating errors.

![Solution](/screenshots/solution-blocks.PNG)


## Screenshots

![Screenshot 1](/screenshots/screenshot-1.PNG)
![Screenshot 2](/screenshots/screenshot-2.PNG)

## Impressionen / Impressions

![Impression 1](/screenshots/impression-1.jpg)
![Impression 2](/screenshots/impression-2.jpg)
![Impression 3](/screenshots/impression-4.jpg)
![Impression 4](/screenshots/impression-3.jpg)