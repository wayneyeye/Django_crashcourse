#_*_ encoding:utf-8 _*_
from django.contrib import admin
from mysite import models

class ProductAdmin(admin.ModelAdmin):
	list_display=('pmodel', 'nickname', 'price', 'year')
	#list_display=('pmodel',  'price', 'year')
	search_fields=('nickname',)
	ordering = ('-price', )

admin.site.register(models.Product, ProductAdmin)

admin.site.register(models.Maker)
admin.site.register(models.PModel)
admin.site.register(models.PPhoto)
