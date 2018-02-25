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

	'''
	-Especificacion: Esta funcion es el menu de login del sistema
	-Entrada: No recibe entradas
	-Salida: No retorna nada
	'''
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
		elif(usuario_login.lower() == "administrador" and usuario_password.lower() == "administrador"):
			self.datos_usuario = "Administrador"
			self.menu_administrador()
		else:
			print("\nUsuario o contraseña incorrecta\n")
			self.menu_login()

	'''
	-Especificacion: Esta funcion es el menu para usuario
	-Entrada: No recibe entradas
	-Salida: No retorna nada
	'''
	def menu_facturacion(self):
		print('*****************************************************************************')
		print('*                            Menu                                           *')
		print('*                                                                           *')
		print('*               1. Agregar una factura                                      *')
		print('*               2. Ver facturas existentes                                  *')
		print('*               3. Eliminar una factura                                     *')
		print('*               4. Salir                                                    *')
		print('*                                                                           *')
		print('*****************************************************************************')
		print('')
		opcion_seleccionada = input("Digite el numero de la opcion que quiera: ")
		print('')
		if(opcion_seleccionada == "1"):
			self.agregar_datos_factura()
			self.menu_facturacion()
		elif(opcion_seleccionada == "2"):
			self.lista_facturas.imprimir_facturas()
			self.menu_facturacion()
		elif(opcion_seleccionada == "3"):
			numero_factura = int(input("Digite el numero de la factura que desea eliminar: "))
			self.lista_facturas.eliminar_factrura(numero_factura)
			self.menu_facturacion()
		elif(opcion_seleccionada == "4"):
			quit()
		else:
			print("ERROR: La opcion seleccionada no existe\n")
			self.menu_facturacion()
	
	'''
	-Especificacion: Esta funcion es el menu para el administrador
	-Entrada: No recibe entradas
	-Salida: No retorna nada
	'''
	def menu_administrador(self):
		print('*****************************************************************************')
		print('*                          Menu de administrador                            *')
		print('*                                                                           *')
		print('*               1. Agregar una factura                                      *')
		print('*               2. Ver facturas existentes                                  *')
		print('*               3. Eliminar una factura                                     *')
		print('*               4. Agregar un usuario                                       *')
		print('*               5. Ver usuarios existentes                                  *')
		print('*               6. Eliminar un usuario                                      *')
		print('*               7. Salir                                                    *')
		print('*                                                                           *')
		print('*****************************************************************************')
		print('')
		opcion_seleccionada = input("Digite el numero de la opcion que quiera: ")
		print('')
		if(opcion_seleccionada == "1"):
			self.agregar_datos_factura()
			self.menu_administrador()
		elif(opcion_seleccionada == "2"):
			self.lista_facturas.imprimir_facturas()
			self.menu_administrador()
		elif(opcion_seleccionada == "3"):
			numero_factura = int(input("Digite el numero de la factura que desea eliminar: "))
			self.lista_facturas.eliminar_factrura(numero_factura)
			self.menu_administrador()
		elif(opcion_seleccionada == "4"):
			nombre_usuario = input("Digite el nombre de usuario que sea (nick name): ")
			nombre = input("Digite el nombre del usuario: ")
			apellido1 = input("Digite el primer apellido del usuario: ")
			apellido2 = input("Digite el segundo apellido del usuario: ")
			contrasena = input("Digite la contraseña deseada: ")
			self.lista_usuarios.agregar_usuario(nombre_usuario.lower(),nombre,apellido1,apellido2,contrasena.lower())
			self.menu_administrador()
		elif(opcion_seleccionada == "5"):
			self.lista_usuarios.imprimir_usuarios()
			self.menu_administrador()
		elif(opcion_seleccionada == "6"):
			nombre_usuario_eliminar = input("Digite el nombre de usuario (nick name) que sea eliminar: ")
			self.lista_usuarios.eliminar_usuario(nombre_usuario_eliminar.lower())
			self.menu_administrador()
		elif(opcion_seleccionada == "7"):
			quit()
		else:
			print("ERROR: La opcion seleccionada no existe\n")
			self.menu_facturacion()

	'''
	-Especificacion: Esta funcion sirve para agregar los datos de una factura nueva
	-Entrada: No recibe entradas
	-Salida: No retorna nada
	'''
	def agregar_datos_factura(self):
		nombre_cliente = input("Digite el nombre del cliente: ")
		lista_lineas_factura = self.agregar_lineas_factura()
		total_vendido = self.obtener_total_factura(lista_lineas_factura)
		numero_factura = len(self.lista_facturas.facturas)
		self.lista_facturas.agregar_factura(numero_factura,self.datos_usuario,nombre_cliente,lista_lineas_factura,total_vendido)
		self.lista_facturas = factura.Factura()

	'''
	-Especificacion: Esta funcion sirve para agregar las lineas de una factura
	-Entrada: No recibe entradas
	-Salida: Retorna una lista con las lineas de una factura
	'''
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

	'''
	-Especificacion: Esta funcion sirve para obtener la cantidad total vendida en una factura
	-Entrada: Recibe la lista de lineas de la factura deseada
	-Salida: Retorna un numero entero, representando el total vendido en esa factura
	'''
	def obtener_total_factura(self,lista_lineas):
		total = 0
		for i in range(len(lista_lineas)):
			total += lista_lineas[i][4]
		return total

iniciacion_programa = Facturador_asodec()

