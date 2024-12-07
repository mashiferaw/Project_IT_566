"""Implements a MySQL Persistence Wrapper"""

from mysql.connector import connect, Error
from persistence_wrapper_interface import PersistenceWrapperInterface
from mysql import connector

class MySQLPersistenceWrapper(PersistenceWrapperInterface):
	"""Implements MySQL Persistance Wrapper"""

	def __init__(self):
		"""Initializes """
		# Constants
		self.SELECT_ALL_INVENTORIES = 'SELECT id, name, description FROM inventories'
		self.INSERT = 'INSERT INTO items (inventory_id, item, count) VALUES(%s, %s, %s)'
		self.SELECT_ALL_ITEMS_FOR_INVENTORY_ID = 'SELECT id, inventory_id, item, count FROM items WHERE inventory_id = %s'

		# Database Configuration Constants
		self.DB_CONFIG = {}
		self.DB_CONFIG['database'] = 'home_inventory'
		self.DB_CONFIG['user'] = 'home_inventory_user'
		self.DB_CONFIG['host'] = '127.0.0.1'
		self.DB_CONFIG['port'] = 8889 

		# Database Connection
		self._db_connection = self._initialize_database_connection(self.DB_CONFIG)
		print(f"DEBUG: Connection: {self._db_connection}, Cursor: {self.cursor}")
	
	def _initialize_database_connection(self):
		try: 
			print("Attempting to connect to the database...")
			self._db_connection = connect(**self.DB_CONFIG)
			self.cursor = self._db_connection.cursor(dictionary=True)
			print("Database connection established.")
		except Error as e: 
			print(f'Database connection error: {e}')
			self._db_connection = None
			self.cursor = None

	def get_all_inventories(self):
		"""Returns a list of all rows in the inventories table"""
		cursor = None
		try:
			cursor = self._db_connection.cursor()
			cursor.execute(self.SELECT_ALL_INVENTORIES)
			results = cursor.fetchall()
		except Exception as e:
			print(f'Exception in persistance wrapper: {e}')
		return results


	def get_items_for_inventory(self, inventory_id):
		"""Returns a list of all items for given inventory id"""
		cursor = None
		try:
			cursor = self._db_connection.cursor()
			cursor.execute(self.SELECT_ALL_ITEMS_FOR_INVENTORY_ID, ([inventory_id]))
			results = cursor.fetchall()
		except Exception as e:
			print(f'Exception in persistance wrapper: {e}')
		return results


	def create_inventory(self, name: str, description: str, date: str):
		"""Insert new row into inventories table."""
		try:
			query = "INSERT INTO inventory (inventory_id, item, count) VALUES (%s, %s, %s)"
			self.cursor.execute(query, (name, description, date))
			self.connection.commit()
			return self.cursor.lastrowid
		except Exception as e:
			print(f'Error: {e}')


	def create_item(self, inventory_id: int, item: str, count: int):
		"""Insert new row into items table for given inventory id"""
		try:
			if not inventory_id: 
				print('Error: inventory_id is none or invalid. ')
				return None 
			
			query = "INSERT INTO items (inventory_id, item, count) VALUES (%s, %s, %s)"
			self.cursor.execute(query, (inventory_id, item, count))
			self.connection.commit()
			return self.cursor.lastrowid
		except Exception as e:
			print(f'Error: {e}')
		
		
	def _initialize_database_connection(self, config):
		"""Initializes and returns database connection pool."""
		cnx = None
		try:
			cnx = connector.connect(pool_name = 'dbpool', pool_size=10, **config)
		except Exception as e:
			print(e)
		return cnx



