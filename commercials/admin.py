from django.contrib import admin

# Register your models here.
from commercials.models import Label, Unit, Nutrient



class NutrientInline(admin.StackedInline):
    model = Nutrient
    extra = 3



# @admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ("name", "brand")
    fieldsets = [
        (None, {"fields": ["name"]}),
        ("Date information", {"fields": ["brand"], "classes": ["collapse"]}),
    ]
    inlines = [NutrientInline]


admin.site.register(Label,LabelAdmin)

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ("name", "abbreviation")
    search_fields = ("name", )
    

# @admin.register(Nutrient)
# class NutrientAdmin(admin.ModelAdmin):
#     list_display = ("nutrient", )
#     # search_fields = ("name", )

admin.site.register(Nutrient)
