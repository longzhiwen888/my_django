from django.contrib import admin, auth

admin.default_app_config = 'inventory.admin.AdminConfig'
auth.default_app_config = 'inventory.admin.AuthConfig'
default_app_config = 'inventory.admin.InventoryConfig'