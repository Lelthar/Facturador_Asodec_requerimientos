#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Usuario:
	'''
	-Especificacion: Esta funcion es el constructor de la clase Usuario
	-Entrada: No tiene entrada de parametros
	-Salida: No tiene salida
	'''
	def __init__(self):
		self.usuarios = []  #Es la lista de usuarios del programa
		self.cargar_usuarios() #Esta funcion carga los datos de los usuarios
	
	'''
	-Especificacion: Esta funcion sirve para agregar los usuarios a la base de datos(Un txt)
	-Entrada: Recibe el nombre de usuario (nick_name el cual debe ser unico),nombre del usuario, el primer apellido, el segundo apellido y la contraseña para logearse
	-Salida: No tiene salida
	'''
	def agregar_usuario(self,nombre_usuario,nombre,apellido1,apellido2,contrasena):
		if(self.existe_usuario(nombre_usuario) == False):
			print("Usuario agregado")
			self.usuarios.append([nombre_usuario,nombre,apellido1,apellido2,contrasena])
			self.sobreescribir_archivo("usuarios.txt",str(self.usuarios))
			print("\nEl usuario de ha agregado\n")
		else:
			print("\nNo se pudo agregar al usuario\n")

	'''
	-Especificacion: Esta funcion sirve para cargar los usuarios guardados en el .txt
	-Entrada: No tiene parametros
	-Salida: No tiene salida
	'''
	def cargar_usuarios(self):
		usuarios_archivo  = self.leer_archivo("usuarios.txt")
		if(usuarios_archivo !=''):
			self.usuarios = eval(usuarios_archivo) #Convierte el string del archivo a una lista

	'''
	-Especificacion: Esta funcion sirve para leer un archivo
	-Entrada: Recibe el nombre del archivo que se desea leer
	-Salida: Retorna el contenido del archivo leido
	'''
	def leer_archivo(self,nombre_archivo):
		archivo = open(nombre_archivo, "r+")
		contenido = archivo.read ()
		archivo.close()
		return contenido

	'''
	-Especificacion: Esta funcion sirve para sobreescribir el archivo .txt donde se guardan los usuarios
	-Entrada: Recibe el nombre del archivo y el texto a guardar en el archivo
	-Salida: No tiene salida
	'''
	def sobreescribir_archivo(self,nombre_archivo, texto):
		archivo = open(nombre_archivo, "w+")
		archivo.seek (0,2)
		archivo.write(texto)
		archivo.close()

	'''
	-Especificacion: Esta funcion sirve para ver si un usuario existe en la lista de usuarios
	-Entrada: Recibe un string, el noombre del usuario
	-Salida: Retorna un valor booleano dependiendo si el usuario existe o no
	'''
	def existe_usuario(self,nombre_usuario):
		for i in range(len(self.usuarios)):
			if(self.usuarios[i][0] == nombre_usuario):
				return True
		return False
	'''
	-Especificacion: Esta funcion sirve para ver si un usuario existe en la lista de usuarios
	-Entrada: Recibe un string, el noombre del usuario
	-Salida: Retorna un valor booleano dependiendo si el usuario existe o no
	'''
	def existe_usuario_y_contraseña(self,nombre_usuario,contrasena_usuario):
		for i in range(len(self.usuarios)):
			if(self.usuarios[i][0] == nombre_usuario and self.usuarios[i][4] == contrasena_usuario):
				return True
		return False
		
	'''
	-Especificacion: Imprimir lista usuarios
	-Entrada: No recibe entrada de parametros
	-Salida: No tiene salida
	'''
	def imprimir_usuarios(self):
		for i in range(len(self.usuarios)):
			print("")
			string_imprimir = "Nombre de usuario: "+self.usuarios[i][0]+"\nNombre: "+self.usuarios[i][1]+"\nApellidos: "+self.usuarios[i][2]+" "+self.usuarios[i][3]+"\nContraseña: "+self.usuarios[i][4]
			print(string_imprimir)
		print("")

	'''
	-Especificacion: Esta funcion sirve para obtener los datos del usuario seleccionado
	-Entrada: Recibe un string, el nombre de usuario
	-Salida: Retorna un string, los datos del usuario seleccionado
	'''
	def obtener_datos_usuario(self,nombre_usuario):
		for i in range(len(self.usuarios)):
			if(self.usuarios[i][0] == nombre_usuario):
				datos = self.usuarios[i][1]+" "+self.usuarios[i][2]+" "+self.usuarios[i][3]
				return datos
		return ""

	'''
	-Especificacion: Esta funcion sirve para eliminar un usuario
	-Entrada: Recibe un string, el nombre de usuario
	-Salida: No retorna nada
	'''
	def eliminar_usuario(self,nombre_usuario):
		for i in range(len(self.usuarios)):
			if(self.usuarios[i][0] == nombre_usuario):
				self.usuarios.pop(i)
				self.sobreescribir_archivo("usuarios.txt",str(self.usuarios))
				print("\nEl usuario ha sido eliminado\n")
				break
