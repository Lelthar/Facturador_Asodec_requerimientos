#!/usr/bin/env python
# -*- coding: utf-8 -*-
import usuario
import factura

class Facturador_asocec:
	'''
	-Especificacion: Esta funcion es el constructor de la clase Facturador_asodec
	-Entrada: No tiene entrada de parametros
	-Salida: No tiene salida
	'''
	def __init__(self):
		self.lista_usuarios = usuario.Usuario()

a = Facturador_asocec()
#a.lista_usuarios.agregar_usuario("lelthar19981","Lelthar","Morales","Alvarado","1234")
a.lista_usuarios.imprimir_usuarios()

