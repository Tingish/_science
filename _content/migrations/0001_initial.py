# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StructureNode'
        db.create_table(u'_content_structurenode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pubDate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['_content.StructureNode'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True, blank=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('isPublished', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200, blank=True)),
            ('position', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'_content', ['StructureNode'])

        # Adding unique constraint on 'StructureNode', fields ['parent', 'position']
        db.create_unique(u'_content_structurenode', ['parent_id', 'position'])

        # Adding model 'Rating'
        db.create_table(u'_content_rating', (
            ('structureNode', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['_content.StructureNode'], unique=True, primary_key=True)),
            ('rating', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'_content', ['Rating'])

        # Adding model 'ViewCount'
        db.create_table(u'_content_viewcount', (
            ('structureNode', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['_content.StructureNode'], unique=True, primary_key=True)),
            ('viewCount', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'_content', ['ViewCount'])

        # Adding model 'Paragraph'
        db.create_table(u'_content_paragraph', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'_content', ['Paragraph'])

        # Adding model 'Image'
        db.create_table(u'_content_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('linkSource', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('localSource', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'_content', ['Image'])

        # Adding model 'Timelike'
        db.create_table(u'_content_timelike', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('linkSource', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('localSource', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'_content', ['Timelike'])


    def backwards(self, orm):
        # Removing unique constraint on 'StructureNode', fields ['parent', 'position']
        db.delete_unique(u'_content_structurenode', ['parent_id', 'position'])

        # Deleting model 'StructureNode'
        db.delete_table(u'_content_structurenode')

        # Deleting model 'Rating'
        db.delete_table(u'_content_rating')

        # Deleting model 'ViewCount'
        db.delete_table(u'_content_viewcount')

        # Deleting model 'Paragraph'
        db.delete_table(u'_content_paragraph')

        # Deleting model 'Image'
        db.delete_table(u'_content_image')

        # Deleting model 'Timelike'
        db.delete_table(u'_content_timelike')


    models = {
        u'_content.image': {
            'Meta': {'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkSource': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'localSource': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'_content.paragraph': {
            'Meta': {'object_name': 'Paragraph'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'_content.rating': {
            'Meta': {'object_name': 'Rating'},
            'rating': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'structureNode': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['_content.StructureNode']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'_content.structurenode': {
            'Meta': {'unique_together': "(('parent', 'position'),)", 'object_name': 'StructureNode'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isPublished': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['_content.StructureNode']"}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'pubDate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'_content.timelike': {
            'Meta': {'object_name': 'Timelike'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkSource': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'localSource': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'_content.viewcount': {
            'Meta': {'object_name': 'ViewCount'},
            'structureNode': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['_content.StructureNode']", 'unique': 'True', 'primary_key': 'True'}),
            'viewCount': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['_content']