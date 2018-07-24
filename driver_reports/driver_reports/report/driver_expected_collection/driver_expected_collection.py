# Copyright (c) 2013, Neil Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import flt

def execute(filters=None):
	if not filters: filters = frappe._dict()
	columns= ["Delivery Note:Link/Delivery Note:150", "Customer Name", "Amount:Currency/currency:140"]
	data = get_for_driver(filters.get("Date"), filters.get("Driver"))
	return columns, data

def get_for_driver(date, driver):
	row = []
	delivery_notes = []
	total = 0
	for dt in frappe.get_all("Delivery Trip", filters={"date": date, "driver": driver, "docstatus":1}):
		delivery_trip = frappe.get_doc("Delivery Trip", dt.name)
		for item in delivery_trip.delivery_stops:
			if item.delivery_note not in delivery_notes:
				delivery_notes.append(item.delivery_note)
	for dn in delivery_notes:
		amount = flt(frappe.db.get_value("Delivery Note", dn, "grand_total"))
		row.append([dn, frappe.db.get_value("Delivery Note", dn, "Customer") ,amount])
		total+= amount
	row.append(["", "TOTAL AMOUNT", total])
	return row