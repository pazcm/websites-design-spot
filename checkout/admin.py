from django.contrib import admin
from .models import Order, OrderLineItem

# Model register here to be edit in the admin panel

# TabularInline subclass defines the template used to render the order in the admin panel. Other option is StackedInline.
class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )

admin.site.register(Order, OrderAdmin)


