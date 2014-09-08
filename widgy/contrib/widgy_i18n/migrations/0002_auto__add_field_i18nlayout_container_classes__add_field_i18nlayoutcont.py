# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'I18NLayout.container_classes'
        db.add_column(u'widgy_i18n_i18nlayout', 'container_classes',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'I18NLayoutContainer.container_classes'
        db.add_column(u'widgy_i18n_i18nlayoutcontainer', 'container_classes',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'I18NLayout.container_classes'
        db.delete_column(u'widgy_i18n_i18nlayout', 'container_classes')

        # Deleting field 'I18NLayoutContainer.container_classes'
        db.delete_column(u'widgy_i18n_i18nlayoutcontainer', 'container_classes')


    models = {
        u'widgy_i18n.i18nlayout': {
            'Meta': {'object_name': 'I18NLayout'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'widgy_i18n.i18nlayoutcontainer': {
            'Meta': {'object_name': 'I18NLayoutContainer'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['widgy_i18n']