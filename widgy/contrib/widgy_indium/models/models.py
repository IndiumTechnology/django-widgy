from django.db import models
from django.utils.translation import (
    ugettext_lazy as _, ugettext, get_language, get_language_info, activate
)
from django.conf import settings
from django.core import urlresolvers

from mezzanine.pages.models import Page

from widgy.models import links
from widgy import register
from widgy.db.fields import VersionedWidgyField
from widgy.utils import SelectRelatedManager
from widgy.contrib.widgy_mezzanine.models import WidgyPageMixin, PageSelectRelatedManager

from widgy.contrib.widgy_i18n.models import I18NChild, I18NTabbedContainer, I18NLayout, I18NLayoutContainer, I18NBucket

@register
class MainContentArea(I18NBucket):
    	def valid_parent_of(self, cls, obj=None):
        	return not issubclass(cls, (MainContentArea, SidebarArea))

    	@classmethod
    	def valid_child_of(cls, parent, obj=None):
        	return isinstance(parent, I18NLayout)

    	class Meta:
        	verbose_name = _('main content')
        	verbose_name_plural = _('main contents')	
		app_label = "widgy_indium"

 

@register
class SidebarArea(I18NBucket):
    	pop_out = 1

	def valid_parent_of(self, cls, obj=None):
	        return not issubclass(cls, (MainContentArea, SidebarArea))

    	@classmethod
    	def valid_child_of(cls, parent, obj=None):
        	return isinstance(parent, I18NLayout)

    	class Meta:
        	verbose_name = _('sidebar')
        	verbose_name_plural = _('sidebars')	
		app_label = "widgy_indium"



@register
class IndiumDefaultLayout(I18NLayout):
    	"""
    	On creation, creates a left and right bucket.
    	"""
    	class Meta:
        	verbose_name = _('default layout')
        	verbose_name_plural = _('default layouts')	
		app_label = "widgy_indium"


    	default_children = [
        	('main', MainContentArea, (), {}),
        	('sidebar', SidebarArea, (), {}),
    	]

@register
class LayoutContainer(I18NLayoutContainer):
    	child_class = IndiumDefaultLayout

	class Meta:		
        	verbose_name = _('layout container')
        	verbose_name_plural = _('layout containers')	
		app_label = "widgy_indium"



def i18nreverse(language, *args, **kwargs):
    	current_language = get_language()
    	activate(language)
    	url = urlresolvers.reverse(*args, **kwargs)
    	activate(current_language)
    	return url

@links.register
class WidgetPage(WidgyPageMixin, Page):
	permanent_id = models.CharField(max_length=255, default="", verbose_name="permanent id")

	root_node = VersionedWidgyField(
	    site=settings.WIDGY_MEZZANINE_SITE,
	    verbose_name=_('widgy content'),
	    root_choices=(
		'widgy_indium.LayoutContainer',
	    ),
	    # WidgyField used to have these as defaults.
	    null=True,
	    on_delete=models.SET_NULL,
	)

	class Meta:
	    	verbose_name = _('widget page')
	    	verbose_name_plural = _('widget pages')	
		app_label = "widgy_indium"


	objects = PageSelectRelatedManager(select_related=[
	    'root_node'
	    'root_node__head',
	    # we might not need this, if head isn't published, but we
	    # probably will.
	    'root_node__head__root_node',
	])
	
	def get_action_links(self, root_node):
		# Provide the preview links for the various languages.
		return [
		    {
			'type': 'preview',
			'text': _('Preview (%s)') % node.content.language_code,
			'url': i18nreverse(node.content.language_code,
			    'widgy.contrib.widgy_mezzanine.views.preview',
			    kwargs={'slug': self.slug, 'node_pk': node.pk}
			)
		    }
		    for node in root_node.get_children()
		]
	

