// Copyright (c) 2017, MN Technique and contributors
// For license information, please see license.txt

frappe.ui.form.on('Event Commission', {
	refresh: function(frm, cdt, cdn) {
		//All Link Fields with ERPNext Connector Doctypes
		$.each(frm.fields_dict, function(fieldname, field ){
			if (field.df.fieldtype == "Link" && (field.df.options.indexOf("ERPNext ") == 0)){
				frm.set_query(fieldname, function(){
					return {
						query:"erpnext_connector.api.upstream_doc_query"
					}
				});
			}
		});

		// Specific Field with query (upstream)
		frm.set_query("company", function(){
			return {
				query:"erpnext_connector.api.upstream_doc_query",
				filters:[["abbr", "=","TC"]]
			}
		});

		// Child level item
		frm.set_query("item_code", "items", function(){
			return {
				query:"erpnext_connector.api.upstream_doc_query"
			}
		});
	}
});
