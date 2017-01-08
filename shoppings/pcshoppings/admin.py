from django.contrib import admin


from .models import item,member,Category

admin.site.register(member)
admin.site.register(item)
admin.site.register(Category)
# Register your models here.
