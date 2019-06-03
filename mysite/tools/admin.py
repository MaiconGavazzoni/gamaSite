from django.contrib import admin

from .models import TypeItem, Item

class ItemAdmin(admin.ModelAdmin):

    list_display = ['type', 'stock_code', 'name', 'diameter', 'cutterLength']

admin.site.register(TypeItem)
admin.site.register(Item, ItemAdmin) #Model + classe personalisada para apresentar no admin