# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'MultiLanguageLayout'
        db.delete_table(u'widgy_i18n_multilanguagelayout')

        # Deleting model 'MultiLanguageLayoutContainer'
        db.delete_table(u'widgy_i18n_multilanguagelayoutcontainer')

        # Deleting model 'ContainerI18N'
        db.delete_table(u'widgy_i18n_containeri18n')

        # Adding model 'IndiumDefaultLayout'
        db.create_table(u'widgy_i18n_indiumdefaultlayout', (
            (u'i18nlayout_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['widgy_i18n.I18NLayout'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'widgy_i18n', ['IndiumDefaultLayout'])

        # Deleting field 'I18NLayoutContainer.container_classes'
        db.delete_column(u'widgy_i18n_i18nlayoutcontainer', 'container_classes')

        # Deleting field 'MainContentArea.container_classes'
        db.delete_column(u'widgy_i18n_maincontentarea', 'container_classes')

        # Deleting field 'I18NLayout.container_classes'
        db.delete_column(u'widgy_i18n_i18nlayout', 'container_classes')

        # Deleting field 'SidebarArea.container_classes'
        db.delete_column(u'widgy_i18n_sidebararea', 'container_classes')


    def backwards(self, orm):
        # Adding model 'MultiLanguageLayout'
        db.create_table(u'widgy_i18n_multilanguagelayout', (
            (u'i18nlayout_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['widgy_i18n.I18NLayout'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'widgy_i18n', ['MultiLanguageLayout'])

        # Adding model 'MultiLanguageLayoutContainer'
        db.create_table(u'widgy_i18n_multilanguagelayoutcontainer', (
            (u'i18nlayoutcontainer_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['widgy_i18n.I18NLayoutContainer'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'widgy_i18n', ['MultiLanguageLayoutContainer'])

        # Adding model 'ContainerI18N'
        db.create_table(u'widgy_i18n_containeri18n', (
            ('language_code', self.gf('django.db.models.fields.CharField')(default=u'fi', max_length=2)),
            ('container_classes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'widgy_i18n', ['ContainerI18N'])

        # Deleting model 'IndiumDefaultLayout'
        db.delete_table(u'widgy_i18n_indiumdefaultlayout')

        # Adding field 'I18NLayoutContainer.container_classes'
        db.add_column(u'widgy_i18n_i18nlayoutcontainer', 'container_classes',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MainContentArea.container_classes'
        db.add_column(u'widgy_i18n_maincontentarea', 'container_classes',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'I18NLayout.container_classes'
        db.add_column(u'widgy_i18n_i18nlayout', 'container_classes',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SidebarArea.container_classes'
        db.add_column(u'widgy_i18n_sidebararea', 'container_classes',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


    models = {
        u'widgy_i18n.i18nlayout': {
            'Meta': {'object_name': 'I18NLayout'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'widgy_i18n.i18nlayoutcontainer': {
            'Meta': {'object_name': 'I18NLayoutContainer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'widgy_i18n.indiumdefaultlayout': {
            'Meta': {'object_name': 'IndiumDefaultLayout', '_ormbases': [u'widgy_i18n.I18NLayout']},
            u'i18nlayout_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['widgy_i18n.I18NLayout']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'widgy_i18n.maincontentarea': {
            'Meta': {'object_name': 'MainContentArea'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'widgy_i18n.sidebararea': {
            'Meta': {'object_name': 'SidebarArea'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['widgy_i18n']