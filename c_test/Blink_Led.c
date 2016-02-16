/*
 * Blink_Led.c
 *
 * Copyright 2016 Giuseppe R. <gronzuladm@OTOLS002>
 *
 * TEST MODIFICA
 */


#include <stdio.h>
#include <wiringPi.h>

// LED Pin - wiringPi pin 5 is BCM_GPIO 24.
#define LED     5


int main(int argc, char **argv)
{
	printf ("Raspberry Pi - Gertboard Blink\n") ;
	wiringPiSetup () ;
	printf ("Raspberry Pi - wiringPiSetup\nCOMPLETE!\n") ;
	pinMode (LED, OUTPUT) ;
	for (;;)
	{
		digitalWrite (LED, 1) ;
		printf ("on\n");
		delay (500) ;
		digitalWrite (LED,  0) ;
		printf ("off\n");
		delay (500) ;
	}
	return 0;
}
