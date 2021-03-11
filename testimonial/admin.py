from django.contrib import admin

from wagtail.contrib.modeladmin.options import (
    ModelAdmin,modeladmin_register
)
from .models import Testimonial
# Register your models here.

@modeladmin_register
class TestimonialAdmin(ModelAdmin):
    """Testimonial Admin"""

    model=Testimonial
    menu_label='Testimonial'
    menu_icon='placeholder'
    menu_order = 290
    add_to_settings_menu=False
    exlude_from_explorer=False
    list_display= ("quote",'attribution')
    search_fields=("quote","attribution")