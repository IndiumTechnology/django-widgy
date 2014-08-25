from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings

from widgy.models import Content
from widgy.models.mixins import (
    StrictDefaultChildrenMixin, InvisibleMixin, StrDisplayNameMixin,
    TabbedContainer,
)

import widgy
  
from widgy.contrib.page_builder.models import CssContainerClasses

@widgy.register
class BlogPostList(StrDisplayNameMixin, Content, CssContainerClasses):    
	title = models.CharField(max_length=255, default="", verbose_name=_('title'), null=True, blank=True)

        #based on category field
        #based on author field
        post_count = models.PositiveIntegerField(default=5, verbose_name=_("post count"), help_text=_("Count of newest posts to show."))

	draggable = True
	deletable = True
	accepting_children = False
	editable = True

	class Meta:
		verbose_name = _('blog post list')
		verbose_name_plural = _('blog post lists')
                permissions = (
                        ("can_add_blog post_list_css_classes", "Can add blog post list CSS classes"),
                )
		
		app_label = "widgy_indium"


	def __str__(self):
		return self.title

