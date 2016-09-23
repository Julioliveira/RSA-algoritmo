#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import math

def isPrime(number): 
  m = math.sqrt(number) 
  m = int(math.ceil(m)) 
  if (number % 2 == 0): 
    return False
  else:
    for x in range(3, m, 2): 
      if ((number % x) == 0):
        return False
  return True

def findP():
  p = random.randint(2,40000000000000) 
  while isPrime(p) == False: 
    p = random.randint(2,40000000000000)
  print p
  return p

def findQ(p):
  q = random.randint(2,40000000000000) 
  while isPrime(q) == False or p == q: #verifica se é primo e diferente de P, se não, gera outro
    q = random.randint(2,40000000000000)
  print q 
  return q

def findN(p,q): #descobre N usando P e Q
  n = p * q  
  return n

def findPhi(p, q): #descobre phi utilizando p e q
  phi = (p-1) * (q-1)
  #print "p " + str(p)
  #print "q " + str(q)
  #print "phi " + str(phi)
  return phi


def euclides(phi, e): #retorna o mdc utilizando Algoritmo de Euclides
  while e:
    phi, e = e, phi%e
  return phi

def findE(phi): 
  e = random.randint(2, phi-1) #gera E randômico 1 < E < phi
  while(euclides(phi,e) != 1): #chama o algoritmo de euclides para MDC e verifica se são primos entre si
    e = random.randint(2, phi-1) #se enquanto não forem primos entre si, gerar novo E
  #print "e " + str(e)
  return e

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi



def keys():
  p = findP()
  q = findQ(p)
  n = findN(p,q)
  phi = findPhi(p,q)
  e = findE(phi)
  d = multiplicative_inverse(e,phi)
  return ((e,n),(d,n))

def encrypt(pk, text):
  public, n = pk
  encrypted = [(pow(ord(char), public, n)) for char in text]
  return encrypted

def decrypt(pk, encrypted):
  privada, n = pk
  texto = ''
  decrypted = [chr((pow(char, privada, n))) for char in encrypted]

  return ''.join(decrypted)
public, private = keys()

enc = encrypt(public, 'hoje em dia todos correm')
print enc
print decrypt(private, enc)


