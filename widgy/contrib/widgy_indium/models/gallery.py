from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings

from widgy.models import Content

import widgy
  
from filer.fields.folder import FilerFolderField
from widgy.contrib.page_builder.models import CssContainerClasses, Image

@widgy.register
class ImageGallery(Content, CssContainerClasses):    
    
    folder = FilerFolderField(verbose_name=_("folder"), null=True)

    draggable = True
    deletable = True
    accepting_children = False
    editable = True

    class Meta:
        verbose_name = _('image gallery')
        verbose_name_plural = _('image galleries')
        permissions = (
                ("can_add_image_gallery_css_classes", "Can add image gallery CSS classes"),
        )
        
        app_label = "widgy_indium"

    #def valid_parent_of(self, cls, obj=None):
    #    return not issubclass(cls, (ImageGallery, Image))


