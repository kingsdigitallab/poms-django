# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GephiVis'
        db.create_table('sna_gephivis', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=500)),
            ('style', self.gf('django.db.models.fields.CharField')(default='Curvy', max_length='20')),
        ))
        db.send_create_signal('sna', ['GephiVis'])


    def backwards(self, orm):
        # Deleting model 'GephiVis'
        db.delete_table('sna_gephivis')


    models = {
        'sna.gephivis': {
            'Meta': {'object_name': 'GephiVis'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'style': ('django.db.models.fields.CharField', [], {'default': "'Curvy'", 'max_length': "'20'"})
        }
    }

    complete_apps = ['sna']