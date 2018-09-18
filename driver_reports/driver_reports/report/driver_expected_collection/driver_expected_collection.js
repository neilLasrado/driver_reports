// Copyright (c) 2016, Neil Lasrado and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Driver Expected Collection"] = {
	"filters": [
		{
			"fieldname": "Date",
			"label": __("Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today(),
			"reqd": 1
		},
		{
			"fieldname": "Driver",
			"label": __("Driver"),
			"fieldtype": "Link",
			"options": "Driver"
		}
	]
}
