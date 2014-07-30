from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db import models

import widgy

from widgy.models import Content
from widgy.models.mixins import (
    StrDisplayNameMixin,
)
from widgy.contrib.page_builder.models import CssContainerClasses

@widgy.register
class Container(StrDisplayNameMixin, Content, CssContainerClasses):
	name = models.CharField(max_length=255, default="", verbose_name=_('name'), null=True, blank=True)

	draggable = True
	deletable = True
	accepting_children = True
	editable = True

	class Meta:
		verbose_name = _('container')
		verbose_name_plural = _('containers')
		permissions = (
				("can_add_container_css_classes", "Can add Container CSS classes"),
			)
	
		app_label = "widgy_indium"


	def __str__(self):
		return self.name


