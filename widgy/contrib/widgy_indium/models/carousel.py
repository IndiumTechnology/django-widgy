from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings

from filer.fields.file import FilerFileField
from filer.models.filemodels import File

from widgy.models import Content
from widgy.models.mixins import (
    StrictDefaultChildrenMixin, InvisibleMixin, StrDisplayNameMixin,
    TabbedContainer,
)

import widgy
import re
import os
  
from widgy.contrib.page_builder.models import CssContainerClasses

def validate_image(file_pk):
    	file = File.objects.get(pk=file_pk)
    	iext = os.path.splitext(file.file.name)[1].lower()
    	if not iext in ['.jpg', '.jpeg', '.png', '.gif']:
        	raise forms.ValidationError('File type must be jpg, png, or gif')
    	return file_pk


def ImageField(*args, **kwargs):
	"""
	This is a convenience function to wrap the default args that we always
	want.  This is implemented as a function to avoid invoking the wrath of
	South's model introspection.
	"""
	defaults = {
	    'null': True,
  	    'blank': True,
	    'verbose_name': _('image'),
	    'validators': [validate_image],
	    'related_name': '+',
	    # What should happen on_delete.  Set to models.PROTECT so this is harder to
	    # ignore and forget about.
	    'on_delete': models.PROTECT,
	}
	defaults.update(kwargs)

	return FilerFileField(*args, **defaults)


@widgy.register
class Carousel(StrDisplayNameMixin, Content, CssContainerClasses):    
	title = models.CharField(max_length=255, default="", verbose_name=_('title'), null=True, blank=True)

	# Settings for jCarousel
	delay = 			models.PositiveIntegerField(default=2000, verbose_name=_("delay"), help_text=_("The delay in milliseconds between slides. Used only if autoscroll is enabled."))
	auto_scroll =  		models.BooleanField(default=True, verbose_name=_("auto scroll"))
	pause_scroll_on_hover =  	models.BooleanField(default=True, verbose_name=_("pause scroll on hover"))
	pagination = 		models.BooleanField(default=False, verbose_name=_("pagination"))
	controls = 			models.BooleanField(default=True, verbose_name=_("controls"), help_text=_("Arrows to go next or previous."))

	# Advanced settings
	AN_EASINGS = (	('swing', _('Swing')),
			('linear', _('Linear')),)

	WRAP_MODES = (	('first', _('First')),
			('last', _('Last')),
			('both', _('Both')),
			('circular', _('Circular')),)

	ORIENTATIONS = ((False, _('Horizonal')),
			(True, _('Vetical')),)

	animation_duration =	models.PositiveIntegerField(default=400, help_text=_("The duration in milliseconds."), verbose_name=_("animation duration"))
	animation_easing = 		models.CharField(max_length=10, choices=AN_EASINGS, default="linear", verbose_name=_("animation easing"))
	wrap_mode = 		models.CharField(max_length=10, choices=WRAP_MODES, default="circular", verbose_name=_("wrap mode"))
	orientation = 		models.BooleanField(choices=ORIENTATIONS, default=False , verbose_name=_("orientation"))
	visible_slides_at_time = 	models.PositiveIntegerField(default=1, verbose_name=_("visible slides at time"))

	collapsed = { 	'title' : _("Advanced settings"),
			'fields': ("animation_duration", "animation_easing", "wrap_mode", "orientation", "visible_slides_at_time"),
		}

	js = ("/static/js/jquery.jcarousel.min.js",)

	css = ()

	draggable = True
	deletable = True
	accepting_children = True
	editable = True

	class Meta:
		verbose_name = _('carousel')
		verbose_name_plural = _('carousels')
                permissions = (
                        ("can_add_carousel_css_classes", "Can add Carousel CSS classes"),
                )
		
		app_label = "widgy_indium"


	def valid_parent_of(self, cls, obj=None):
		# only accept CarouselItems
		return issubclass(cls, CarouselItem)


	def __str__(self):
		return self.title

@widgy.register
class CarouselItem(StrDisplayNameMixin, Content, CssContainerClasses):    
	title = models.CharField(max_length=255, default="", verbose_name=_('title'), null=True, blank=True)
	background_image = ImageField(verbose_name=_('background image'))
	background_color = models.CharField(max_length=255, default="", null=True, blank=True, verbose_name=_('background color'))
	#objects = SelectRelatedManager(select_related=['image'])

	draggable = True
	deletable = True
	accepting_children = True
	editable = True

	class Meta:
		verbose_name = _('carousel item')
		verbose_name_plural = _('carousel items')
                permissions = (
                        ("can_add_carousel_item_css_classes", "Can add Carousel Item CSS Classes"),
                )
		
		app_label = "widgy_indium"


	@classmethod
	def valid_child_of(cls, parent, obj=None):
		# Only go in Carousel
		return isinstance(parent, Carousel)

	def __str__(self):
		return self.title

