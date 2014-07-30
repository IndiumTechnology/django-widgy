# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FieldMappingValue'
        db.create_table(u'form_builder_fieldmappingvalue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('container_classes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('field_ident', self.gf('django.db.models.fields.CharField')(max_length=36)),
        ))
        db.send_create_signal(u'form_builder', ['FieldMappingValue'])

        # Adding model 'FileUpload'
        db.create_table(u'form_builder_fileupload', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('required', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('help_text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('ident', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
        ))
        db.send_create_signal(u'form_builder', ['FileUpload'])

        # Adding model 'WebToLeadMapperHandler'
        db.create_table(u'form_builder_webtoleadmapperhandler', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('container_classes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('oid', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'form_builder', ['WebToLeadMapperHandler'])

        # Adding field 'EmailSuccessHandler.container_classes'
        db.add_column(u'form_builder_emailsuccesshandler', 'container_classes',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'EmailSuccessHandler.include_form_data'
        db.add_column(u'form_builder_emailsuccesshandler', 'include_form_data',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


        # Changing field 'EmailSuccessHandler.content'
        db.alter_column(u'form_builder_emailsuccesshandler', 'content', self.gf('django.db.models.fields.TextField')())
        # Deleting field 'EmailUserHandler.to'
        db.delete_column(u'form_builder_emailuserhandler', 'to_id')

        # Adding field 'EmailUserHandler.container_classes'
        db.add_column(u'form_builder_emailuserhandler', 'container_classes',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'EmailUserHandler.include_form_data'
        db.add_column(u'form_builder_emailuserhandler', 'include_form_data',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'EmailUserHandler.to_ident'
        db.add_column(u'form_builder_emailuserhandler', 'to_ident',
                      self.gf('django.db.models.fields.CharField')(default=False, max_length=36),
                      keep_default=False)


        # Changing field 'EmailUserHandler.content'
        db.alter_column(u'form_builder_emailuserhandler', 'content', self.gf('django.db.models.fields.TextField')())
        # Deleting field 'FormSubmission.updated_at'
        db.delete_column(u'form_builder_formsubmission', 'updated_at')


        # Changing field 'FormSubmission.created_at'
        db.alter_column(u'form_builder_formsubmission', 'created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))
        # Adding field 'Uncaptcha.container_classes'
        db.add_column(u'form_builder_uncaptcha', 'container_classes',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MultipleChoiceField.container_classes'
        db.add_column(u'form_builder_multiplechoicefield', 'container_classes',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Form.container_classes'
        db.add_column(u'form_builder_form', 'container_classes',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SubmitButton.container_classes'
        db.add_column(u'form_builder_submitbutton', 'container_classes',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'FormInput.container_classes'
        db.add_column(u'form_builder_forminput', 'container_classes',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Textarea.container_classes'
        db.add_column(u'form_builder_textarea', 'container_classes',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ChoiceField.container_classes'
        db.add_column(u'form_builder_choicefield', 'container_classes',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SaveDataHandler.container_classes'
        db.add_column(u'form_builder_savedatahandler', 'container_classes',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'FieldMappingValue'
        db.delete_table(u'form_builder_fieldmappingvalue')

        # Deleting model 'FileUpload'
        db.delete_table(u'form_builder_fileupload')

        # Deleting model 'WebToLeadMapperHandler'
        db.delete_table(u'form_builder_webtoleadmapperhandler')

        # Deleting field 'EmailSuccessHandler.container_classes'
        db.delete_column(u'form_builder_emailsuccesshandler', 'container_classes')

        # Deleting field 'EmailSuccessHandler.include_form_data'
        db.delete_column(u'form_builder_emailsuccesshandler', 'include_form_data')


        # Changing field 'EmailSuccessHandler.content'
        db.alter_column(u'form_builder_emailsuccesshandler', 'content', self.gf('widgy.contrib.page_builder.db.fields.MarkdownField')())
        # Adding field 'EmailUserHandler.to'
        db.add_column(u'form_builder_emailuserhandler', 'to',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'+', null=True, to=orm['widgy.Node']),
                      keep_default=False)

        # Deleting field 'EmailUserHandler.container_classes'
        db.delete_column(u'form_builder_emailuserhandler', 'container_classes')

        # Deleting field 'EmailUserHandler.include_form_data'
        db.delete_column(u'form_builder_emailuserhandler', 'include_form_data')

        # Deleting field 'EmailUserHandler.to_ident'
        db.delete_column(u'form_builder_emailuserhandler', 'to_ident')


        # Changing field 'EmailUserHandler.content'
        db.alter_column(u'form_builder_emailuserhandler', 'content', self.gf('widgy.contrib.page_builder.db.fields.MarkdownField')())
        # Adding field 'FormSubmission.updated_at'
        db.add_column(u'form_builder_formsubmission', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default='', blank=True),
                      keep_default=False)


        # Changing field 'FormSubmission.created_at'
        db.alter_column(u'form_builder_formsubmission', 'created_at', self.gf('django.db.models.fields.DateTimeField')())
        # Deleting field 'Uncaptcha.container_classes'
        db.delete_column(u'form_builder_uncaptcha', 'container_classes')

        # Deleting field 'MultipleChoiceField.container_classes'
        db.delete_column(u'form_builder_multiplechoicefield', 'container_classes')

        # Deleting field 'Form.container_classes'
        db.delete_column(u'form_builder_form', 'container_classes')

        # Deleting field 'SubmitButton.container_classes'
        db.delete_column(u'form_builder_submitbutton', 'container_classes')

        # Deleting field 'FormInput.container_classes'
        db.delete_column(u'form_builder_forminput', 'container_classes')

        # Deleting field 'Textarea.container_classes'
        db.delete_column(u'form_builder_textarea', 'container_classes')

        # Deleting field 'ChoiceField.container_classes'
        db.delete_column(u'form_builder_choicefield', 'container_classes')

        # Deleting field 'SaveDataHandler.container_classes'
        db.delete_column(u'form_builder_savedatahandler', 'container_classes')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'form_builder.choicefield': {
            'Meta': {'object_name': 'ChoiceField'},
            'choices': ('django.db.models.fields.TextField', [], {}),
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ident': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'form_builder.emailsuccesshandler': {
            'Meta': {'object_name': 'EmailSuccessHandler'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'include_form_data': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'to': ('django.db.models.fields.EmailField', [], {'max_length': '75'})
        },
        u'form_builder.emailuserhandler': {
            'Meta': {'object_name': 'EmailUserHandler'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'include_form_data': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'to_ident': ('django.db.models.fields.CharField', [], {'max_length': '36'})
        },
        u'form_builder.fieldmappingvalue': {
            'Meta': {'object_name': 'FieldMappingValue'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'field_ident': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'form_builder.fileupload': {
            'Meta': {'object_name': 'FileUpload'},
            'help_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ident': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'form_builder.form': {
            'Meta': {'object_name': 'Form'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ident': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u'Untitled form 1'", 'max_length': '255'})
        },
        u'form_builder.formbody': {
            'Meta': {'object_name': 'FormBody'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'form_builder.forminput': {
            'Meta': {'object_name': 'FormInput'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ident': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'form_builder.formmeta': {
            'Meta': {'object_name': 'FormMeta'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'form_builder.formsubmission': {
            'Meta': {'object_name': 'FormSubmission'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'form_ident': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'form_node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'form_submissions'", 'on_delete': 'models.PROTECT', 'to': "orm['widgy.Node']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'form_builder.formvalue': {
            'Meta': {'object_name': 'FormValue'},
            'field_ident': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'field_node': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['widgy.Node']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'submission': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'values'", 'to': u"orm['form_builder.FormSubmission']"}),
            'value': ('django.db.models.fields.TextField', [], {})
        },
        u'form_builder.multiplechoicefield': {
            'Meta': {'object_name': 'MultipleChoiceField'},
            'choices': ('django.db.models.fields.TextField', [], {}),
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ident': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'form_builder.savedatahandler': {
            'Meta': {'object_name': 'SaveDataHandler'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'form_builder.submitbutton': {
            'Meta': {'object_name': 'SubmitButton'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'default': "u'submit'", 'max_length': '255'})
        },
        u'form_builder.successhandlers': {
            'Meta': {'object_name': 'SuccessHandlers'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'form_builder.successmessagebucket': {
            'Meta': {'object_name': 'SuccessMessageBucket'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'form_builder.textarea': {
            'Meta': {'object_name': 'Textarea'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ident': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'form_builder.uncaptcha': {
            'Meta': {'object_name': 'Uncaptcha'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'form_builder.webtoleadmapperhandler': {
            'Meta': {'object_name': 'WebToLeadMapperHandler'},
            'container_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'oid': ('django.db.models.fields.CharField', [], {'max_length': '16'})
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

    complete_apps = ['form_builder']