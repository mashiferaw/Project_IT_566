"""Implements application business logic."""
#from persistence_wrapper_interface import PersistenceWrapperInterface
from mysql_persistence_wrapper import MySQLPersistenceWrapper
import json

class BusinessLogic():
	"""Implements application business logic."""

	def __init__(self):
		"""Initialize object."""
		self._persistence_wrapper = MySQLPersistenceWrapper()
	

	def get_all_inventories(self):
		"""Returns a list of inventories."""
		query_results = None
		try:
			query_results = self._persistence_wrapper.get_all_inventories()
		except Exception as e:
			print(f'Exception in business logic: {e}')
		return query_results


	def get_all_inventories_with_format(self, format: str):
		"""Returns all inventories in requested format. 
		   Only supported format is JSON. Add others as required.
		"""
		query_results = None
		try:
			query_results = self._persistence_wrapper.get_all_inventories()
		except Exception as e:
			print(f'Exception in business logic: {e}')
		
		return_results = None
		try:
			match format:
				case 'json': return_results = json.dumps(query_results)
		except Exception as e:
			print(f'Exception in business logic: {e}')
		return return_results


	def create_new_inventory(self, name: str, description: str, date: str):
		"""Adds a new inventory to the datastore."""
		inventory_id = 0
		try:
			inventory_id = self._persistence_wrapper.create_inventory(name, description, date)
		except Exception as e:
			print(f'Exception in business logic: {e}')
		return inventory_id


	def get_items_for_inventory_id(self, id):
		"""Gets all items for given inventory id."""
		query_results = None
		try:
			query_results = self._persistence_wrapper.get_items_for_inventory(id)
			return query_results
		except Exception as e:
			print(f'Exception in business logic: {e}')
			results = ()
			return results
		

	def add_item_to_inventory(self, inventory_id: int, item: str, count: int): 
		try: 
			result = self._persistence_wrapper.create_item(inventory_id, item, count)
			return result
		except Exception as e: 
			print(f"Error in add_item_to_inventory: {e}")
			return None
