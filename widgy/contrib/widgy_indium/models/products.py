from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings

from widgy.models import Content

import widgy
  
from widgy.contrib.page_builder.models import CssContainerClasses

from indium_mezzanine.mezzanine_products.models import ProductSubCategory

@widgy.register
class ProductsViewer(Content, CssContainerClasses):    

    draggable = True
    deletable = True
    accepting_children = False
    editable = True

    class Meta:
        verbose_name = _('products viewer')
        verbose_name_plural = _('products viewers')
        permissions = (
                ("can_add_products_viewer_css_classes", "Can add products viewer CSS classes"),
        )
        
        app_label = "widgy_indium"


@widgy.register
class NewestProducts(Content, CssContainerClasses):

    product_count = models.PositiveIntegerField(default=6, verbose_name=_("product count"), help_text=_("Count of newest products to show."))

    draggable = True
    deletable = True
    accepting_children = False
    editable = True

    class Meta:
        verbose_name = _('newest products')
        verbose_name_plural = _('newest products')
        permissions = (
                ("can_add_newest_products_css_classes", "Can add newest products CSS classes"),
        )
        
        app_label = "widgy_indium"

