import os
import psycopg2
import urlparse

# Best wrapper alive!
class DBConnect(object):
	"""Small wrapper to connect and query remote PostgreSQL db"""
	
	def __init__(self):
		urlparse.uses_netloc.append("postgres")
		url = urlparse.urlparse(os.environ["DATABASE_URL"])
		self.conn = psycopg2.connect(
		    database=url.path[1:],
		    user=url.username,
		    password=url.password,
		    host=url.hostname,
		    port=url.port
		)

	# General psycopg2 'execute' Wrapper
	def execute(self, *args):
		if hasattr(self, 'cur'):
			del self.cur

		self.cur = self.conn.cursor()
		self.cur.execute(*args)
		self.conn.commit()

		return self.cur

	# 'Select' wrapper returning formatted results
	def query(self, *args):
		cur = self.execute(*args)

		try:
			result = cur.fetchall()
		except:
			result = []

		return self._format_results(result)

	# Formats result list, pairing column names with data for each row
	def _format_results(self, result):
		result_arr = []
		fields = [column.name for column in self.cur.description]
		
		for row in result:
			row_dict = dict(zip(fields, row))
			result_arr.append(row_dict)

		return result_arr

	# Close DB connection
	def close(self):
		if hasattr(self, 'cur'):
			del self.cur

		self.conn.close()
