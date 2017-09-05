# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "insider_frappe"
app_title = "Insider Frappe"
app_publisher = "MN Technique"
app_description = "Customization for Insider.in"
app_icon = "fa fa-calendar"
app_color = "purple"
app_email = "support@mntechnique.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/insider_frappe/css/insider_frappe.css"
# app_include_js = "/assets/insider_frappe/js/insider_frappe.js"

# include js, css files in header of web template
# web_include_css = "/assets/insider_frappe/css/insider_frappe.css"
# web_include_js = "/assets/insider_frappe/js/insider_frappe.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "insider_frappe.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "insider_frappe.install.before_install"
# after_install = "insider_frappe.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "insider_frappe.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"insider_frappe.tasks.all"
# 	],
# 	"daily": [
# 		"insider_frappe.tasks.daily"
# 	],
# 	"hourly": [
# 		"insider_frappe.tasks.hourly"
# 	],
# 	"weekly": [
# 		"insider_frappe.tasks.weekly"
# 	]
# 	"monthly": [
# 		"insider_frappe.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "insider_frappe.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "insider_frappe.event.get_events"
# }

