from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Presents)
admin.site.register(SalesOrder)
admin.site.register(OrderDetail)



