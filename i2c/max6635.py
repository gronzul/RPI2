import smbus
import time

bus = smbus.SMBus(1)
address = 0b1001000
intervallo_lettura = 0.2
risoluzione_sensore = 0.0625

get_bin = lambda x, n: format(x, 'b').zfill(n)

def Get_Dati():
	datilettura = 0b0
	try:		
		datilettura = bus.read_word_data(address, 0)					
	except IOError, err:
		print "Errore: ", err
	return datilettura
	
def rotateWord(tempW):
	#Sposta il byte MSB al posto del LSB e viceversa
	LSBW1 = (tempW & 0b0000000011111111) << 8
	MSBW1 = (tempW & 0b1111111100000000) >> 8
	rotateW = MSBW1 | LSBW1
	return rotateW	
	
def Get_Segno(dati):		
	try:
		SignBit = dati & 0x8000		
		if SignBit > 0:
			Segno = "-"
		else:
			Segno = "+"	
	except IOError, err:
		print "Errore: ", err	
	return Segno
	
	
def Get_ConfigurationByte():	
	dati =  bus.read_byte_data(address,1)	
	dati1  = rotateWord(dati)
	return dati1
	
def main(args):	
	dati = Get_ConfigurationByte()
	print "****************************"
	print "Configurazione" , bin(dati)
	print "****************************"
	
	while True:
		dati = Get_Dati()	
		dati1  = rotateWord(dati)
		dati2 =(dati1 >>3) 	
		Lettura = dati2 * risoluzione_sensore
		print "Lettura: %3.4f 'C" % Lettura		
		
		"""if Get_Segno(dati)== "-":
			T = Cmp2(dati) * risoluzione_sensore
		else:
			T = dati * 0.625
		
		print 'Temperatura: -', T , " --- " , bin(dati)		
		"""
		time.sleep(intervallo_lettura)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
	
