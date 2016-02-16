// Rapsberry Pi: I2C in C - Versione 0.61 - Luglio 2013
// Copyright (c) 2013, Vincenzo Villa (http://www.vincenzov.net)
// Creative Commons | Attribuzione-Condividi allo stesso modo 3.0 Unported.
// Creative Commons | Attribution-Share Alike 3.0 Unported
// http://www.vincenzov.net/tutorial/elettronica-di-base/RaspberryPi/i2c-c.htm

// Compile:  cc -o i2ctest2_2 i2c_test2.c

// Run as user with R&W right on /dev/i2c-* (NOT ROOT!)
// vv@vvrpi ~ $ ./i2ctest2_2 
// Using MAX6635 - I2C 

#include <stdint.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <getopt.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <linux/types.h>
#include <linux/i2c-dev.h>
#include <stdlib.h>

#define I2C_ADDR 0x48				// Device adress
#define MAX6635_RES 0.0625          // Resolution (see data sheet)

static const char *device = "/dev/i2c-1";	// I2C bus

static void exit_on_error (const char *s)	// Exit and print error code
{ 	perror(s);
  	abort();
} 

int main(int argc, char *argv[])
{
	leggitemp();	
	/*while(1)
	{		
		sleep(1);
	}
	*/
}

int leggitemp()
{
	int fd;
	int end; 
	char temp;	
	uint8_t  buffer[2];
	int16_t  data;
	double   temperature;
	
	
	// Open I2C device
	if ((fd = open(device, O_RDWR)) < 0) exit_on_error ("Can't open I2C device");

	// Set I2C slave address
	if (ioctl(fd, I2C_SLAVE,I2C_ADDR) < 0) exit_on_error ("Can't talk to slave");
	
		// Read from MAX6635 (from Power-up default register)      
		printf("Reading from MAX6635 at address 0x%.2X on %s\n", I2C_ADDR, device);

	while(1)
	{
	
		if (read(fd,buffer,2) != 2) exit_on_error ("Failed to read from the i2c bus");  
		// printf("Data read from Power-up default register: 0x%.2X%.2X\n", buffer[0], buffer[1],buffer[2]);
		
		data =  buffer[0];
		data = data << 8;
		
		data = data | buffer[1];
		data = data >> 3;
		temperature = MAX6635_RES * data;        
		
		printf("Temperatura: %2.1f °C\n", temperature);        	
		// end = scanf ("%c", &temp); 
		// printf("Premuto: ", end);
		sleep(1);
	}                
	close(fd);
	return (0);
}
