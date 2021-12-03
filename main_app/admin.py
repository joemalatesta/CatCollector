from django.contrib import admin

# Register your models here.
from .models import Cat, Feeding, Toy, Photo

admin.site.register(Cat)
admin.site.register(Feeding)
admin.site.register(Toy)
admin.site.register(Photo)
