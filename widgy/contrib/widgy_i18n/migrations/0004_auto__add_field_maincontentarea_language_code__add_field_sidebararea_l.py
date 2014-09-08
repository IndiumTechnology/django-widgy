# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MainContentArea.language_code'
        db.add_column(u'widgy_i18n_maincontentarea', 'language_code',
                      self.gf('django.db.models.fields.CharField')(default=u'fi', max_length=2),
                      keep_default=False)

        # Adding field 'SidebarArea.language_code'
        db.add_column(u'widgy_i18n_sidebararea', 'language_code',
                      self.gf('django.db.models.fields.CharField')(default=u'fi', max_length=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MainContentArea.language_code'
        db.delete_column(u'widgy_i18n_maincontentarea', 'language_code')

        # Deleting field 'SidebarArea.language_code'
        db.delete_column(u'widgy_i18n_sidebararea', 'language_code')


    models = {
        u'widgy_i18n.i18nlayout': {
            'Meta': {'object_name': 'I18NLayout'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'default': "u'fi'", 'max_length': '2'})
        },
        u'widgy_i18n.i18nlayoutcontainer': {
            'Meta': {'object_name': 'I18NLayoutContainer'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'widgy_i18n.maincontentarea': {
            'Meta': {'object_name': 'MainContentArea'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'default': "u'fi'", 'max_length': '2'})
        },
        u'widgy_i18n.multilanguagelayout': {
            'Meta': {'object_name': 'MultiLanguageLayout', '_ormbases': [u'widgy_i18n.I18NLayout']},
            u'i18nlayout_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['widgy_i18n.I18NLayout']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'widgy_i18n.multilanguagelayoutcontainer': {
            'Meta': {'object_name': 'MultiLanguageLayoutContainer', '_ormbases': [u'widgy_i18n.I18NLayoutContainer']},
            u'i18nlayoutcontainer_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['widgy_i18n.I18NLayoutContainer']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'widgy_i18n.sidebararea': {
            'Meta': {'object_name': 'SidebarArea'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'default': "u'fi'", 'max_length': '2'})
        }
    }

    complete_apps = ['widgy_i18n']