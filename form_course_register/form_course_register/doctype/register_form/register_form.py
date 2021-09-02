# Copyright (c) 2021, Z1 and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RegisterForm(Document):
	# def get_value(self):
	# 	c_name = frappe.db.get_value('Course List', 'Python', ['course_name'])
	# 	frappe.msgprint("hello")
	def before_save(self):
<<<<<<< HEAD
		# data_select = self.course_list
		data_select = self.course_list
		# frappe.msgprint(data_select)
		self.full_name = f'{self.first_name or ""} {self.last_name or ""}'
		data = frappe.db.sql(f"""SELECT 
									`course_price`,
									`course_name`
								FROM 
									`tabCourse List` 
								WHERE `name` = '{self.course_list}'
								""")
		self.course_price = data[0][0]
=======
		# data_select = str()
		data_select = self.course_list
		frappe.msgprint(data_select)
		self.full_name = f'{self.first_name or ""} {self.last_name or ""}'
		data = frappe.db.sql("""SELECT 
									`course_price` 
								FROM 
									`tabCourse List` 
								WHERE `name` = data_select
""")
		frappe.msgprint(data)
		# for d in data:
		# 	frappe.msgprint(d)
		# 	frappe.msgprint(self.course_list)
		# 	if self.course_list == d:
		# 		frappe.msgprint("hell")
		# 		c_price = frappe.db.sql("""SELECT
		# 										course_price
		# 								FROM
		# 								`tabCourse List`""", )
		# 		self.course_price = c_price
		# for c_name in self.course_list:
			# frappe.msgprint(c_name)
		# if self.course_list == "CL-001":
		# 	# frappe.msgprint("hello")
		# 	self.course_price = 500
		# elif self.course_list == "CL-002":
		# 	# frappe.msgprint("hello")
		# 	self.course_price = 450
		# elif self.course_list == "CL-003":
		# 	# frappe.msgprint("hello")
		# 	self.course_price = 400

>>>>>>> 222b6cdf9c0e954f221f5805a2c2ee90abd2504d
