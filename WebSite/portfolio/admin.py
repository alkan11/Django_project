from cProfile import Profile
from django.contrib import admin
from .models import Home,About,Portfolio,profile,Category,Skills

admin.site.register(Home)

class Profileline(admin.TabularInline):
    models=profile
    extra=1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inline=[Profileline,]

class Skilline(admin.TabularInline):
    models=Skills
    extra=2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inline=[Skilline,]

admin.site.register(Portfolio)