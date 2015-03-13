	+------------------------------------------+
	| OPTIMERING OCH TESTNING AV MASKINLÄRNING |
	+------------------------------------------+

 TESTER 
---------------
I denna mapp finns fyra olika sessioner uppmätt data från en IMU 9DOF
(https://www.sparkfun.com/products/10736).

I test 1-3 fästes IMU:n på en hjullastares bom. Data samlades in då
hjullastaren skottade snö på olika körningssätt. 

	- I test1.txt så gick viss data förlorad eftersom strömningen
		bröts mitt under körning, kan vara intressant att ha kvar(?).
	
	- I test2.txt körde hjullastaren hårt in i snöhögen och hackade
		sig fram relativt våldsamt för att se hur IMU:n skulle
		reagera på aggressiv körning.
	
	- I test3.txt körde hjullastaren lösare och lite mer försiktigt än
		i test2 för att se om det blev någon skillnad i vibrationer.

Det genomfördes även ett test på en liten högtalare, sine.txt. IMU:n riggades
på en liten högtalare som hade en stav ut från membranet som vibrerade
efter en kvadratisk sinuskurva på 5V och 5Hz.



SCRIPT
---------------
I denna mapp finns det två script. Den ena är för insamling av data, dvs, den
lyssnar på angiven port och skriver över detta i en txt fil, data.txt.
Det andra scriptet filtrerar och paketerar datat för önskad parameter,
accelerometer, gyro eller magnetometer. Dessa har då alla x-,y- och z-led.

För mer info se de enskilda scripten.



DEMO
---------------
För att samla in data används gtkterm, därifrån går man  in i
Cofiguration > Port och väljer vilken port, i de flesta fall USB0,
och Baud Rate(dvs hastighet på utskrift). Detta väljs automatiskt om man kör
scriptet "create_signal.sh". Scriptet anger även vilken fil man ska spara det
avlyssnade datat till, i detta fall "data.txt".

Filtrering sker genom att köra scriptet "filter.py". Den tar en fil,
"data.txt", och filtrerar ut lämplig parameter, som finns hänvisat längst
upp i scriptet, och skriver sedan över det till en ny fil, "filter_file".



För frågor:
---------------
Niklas Lundborg		lunnik-2@student.ltu.se
Kamal Al-Kawhati	kamalk-2@student.ltu.se
