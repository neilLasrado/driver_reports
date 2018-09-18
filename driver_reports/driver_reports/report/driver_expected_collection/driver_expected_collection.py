# Copyright (c) 2013, Neil Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import flt

def execute(filters=None):
	if not filters: filters = frappe._dict()
	columns, data = [], []
	if filters.get("Driver"):
		columns= ["Delivery Note:Link/Delivery Note:150", "Customer Name", "Amount:Currency/currency:140"]
		data = get_for_driver(filters.get("Date"), filters.get("Driver"))
	else:
		columns= ["Delivery Trip:Link/Delivery Trip:150", "Driver", "Driver Name", "Amount:Currency/currency:140"]
		data = get_all_drivers(filters.get("Date"))
	return columns, data

def get_for_driver(date, driver):
	row = []
	total = 0
	for dt in frappe.db.sql("select name from `tabDelivery Trip` where DATE(departure_time)=%s and driver= %s and docstatus= 1", (date,driver), as_dict=True):
		delivery_trip = frappe.get_doc("Delivery Trip", dt.name)
		for item in delivery_trip.delivery_stops:
			amount = flt(item.grand_total)
			row.append([item.delivery_note, item.customer, amount])
			total+= amount
	row.append(["", "TOTAL AMOUNT", total])
	return row

def get_all_drivers(date):
	row = []
	for driver in frappe.get_all("Driver"):
		for dt in frappe.db.sql("select name from `tabDelivery Trip` where DATE(departure_time)=%s and driver= %s and docstatus= 1", (date,driver.name), as_dict=True):
			delivery_trip = frappe.get_doc("Delivery Trip", dt.name)
			total = 0
			for item in delivery_trip.delivery_stops:
				amount = flt(item.grand_total)
				total+= amount
			row.append([delivery_trip.name, delivery_trip.driver, delivery_trip.driver_name, total])
	return row
	
