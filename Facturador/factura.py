import time

class Factura:
	def __init__():
		self.facturas = []

	'''
	-Especificacion: Esta funcion sirve para una nueva factura
	-Entrada: No tiene entrada de parametros
	-Salida: No tiene salida
	'''
	def agregar_factura(self,id_factura,nombre_usuario,nombre_cliente,lista_lineas):
		if(self.id_factura(id_factura) == False):
			print("Factura agregada")
			fecha = time.strftime("%d/%m/%Y %H:%M:%S")
			self.facturas.append([id_factura,nombre_usuario,fecha,nombre_cliente,lista_lineas])
			self.sobreescribir_archivo("facturas.txt",str(self.facturas))
		else:
			print("No se pudo agregar la factura")

	'''
	-Especificacion: Esta funcion sirve para cargar las facturas guardados en el .txt
	-Entrada: No tiene parametros
	-Salida: No tiene salida
	'''
	def cargar_facturas(self):
		facturas_archivo = self.leer_archivo("facturas.txt")
		if(facturas_archivo !=''):
			self.facturas = eval(facturas_archivo)
	'''
	-Especificacion: Esta funcion sirve para leer archivos
	-Entrada: Recibe el nombre del archivo
	-Salida: Devuelve el contenido del archivo
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
	def existe_factura(self,id_factura):
		for i in range(len(self.facturas)):
			if(self.facturas[i][0] == id_factura):
				return True
		return False