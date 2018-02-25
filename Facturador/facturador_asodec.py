#!/usr/bin/env python
# -*- coding: utf-8 -*-
import usuario
import factura

class Facturador_asodec:
	'''
	-Especificacion: Esta funcion es el constructor de la clase Facturador_asodec
	-Entrada: No tiene entrada de parametros
	-Salida: No tiene salida
	'''
	def __init__(self):
		self.lista_usuarios = usuario.Usuario()
		self.lista_facturas = factura.Factura()
		#print(self.lista_facturas.facturas)
		self.datos_usuario = ""
		self.menu_login()

	def menu_login(self):
		print('*****************************************************************************')
		print('*                            Login                                          *')
		print('*                                                                           *')
		print('*               1. Se le solicitara su nombre de usuario                    *')
		print('*               2. Se le solicitara su contraseña                           *')
		print('*                                                                           *')
		print('*****************************************************************************')
		print('')
		usuario_login = input("Digite su nombre de usuario: ")
		usuario_password = input("Digite su contraseña: ")
		if(self.lista_usuarios.existe_usuario_y_contraseña(usuario_login.lower(),usuario_password.lower())):
			print("")
			self.datos_usuario = self.lista_usuarios.obtener_datos_usuario(usuario_login.lower())
			self.menu_facturacion()
		else:
			print("\nUsuario o contraseña incorrecta\n")
			self.menu_login()

	def menu_facturacion(self):
		print('*****************************************************************************')
		print('*                            Menu                                           *')
		print('*                                                                           *')
		print('*               1. Agregar una factura                                      *')
		print('*               2. Ver facturas existentes                                  *')
		print('*               3. Eliminar factura                                         *')
		print('*               4. Salir                                                    *')
		print('*                                                                           *')
		print('*****************************************************************************')
		print('')
		opcion_seleccionada = input("Digite el numero de la opcion que quiera: ")
		print('')
		if(opcion_seleccionada == "1"):
			self.agregar_datos_factura()
		elif(opcion_seleccionada == "2"):
			self.lista_facturas.imprimir_facturas()
			self.menu_facturacion()
		elif(opcion_seleccionada == "3"):
			print("Opcion3")
		elif(opcion_seleccionada == "4"):
			quit()
		else:
			print("ERROR: La opcion seleccionada no existe\n")
			self.menu_facturacion()
	
	def agregar_datos_factura(self):
		nombre_cliente = input("Digite el nombre del cliente: ")
		lista_lineas_factura = self.agregar_lineas_factura()
		total_vendido = self.obtener_total_factura(lista_lineas_factura)
		numero_factura = len(self.lista_facturas.facturas)
		self.lista_facturas.agregar_factura(numero_factura,self.datos_usuario,nombre_cliente,lista_lineas_factura,total_vendido)
		self.lista_facturas = factura.Factura()
		self.menu_facturacion()
		


	def agregar_lineas_factura(self):
		lineas_factura = []
		lista_datos = []
		contador_lineas = 0

		while(True):
			lista_datos.append(contador_lineas)
			nombre_producto = input("Inserte el nombre del producto: ")
			descripcion = input("Inserte la descripcion del producto: ")
			cantidad = input("Inserte la cantidad de unidades: ")
			precio_vendido = input("Inserte el precio del total vendido de este producto: ")
			lista_datos.append(nombre_producto)
			lista_datos.append(descripcion)
			lista_datos.append(cantidad)
			lista_datos.append(int(precio_vendido))
			lineas_factura.append(lista_datos)
			lista_datos = []
			agregar_lineas = input("¿Desea agregar otro producto?(Si/No): ")
			if(agregar_lineas.lower() == "si"):
				contador_lineas+=1
				continue
			elif(agregar_lineas.lower() == "no"):				
				break
		return lineas_factura
	def obtener_total_factura(self,lista_lineas):
		total = 0
		for i in range(len(lista_lineas)):
			total += lista_lineas[i][4]
		return total

a = Facturador_asodec()
#a.lista_usuarios.agregar_usuario("lelthar19981","Lelthar","Morales","Alvarado","1234")
#a.lista_usuarios.imprimir_usuarios()

