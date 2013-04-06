from operator import or_
import itertools

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django import forms

from widgy.generic import WidgyGenericForeignKey


def is_linkable(model):
    return issubclass(model, LinkableMixin) and not model._meta.proxy


def has_link(model):
    return any(isinstance(field, LinkField)
               for field in model._meta.virtual_fields)


def get_all_linkable_classes():
    return filter(is_linkable, models.get_models())


def get_all_linker_classes():
    return filter(has_link, models.get_models())


def points_to_links(linker, linkable):
    """
    Returns a Q object that filters for the linkable instance across all
    LinkFields on the linker model.
    """
    content_type = ContentType.objects.get_for_model(linkable)
    return reduce(or_, (models.Q(**{field.ct_field: content_type,
                                    field.fk_field: linkable.pk})
                        for field in linker._meta.virtual_fields
                        if isinstance(field, LinkField)))


class LinkableMixin(object):
    def get_links(self):
        """
        Returns a heterogenous list of all things that have a LinkField that
        points to self.
        """
        all_qs = (linker._default_manager.filter(points_to_links(linker, self))
                  for linker in get_all_linker_classes())

        return itertools.chain.from_iterable(all_qs)


class LinkField(WidgyGenericForeignKey):
    """
    TODO: Explore the consequences of using add_field in contribute_to_class to
    make this a real field instead of a virtual_field.
    """
    def __init__(self, ct_field=None, fk_field=None, *args, **kwargs):
        self.null = kwargs.pop('null', False)
        super(LinkField, self).__init__(ct_field, fk_field, *args, **kwargs)

    def get_choices(self):
        all_qs = (model._default_manager.all()
                  for model in get_all_linkable_classes())
        return itertools.chain.from_iterable(all_qs)

    def contribute_to_class(self, cls, name):
        if self.ct_field is None:
            self.ct_field = '%s_content_type' % name

        if self.fk_field is None:
            self.fk_field = '%s_object_id' % name

        if self.ct_field not in cls._meta.get_all_field_names():
            ct_field = models.ForeignKey(ContentType, related_name='+',
                                         null=self.null, editable=False)
            cls.add_to_class(self.ct_field, ct_field)

        if self.fk_field not in cls._meta.get_all_field_names():
            fk_field = models.PositiveIntegerField(null=self.null,
                                                   editable=False)
            cls.add_to_class(self.fk_field, fk_field)

        super(LinkField, self).contribute_to_class(cls, name)


def get_composite_key(linkable):
    content_type = ContentType.objects.get_for_model(linkable)
    return u'%s-%s' % (content_type.pk, linkable.pk)


def convert_linkable_to_choice(linkable):
    key = get_composite_key(linkable)

    try:
        value = u'%s (%s)' % (unicode(linkable), linkable.get_absolute_url())
    except AttributeError:
        value = unicode(linkable)

    return (key, value)


class LinkFormField(forms.ChoiceField):
    def __init__(self, choices=(), empty_label="---------", *args, **kwargs):
        self.empty_label = empty_label
        super(LinkFormField, self).__init__(choices, *args, **kwargs)

    def clean(self, value):
        content_type_pk, _, object_pk = value.partition('-')
        if object_pk:
            content_type = ContentType.objects.get_for_id(content_type_pk)
            return content_type.get_object_for_this_type(pk=object_pk)
        else:
            return None

    def populate_choices(self, choices):
        choices = map(convert_linkable_to_choice, choices)
        if not self.required and self.empty_label is not None:
            choices.insert(0, ('', self.empty_label))

        self.choices = choices


def get_link_field_from_model(model, name):
    for field in model._meta.virtual_fields:
        if isinstance(field, LinkField) and field.name == name:
            return field


class LinkFormMixin(object):
    def __init__(self, *args, **kwargs):
        super(LinkFormMixin, self).__init__(*args, **kwargs)
        for name, field in self.get_link_form_fields():
            value = getattr(self.instance, name, None)
            model_field = get_link_field_from_model(self.instance, name)
            field.initial = get_composite_key(value) if value else None
            field.populate_choices(model_field.get_choices())

    def get_link_form_fields(self):
        return ((name, field)
                for name, field in self.fields.items()
                if isinstance(field, LinkFormField))

    def save(self, *args, **kwargs):
        if not self.errors:
            cleaned_data = self.cleaned_data

            for name, field in self.get_link_form_fields():
                setattr(self.instance, name, cleaned_data[name])

        return super(LinkFormMixin, self).save(*args, **kwargs)