from django.contrib import admin

# Register your models here.
from .models import Snake
from .models import Feeding
from .models import Toy
admin.site.register(Snake)
admin.site.register(Toy)
# register the new Feeding Model
admin.site.register(Feeding)