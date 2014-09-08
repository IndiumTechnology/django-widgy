# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Video.container_classes'
        db.alter_column(u'page_builder_video', 'container_classes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Table.container_classes'
        db.alter_column(u'page_builder_table', 'container_classes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Accordion.container_classes'
        db.alter_column(u'page_builder_accordion', 'container_classes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'GoogleMap.container_classes'
        db.alter_column(u'page_builder_googlemap', 'container_classes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Figure.container_classes'
        db.alter_column(u'page_builder_figure', 'container_classes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'CalloutWidget.container_classes'
        db.alter_column(u'page_builder_calloutwidget', 'container_classes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Section.container_classes'
        db.alter_column(u'page_builder_section', 'container_classes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DefaultLayout.container_classes'
        db.alter_column(u'page_builder_defaultlayout', 'container_classes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'CalloutBucket.container_classes'
        db.alter_column(u'page_builder_calloutbucket', 'container_classes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'TableHeaderData.container_classes'
        db.alter_column(u'page_builder_tableheaderdata', 'container_classes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Markdown.container_classes'
        db.alter_column(u'page_builder_markdown', 'container_classes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'MainContent.container_classes'
        db.alter_column(u'page_builder_maincontent', 'container_classes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'TableData.container_classes'
        db.alter_column(u'page_builder_tabledata', 'container_classes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'UnsafeHtml.container_classes'
        db.alter_column(u'page_builder_unsafehtml', 'container_classes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Button.container_classes'
        db.alter_column(u'page_builder_button', 'container_classes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Html.container_classes'
        db.alter_column(u'page_builder_html', 'container_classes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'TableRow.container_classes'
        db.alter_column(u'page_builder_tablerow', 'container_classes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'TableHeader.container_classes'
        db.alter_column(u'page_builder_tableheader', 'container_classes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'TableBody.container_classes'
        db.alter_column(u'page_builder_tablebody', 'container_classes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Image.container_classes'
        db.alter_column(u'page_builder_image', 'container_classes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Sidebar.container_classes'
        db.alter_column(u'page_builder_sidebar', 'container_classes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    def backwards(self, orm):

        # Changing field 'Video.container_classes'
        db.alter_column(u'page_builder_video', 'container_classes', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Table.container_classes'
        db.alter_column(u'page_builder_table', 'container_classes', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Accordion.container_classes'
        db.alter_column(u'page_builder_accordion', 'container_classes', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'GoogleMap.container_classes'
        db.alter_column(u'page_builder_googlemap', 'container_classes', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Figure.container_classes'
        db.alter_column(u'page_builder_figure', 'container_classes', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'CalloutWidget.container_classes'
        db.alter_column(u'page_builder_calloutwidget', 'container_classes', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Section.container_classes'
        db.alter_column(u'page_builder_section', 'container_classes', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DefaultLayout.container_classes'
        db.alter_column(u'page_builder_defaultlayout', 'container_classes', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'CalloutBucket.container_classes'
        db.alter_column(u'page_builder_calloutbucket', 'container_classes', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'TableHeaderData.container_classes'
        db.alter_column(u'page_builder_tableheaderdata', 'container_classes', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Markdown.container_classes'
        db.alter_column(u'page_builder_markdown', 'container_classes', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'MainContent.container_classes'
        db.alter_column(u'page_builder_maincontent', 'container_classes', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'TableData.container_classes'
        db.alter_column(u'page_builder_tabledata', 'container_classes', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'UnsafeHtml.container_classes'
        db.alter_column(u'page_builder_unsafehtml', 'container_classes', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Button.container_classes'
        db.alter_column(u'page_builder_button', 'container_classes', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Html.container_classes'
        db.alter_column(u'page_builder_html', 'container_classes', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'TableRow.container_classes'
        db.alter_column(u'page_builder_tablerow', 'container_classes', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'TableHeader.container_classes'
        db.alter_column(u'page_builder_tableheader', 'container_classes', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'TableBody.container_classes'
        db.alter_column(u'page_builder_tablebody', 'container_classes', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Image.container_classes'
        db.alter_column(u'page_builder_image', 'container_classes', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Sidebar.container_classes'
        db.alter_column(u'page_builder_sidebar', 'container_classes', self.gf('django.db.models.fields.TextField')(null=True))

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
        u'page_builder.accordion': {
            'Meta': {'object_name': 'Accordion'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'page_builder.button': {
            'Meta': {'object_name': 'Button'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'link_object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'page_builder.callout': {
            'Meta': {'object_name': 'Callout'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'root_node': ('widgy.db.fields.WidgyField', [], {'to': "orm['widgy.Node']", 'null': 'True', 'on_delete': 'models.SET_NULL'})
        },
        u'page_builder.calloutbucket': {
            'Meta': {'object_name': 'CalloutBucket'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'page_builder.calloutwidget': {
            'Meta': {'object_name': 'CalloutWidget'},
            'callout': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['page_builder.Callout']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'page_builder.defaultlayout': {
            'Meta': {'object_name': 'DefaultLayout'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'page_builder.figure': {
            'Meta': {'object_name': 'Figure'},
            'caption': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'default': "u'center'", 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1023', 'null': 'True', 'blank': 'True'})
        },
        u'page_builder.googlemap': {
            'Meta': {'object_name': 'GoogleMap'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'roadmap'", 'max_length': '20'})
        },
        u'page_builder.html': {
            'Meta': {'object_name': 'Html'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'page_builder.image': {
            'Meta': {'object_name': 'Image'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['filer.File']"})
        },
        u'page_builder.maincontent': {
            'Meta': {'object_name': 'MainContent'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'page_builder.markdown': {
            'Meta': {'object_name': 'Markdown'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'content': ('widgy.contrib.page_builder.db.fields.MarkdownField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rendered': ('django.db.models.fields.TextField', [], {})
        },
        u'page_builder.section': {
            'Meta': {'object_name': 'Section'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1023'})
        },
        u'page_builder.sidebar': {
            'Meta': {'object_name': 'Sidebar'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'page_builder.table': {
            'Meta': {'object_name': 'Table'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'page_builder.tablebody': {
            'Meta': {'object_name': 'TableBody'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'page_builder.tabledata': {
            'Meta': {'object_name': 'TableData'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'page_builder.tableheader': {
            'Meta': {'object_name': 'TableHeader'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'page_builder.tableheaderdata': {
            'Meta': {'object_name': 'TableHeaderData'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'page_builder.tablerow': {
            'Meta': {'object_name': 'TableRow'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'page_builder.unsafehtml': {
            'Meta': {'object_name': 'UnsafeHtml'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'page_builder.video': {
            'Meta': {'object_name': 'Video'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'video': ('widgy.contrib.page_builder.db.fields.VideoField', [], {'max_length': '200'})
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
        }
    }

    complete_apps = ['page_builder']