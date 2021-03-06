#!/usr/bin/python

#Covered by GPL V2.0

from encoders import *
from payloads import *

# generate_dictio evolution		
class dictionary:
	def __init__(self,dicc=None):
		if dicc:
			self.__payload=dicc.getpayload()
			self.__encoder=dicc.getencoder()
		else:	
			self.__payload=payload()
			self.__encoder = [lambda x: encoder().encode(x)]
		self.restart()

	def count (self):
		return self.__payload.count() * len(self.__encoder)

	def setpayload(self,payl):
		self.__payload = payl
		self.restart()

	def setencoder(self,encd):
		self.__encoder=encd
		self.generator = self.gen()

	def getpayload (self):
		return self.__payload
	
	def getencoder (self):
		return self.__encoder

	def generate_all(self):
		dicc=[]
		for i in self.__payload:
			dicc.append(self.__encoder.encode(i))
		return dicc

	def __iter__(self):
		self.restart()
		return self

	def gen(self):
	    while 1:
		pl=self.iter.next()
		for encode in self.__encoder:
		    yield encode(pl)

	def next(self):
		return self.generator.next()

	def restart(self):
		self.iter=self.__payload.__iter__()
		self.generator = self.gen()

