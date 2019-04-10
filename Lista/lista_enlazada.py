class Nodo:
	"""
	Modela un Nodo para la lista Enlazada con una operacion que permite
	representar al Nodo.
	"""
	def __init__(self, valor):
		"""Crea un nodo. El elemento recibido es un caracter.
		"""
		self.dato = valor
		self.proximo = None

class ListaEnlazada:
	"""
	Modela una ListaEnlazada con operaciones agregar, eliminar, insertar, iter y
	su representacion.
	"""
	def __init__(self):
		"""
		Crea un lista enlazada vacia.
		"""
		self.primero = None
		self.ultimo = None
		self.len = 0

	def largo(self):
		return self.len

	def esta_vacia(self):
		return not self.primero

	def insertar_primero(self, dato):
		nodo_nuevo = Nodo(dato)

		if not self.esta_vacia():
			nodo_nuevo.proximo = self.ver_primero

		else:
			self.ultimo = nodo_nuevo

		self.primero = nodo_nuevo
		self.len += 1

	def insertar_ultimo(self, dato):
		nodo_nuevo = Nodo(dato)

		if not self.esta_vacia():
			self.ultimo.proximo = nodo_nuevo
		else:
			self.primero = nodo_nuevo

		self.ultimo = nodo_nuevo
		self.len += 1

	def ver_primero(self):
		return None if self.esta_vacia() else self.primero.dato

	def ver_ultimo(self):
		return None if self.esta_vacia() else self.ultimo.dato

	def borrar_primero(self):

		if self.esta_vacia():
			return None

		nodo_actual = self.primero
		valor = nodo_actual.dato
		self.primero = nodo_actual.proximo

		if not self.primero:
			self.ultimo = None

		self.len -= 1
		return valor

	def slice(self, inicio, fin = 800000000):
		nuevo_fin = fin

		if fin > ( self.len -1 ):
			nuevo_fin = self.len - 1

		nueva = ListaEnlazada()
		principio = 0
		actual = self.primero

		while principio < inicio:
			actual = actual.proximo
			principio += 1

		while principio < nuevo_fin and actual:
			nueva.insertar_ultimo(actual.dato)
			actual = actual.proximo
			principio += 1

		if fin == ( self.len - 1 ):
			return nueva

		if nuevo_fin == ( self.len - 1) and actual:
			nueva.insertar_ultimo(actual.dato)

		return nueva

	def obtener(self, indice):

		if indice < 0 or indice > ( self.len - 1):
			raise IndexError("Indice fuera del rango de la lista")

		if indice == ( self.len - 1 ):
			return self.ver_ultimo()

		indice_actual = 0
		actual = self.primero

		while actual:

			if indice_actual == indice:
				return actual.dato

			actual = actual.proximo
			indice_actual += 1

	def __add__(self, otra):
		nueva = ListaEnlazada()
		actual = self.primero

		while actual:
			nueva.insertar_ultimo(actual.dato)
			actual = actual.proximo

		actual = otra.primero

		while actual:
			nueva.insertar_ultimo(actual.dato)
			actual = actual.proximo

		return nueva

	def __iter__(self):
		return IteradorLista(self.primero)

class IteradorLista:
	def __init__(self, primero):
		self.actual = primero

	def next(self):

		if not self.actual:
			raise StopIteration

		dato = self.actual.dato
		self.actual = self.actual.proximo
		return dato

	def __next__(self):
		return self.next()
