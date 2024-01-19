from django.contrib import admin

# Register your models here.
from .models import Watch
from .models import CartItem
admin.site.register(Watch)
admin.site.register(CartItem)
