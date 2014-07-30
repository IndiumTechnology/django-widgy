from django.db import models
from django.utils.translation import (
    ugettext_lazy as _, ugettext, get_language, get_language_info
)
from django.conf import settings
 
from widgy.models import Content
from widgy.contrib.page_builder.models import Layout
from widgy.models.mixins import TabbedContainer, StrictDefaultChildrenMixin
from widgy import register


class I18NChild(models.Model):
    """
    Mixin for Contents that go directly inside I18NTabbedContainers.
    """
    language_code = models.CharField(verbose_name=_('Layout'),
                                     max_length=2,
                                     choices=settings.LANGUAGES,
                                     default=settings.LANGUAGE_CODE)
    class Meta:
        abstract = True

    @property
    def language_name(self):
        info = get_language_info(self.language_code)
        return ugettext(info['name'])

    @property
    def display_name(self):
        return self.language_name


class I18NTabbedContainer(TabbedContainer, Content):
    """
    A TabbedContainer that chooses which child to render based on the
    current language.  You should only put I18NChild in this as children.
    """
    class Meta:
        abstract = True

    def render(self, *args, **kwargs):
        current_language = get_language()
        try:
            child = self.get_child_for_language(current_language)
        except IndexError:
            child = self.get_child_for_language(current_language[0:2])
        return child.render(*args, **kwargs)

    def get_child_for_language(self, code):
        return [child for child in self.get_children() if child.language_code == code][0]


@register
class I18NLayout(I18NChild, Layout):
    """
    This is a layout for a specific language that lives inside a
    I18NLayoutContainer.
    """
    @classmethod
    def valid_child_of(cls, content, obj=None):
        return isinstance(content, I18NLayoutContainer)


@register
class I18NLayoutContainer(StrictDefaultChildrenMixin, I18NTabbedContainer):
    """
    A root node that holds different language versions of the same page.
    """
    child_class = I18NLayout
    draggable = False
    editable = False
    deletable = False

    @property
    def default_children(self):
        return [
            (l[0], self.child_class, (), {'language_code': l[0]})
            for l in settings.LANGUAGES
        ]

    @classmethod
    def valid_child_of(self, content, obj=None):
        return False




class I18NBucket(I18NChild, Content):
    	draggable = False
    	deletable = False
    	accepting_children = True

	@property
    	def display_name(self):
        	return unicode(self._meta.verbose_name)	

    	class Meta:
        	abstract = True
"""
@register
class MainContentArea(Bucket):
    	def valid_parent_of(self, cls, obj=None):
        	return not issubclass(cls, (MainContentArea, SidebarArea))

    	@classmethod
    	def valid_child_of(cls, parent, obj=None):
        	return isinstance(parent, I18NLayout)

    	class Meta:
        	verbose_name = _('main content')
        	verbose_name_plural = _('main contents')
 

@register
class SidebarArea(Bucket):
    	pop_out = 1

	def valid_parent_of(self, cls, obj=None):
	        return not issubclass(cls, (MainContentArea, SidebarArea))

    	@classmethod
    	def valid_child_of(cls, parent, obj=None):
        	return isinstance(parent, I18NLayout)

    	class Meta:
        	verbose_name = _('sidebar')
        	verbose_name_plural = _('sidebars')


@register
class IndiumDefaultLayout(I18NLayout):
    	class Meta:
        	verbose_name = _('default layout')
        	verbose_name_plural = _('default layouts')

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
		'widgy_i18n.LayoutContainer',
	    ),
	    # WidgyField used to have these as defaults.
	    null=True,
	    on_delete=models.SET_NULL,
	)

	class Meta:
	    	verbose_name = _('widget page')
	    	verbose_name_plural = _('widget pages')

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
	
"""
