import time

class Factura:
	def __init__(self):
		self.facturas = []
		self.cargar_facturas()

	'''
	-Especificacion: Esta funcion sirve para una nueva factura
	-Entrada: No tiene entrada de parametros
	-Salida: No tiene salida
	'''
	def agregar_factura(self,id_factura_cantidad,nombre_usuario,nombre_cliente,lista_lineas,total):
		if(self.existe_factura(id_factura_cantidad) == False):
			fecha = time.strftime("%d/%m/%Y %H:%M:%S")
			self.facturas.append([id_factura_cantidad,nombre_usuario,fecha,nombre_cliente,lista_lineas,total])
			self.sobreescribir_archivo("facturas.txt",str(self.facturas))
			print("\nFactura agregada\n")
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
	-Especificacion: Esta funcion sirve para ver si una factura existe en la lista de facturas
	-Entrada: Recibe un int, el numero de la factura
	-Salida: Retorna un valor booleano dependiendo si la factura existe o no
	'''
	def existe_factura(self,id_factura):
		for i in range(len(self.facturas)):
			if(self.facturas[i][0] == id_factura):
				return True
		return False

	'''
	-Especificacion: Esta funcion sirve para imprimir de una forma ordenada, los datos las facturas existentes
	-Entrada: No recibe parametros
	-Salida: No retorna nada
	'''
	def imprimir_facturas(self):
		for i in range(len(self.facturas)):
			print('*****************************************************************************')
			print('\tNumero de la factura: '+str(self.facturas[i][0]))
			print('\tNombre del vendedor: '+self.facturas[i][1])
			print('\tNombre del comprador: '+self.facturas[i][3])
			print('\tFecha de la compra: '+self.facturas[i][2])
			for j in range(len(self.facturas[i][4])):
				print("\tNumero de linea de factura: "+str(self.facturas[i][4][j][0])+"\tProducto: "+self.facturas[i][4][j][1]+"\tDescripcion: "+self.facturas[i][4][j][2]+"\tCantidad: "+str(self.facturas[i][4][j][3])+"\tPrecio: "+str(self.facturas[i][4][j][4]))
			print("\tTOTAL: "+str(self.facturas[i][5]))
	
	'''
	-Especificacion: Esta funcion sirve para eliminar la factura seleccionada
	-Entrada: Recibe un int, el numero de la factura a eliminar
	-Salida: No retorna nada
	'''
	def eliminar_factrura(self,numero_factura):
		for i in range(len(self.facturas)):
			if(self.facturas[i][0] == numero_factura):
				self.facturas.pop(numero_factura)
				for i in range(len(self.facturas)):
					self.facturas[i][0] = i
				self.sobreescribir_archivo("facturas.txt",str(self.facturas))
				print("\nLa factura fue eliminada\n")
				break

