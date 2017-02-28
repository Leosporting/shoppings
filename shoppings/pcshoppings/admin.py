from django.contrib import admin


from .models import item,member,Category,comment

admin.site.register(member)
admin.site.register(item)
admin.site.register(Category)
admin.site.register(comment)
# Register your models here.
