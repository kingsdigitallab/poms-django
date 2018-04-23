# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LegendItem'
        db.create_table('sna_legenditem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('visualisation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sna.GephiVis'])),
            ('category_description', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('red', self.gf('django.db.models.fields.IntegerField')(default=255)),
            ('green', self.gf('django.db.models.fields.IntegerField')(default=255)),
            ('blue', self.gf('django.db.models.fields.IntegerField')(default=255)),
        ))
        db.send_create_signal('sna', ['LegendItem'])


    def backwards(self, orm):
        # Deleting model 'LegendItem'
        db.delete_table('sna_legenditem')


    models = {
        'sna.gephivis': {
            'Meta': {'object_name': 'GephiVis'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'style': ('django.db.models.fields.CharField', [], {'default': "'Curvy'", 'max_length': "'20'"})
        },
        'sna.legenditem': {
            'Meta': {'object_name': 'LegendItem'},
            'blue': ('django.db.models.fields.IntegerField', [], {'default': '255'}),
            'category_description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'green': ('django.db.models.fields.IntegerField', [], {'default': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'red': ('django.db.models.fields.IntegerField', [], {'default': '255'}),
            'visualisation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sna.GephiVis']"})
        }
    }

    complete_apps = ['sna']