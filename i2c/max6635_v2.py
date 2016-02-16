import smbus
import time

bus = smbus.SMBus(1)
address = 0x48
intervallo_lettura = 0.2
risoluzione_sensore = 0.0625

get_bin = lambda x, n: format(x, 'b').zfill(n)

def Get_Dati():
	#datilettura = 0b0
	try:		
		datilettura = bus.read_word_data(address, 0x0)
		datilettura = rotateWord(datilettura)
	except IOError, err:
		print "Errore: ", err
	return datilettura
	
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
	
def Complementoa2(dati):
	try:
		#newdata = (dati ^ 0xffff)
		newdata = (dati ^ 0xfff8)
	except IOError, err:
		print "Errore: ", err		
	return newdata
			
def rotateWord(tempW):
	#Sposta il byte MSB al posto del LSB e viceversa
	LSBW1 = (tempW & 0b0000000011111111) << 8
	MSBW1 = (tempW & 0b1111111100000000) >> 8
	rotateW = MSBW1 | LSBW1
	return rotateW	
			
def manipola(dati):
	dati_1 = dati >> 3
	#dati_2 = Complementoa2(dati_1)	
	return dati_1

while True:
	dati = Get_Dati()			
	dati_3= manipola(dati) * risoluzione_sensore
	print 'DATI1:', get_bin(dati,16), "- Temp:" , get_bin(manipola(dati),16), " - TEMP 'C= %3.4f" % dati_3
	#get_bin(Complementoa2(dati),16)
	time.sleep(1)
