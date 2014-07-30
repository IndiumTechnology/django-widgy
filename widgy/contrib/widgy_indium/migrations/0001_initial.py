# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MainContentArea'
        db.create_table(u'widgy_indium_maincontentarea', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(default=u'fi', max_length=2)),
        ))
        db.send_create_signal('widgy_indium', ['MainContentArea'])

        # Adding model 'SidebarArea'
        db.create_table(u'widgy_indium_sidebararea', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(default=u'fi', max_length=2)),
        ))
        db.send_create_signal('widgy_indium', ['SidebarArea'])

        # Adding model 'IndiumDefaultLayout'
        db.create_table(u'widgy_indium_indiumdefaultlayout', (
            (u'i18nlayout_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['widgy_i18n.I18NLayout'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('widgy_indium', ['IndiumDefaultLayout'])

        # Adding model 'LayoutContainer'
        db.create_table(u'widgy_indium_layoutcontainer', (
            (u'i18nlayoutcontainer_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['widgy_i18n.I18NLayoutContainer'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('widgy_indium', ['LayoutContainer'])

        # Adding model 'WidgetPage'
        db.create_table(u'widgy_indium_widgetpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True)),
            ('permanent_id', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('root_node', self.gf('widgy.db.fields.VersionedWidgyField')(to=orm['widgy.VersionTracker'], null=True, on_delete=models.SET_NULL)),
        ))
        db.send_create_signal('widgy_indium', ['WidgetPage'])

        # Adding model 'Carousel'
        db.create_table(u'widgy_indium_carousel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('container_classes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
            ('delay', self.gf('django.db.models.fields.PositiveIntegerField')(default=2000)),
            ('auto_scroll', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('pause_scroll_on_hover', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('pagination', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('controls', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('animation_duration', self.gf('django.db.models.fields.PositiveIntegerField')(default=400)),
            ('animation_easing', self.gf('django.db.models.fields.CharField')(default='linear', max_length=10)),
            ('wrap_mode', self.gf('django.db.models.fields.CharField')(default='circular', max_length=10)),
            ('orientation', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('visible_slides_at_time', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
        ))
        db.send_create_signal('widgy_indium', ['Carousel'])

        # Adding model 'CarouselItem'
        db.create_table(u'widgy_indium_carouselitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('container_classes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
            ('background_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, on_delete=models.PROTECT, to=orm['filer.File'])),
            ('background_color', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('widgy_indium', ['CarouselItem'])

        # Adding model 'Container'
        db.create_table(u'widgy_indium_container', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('container_classes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('widgy_indium', ['Container'])


    def backwards(self, orm):
        # Deleting model 'MainContentArea'
        db.delete_table(u'widgy_indium_maincontentarea')

        # Deleting model 'SidebarArea'
        db.delete_table(u'widgy_indium_sidebararea')

        # Deleting model 'IndiumDefaultLayout'
        db.delete_table(u'widgy_indium_indiumdefaultlayout')

        # Deleting model 'LayoutContainer'
        db.delete_table(u'widgy_indium_layoutcontainer')

        # Deleting model 'WidgetPage'
        db.delete_table(u'widgy_indium_widgetpage')

        # Deleting model 'Carousel'
        db.delete_table(u'widgy_indium_carousel')

        # Deleting model 'CarouselItem'
        db.delete_table(u'widgy_indium_carouselitem')

        # Deleting model 'Container'
        db.delete_table(u'widgy_indium_container')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'filer.file': {
            'Meta': {'object_name': 'File'},
            '_file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'all_files'", 'null': 'True', 'to': "orm['filer.Folder']"}),
            'has_all_mandatory_data': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owned_files'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_filer.file_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'sha1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40', 'blank': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'filer.folder': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('parent', 'name'),)", 'object_name': 'Folder'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'filer_owned_folders'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['filer.Folder']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'pages.page': {
            'Meta': {'ordering': "(u'titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_meta_title_en': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_meta_title_fi': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_fi': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '(1, 2, 3)', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'title_fi': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'widgy.node': {
            'Meta': {'unique_together': "[('content_type', 'content_id')]", 'object_name': 'Node'},
            'content_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_frozen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'numchild': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'widgy.versioncommit': {
            'Meta': {'object_name': 'VersionCommit'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['widgy.VersionCommit']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'root_node': ('widgy.db.fields.WidgyField', [], {'to': "orm['widgy.Node']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'tracker': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'commits'", 'to': "orm['widgy.VersionTracker']"})
        },
        'widgy.versiontracker': {
            'Meta': {'object_name': 'VersionTracker'},
            'head': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['widgy.VersionCommit']", 'unique': 'True', 'null': 'True', 'on_delete': 'models.PROTECT'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'working_copy': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['widgy.Node']", 'unique': 'True', 'on_delete': 'models.PROTECT'})
        },
        u'widgy_i18n.i18nlayout': {
            'Meta': {'object_name': 'I18NLayout'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'default': "u'fi'", 'max_length': '2'})
        },
        u'widgy_i18n.i18nlayoutcontainer': {
            'Meta': {'object_name': 'I18NLayoutContainer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'widgy_indium.carousel': {
            'Meta': {'object_name': 'Carousel'},
            'animation_duration': ('django.db.models.fields.PositiveIntegerField', [], {'default': '400'}),
            'animation_easing': ('django.db.models.fields.CharField', [], {'default': "'linear'", 'max_length': '10'}),
            'auto_scroll': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'controls': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'delay': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orientation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pagination': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pause_scroll_on_hover': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'visible_slides_at_time': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'wrap_mode': ('django.db.models.fields.CharField', [], {'default': "'circular'", 'max_length': '10'})
        },
        'widgy_indium.carouselitem': {
            'Meta': {'object_name': 'CarouselItem'},
            'background_color': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'background_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['filer.File']"}),
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'widgy_indium.container': {
            'Meta': {'object_name': 'Container'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'widgy_indium.indiumdefaultlayout': {
            'Meta': {'object_name': 'IndiumDefaultLayout', '_ormbases': [u'widgy_i18n.I18NLayout']},
            u'i18nlayout_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['widgy_i18n.I18NLayout']", 'unique': 'True', 'primary_key': 'True'})
        },
        'widgy_indium.layoutcontainer': {
            'Meta': {'object_name': 'LayoutContainer', '_ormbases': [u'widgy_i18n.I18NLayoutContainer']},
            u'i18nlayoutcontainer_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['widgy_i18n.I18NLayoutContainer']", 'unique': 'True', 'primary_key': 'True'})
        },
        'widgy_indium.maincontentarea': {
            'Meta': {'object_name': 'MainContentArea'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'default': "u'fi'", 'max_length': '2'})
        },
        'widgy_indium.sidebararea': {
            'Meta': {'object_name': 'SidebarArea'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'default': "u'fi'", 'max_length': '2'})
        },
        'widgy_indium.widgetpage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'WidgetPage', '_ormbases': [u'pages.Page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'permanent_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'root_node': ('widgy.db.fields.VersionedWidgyField', [], {'to': "orm['widgy.VersionTracker']", 'null': 'True', 'on_delete': 'models.SET_NULL'})
        }
    }

    complete_apps = ['widgy_indium']