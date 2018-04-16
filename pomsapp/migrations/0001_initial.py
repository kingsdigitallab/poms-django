# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DocTickboxes'
        db.create_table('pomsapp_doctickboxes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_doctickboxes', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_doctickboxes', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('pomsapp', ['DocTickboxes'])

        # Adding model 'TransTickboxes'
        db.create_table('pomsapp_transtickboxes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_transtickboxes', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_transtickboxes', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('pomsapp', ['TransTickboxes'])

        # Adding model 'GrantorCategory'
        db.create_table('pomsapp_grantorcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_grantorcategory', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_grantorcategory', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('pomsapp', ['GrantorCategory'])

        # Adding model 'MatrixShape'
        db.create_table('pomsapp_matrixshape', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_matrixshape', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_matrixshape', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('pomsapp', ['MatrixShape'])

        # Adding model 'SealColor'
        db.create_table('pomsapp_sealcolor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_sealcolor', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_sealcolor', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('pomsapp', ['SealColor'])

        # Adding model 'AttachmentType'
        db.create_table('pomsapp_attachmenttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_attachmenttype', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_attachmenttype', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('pomsapp', ['AttachmentType'])

        # Adding model 'Role'
        db.create_table('pomsapp_role', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_role', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_role', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('spiritualbenefit', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pomsapp', ['Role'])

        # Adding model 'TitleType'
        db.create_table('pomsapp_titletype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_titletype', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_titletype', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('placefk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Place'], null=True, blank=True)),
        ))
        db.send_create_signal('pomsapp', ['TitleType'])

        # Adding model 'Floruit'
        db.create_table('pomsapp_floruit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_floruit', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_floruit', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('eml', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('century', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('startyear', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('endyear', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('pomsapp', ['Floruit'])

        # Adding model 'Gender'
        db.create_table('pomsapp_gender', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_gender', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_gender', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('pomsapp', ['Gender'])

        # Adding model 'Chartertype'
        db.create_table('pomsapp_chartertype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_chartertype', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_chartertype', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('pomsapp', ['Chartertype'])

        # Adding model 'Relationshipmetatype'
        db.create_table('pomsapp_relationshipmetatype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_relationshipmetatype', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_relationshipmetatype', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('pomsapp', ['Relationshipmetatype'])

        # Adding model 'Relationshiptype'
        db.create_table('pomsapp_relationshiptype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_relationshiptype', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_relationshiptype', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('metatype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Relationshipmetatype'], null=True, blank=True)),
        ))
        db.send_create_signal('pomsapp', ['Relationshiptype'])

        # Adding model 'Referencetype'
        db.create_table('pomsapp_referencetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_referencetype', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_referencetype', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('pomsapp', ['Referencetype'])

        # Adding model 'Occupationtype'
        db.create_table('pomsapp_occupationtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_occupationtype', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_occupationtype', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('pomsapp', ['Occupationtype'])

        # Adding model 'Exemptiontype'
        db.create_table('pomsapp_exemptiontype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_exemptiontype', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_exemptiontype', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('pomsapp', ['Exemptiontype'])

        # Adding model 'Nominalrendertype'
        db.create_table('pomsapp_nominalrendertype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_nominalrendertype', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_nominalrendertype', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('pomsapp', ['Nominalrendertype'])

        # Adding model 'Proanimagenerictypes'
        db.create_table('pomsapp_proanimagenerictypes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_proanimagenerictypes', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_proanimagenerictypes', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('orderno', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('newline', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('pomsapp', ['Proanimagenerictypes'])

        # Adding model 'Renderdate'
        db.create_table('pomsapp_renderdate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_renderdate', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_renderdate', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('pomsapp', ['Renderdate'])

        # Adding model 'Sicutclausetype'
        db.create_table('pomsapp_sicutclausetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_sicutclausetype', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_sicutclausetype', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('orderno', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('newline', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('pomsapp', ['Sicutclausetype'])

        # Adding model 'Tenendasclauseoptions'
        db.create_table('pomsapp_tenendasclauseoptions', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_tenendasclauseoptions', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_tenendasclauseoptions', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('pomsapp', ['Tenendasclauseoptions'])

        # Adding model 'Transactiontype'
        db.create_table('pomsapp_transactiontype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_transactiontype', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_transactiontype', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('pomsapp', ['Transactiontype'])

        # Adding model 'LegalPertinents'
        db.create_table('pomsapp_legalpertinents', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_legalpertinents', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_legalpertinents', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('pomsapp', ['LegalPertinents'])

        # Adding model 'Returns_military'
        db.create_table('pomsapp_returns_military', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_returns_military', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_returns_military', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('pomsapp', ['Returns_military'])

        # Adding model 'Returns_renders'
        db.create_table('pomsapp_returns_renders', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_returns_renders', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_returns_renders', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('pomsapp', ['Returns_renders'])

        # Adding model 'CommonBurdens'
        db.create_table('pomsapp_commonburdens', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_commonburdens', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_commonburdens', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('pomsapp', ['CommonBurdens'])

        # Adding model 'Language'
        db.create_table('pomsapp_language', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_language', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_language', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('pomsapp', ['Language'])

        # Adding model 'MedievalGaelicForename'
        db.create_table('pomsapp_medievalgaelicforename', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_medievalgaelicforename', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_medievalgaelicforename', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('audiofile', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('pomsapp', ['MedievalGaelicForename'])

        # Adding model 'ModernGaelicForename'
        db.create_table('pomsapp_moderngaelicforename', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_moderngaelicforename', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_moderngaelicforename', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('audiofile', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('pomsapp', ['ModernGaelicForename'])

        # Adding model 'Privileges'
        db.create_table('pomsapp_privileges', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_privileges', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_privileges', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('nameextension', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['pomsapp.Privileges'])),
            ('extraid', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Place'], null=True, blank=True)),
            ('util_topancestor', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('helper_name', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('pomsapp', ['Privileges'])

        # Adding model 'PossessionNew'
        db.create_table('pomsapp_possessionnew', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_possessionnew', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_possessionnew', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('nameextension', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('extraid', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Place'], null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('util_topancestor', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('helper_name', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
        ))
        db.send_create_signal('pomsapp', ['PossessionNew'])

        # Adding model 'Poss_Alms'
        db.create_table('pomsapp_poss_alms', (
            ('possessionnew_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pomsapp.PossessionNew'], unique=True, primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['pomsapp.Poss_Alms'])),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('pomsapp', ['Poss_Alms'])

        # Adding model 'Poss_Lands'
        db.create_table('pomsapp_poss_lands', (
            ('possessionnew_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pomsapp.PossessionNew'], unique=True, primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['pomsapp.Poss_Lands'])),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('pomsapp', ['Poss_Lands'])

        # Adding model 'Poss_Objects'
        db.create_table('pomsapp_poss_objects', (
            ('possessionnew_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pomsapp.PossessionNew'], unique=True, primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['pomsapp.Poss_Objects'])),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('pomsapp', ['Poss_Objects'])

        # Adding model 'Poss_Revenues_silver'
        db.create_table('pomsapp_poss_revenues_silver', (
            ('possessionnew_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pomsapp.PossessionNew'], unique=True, primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['pomsapp.Poss_Revenues_silver'])),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('pomsapp', ['Poss_Revenues_silver'])

        # Adding model 'Poss_Revenues_kind'
        db.create_table('pomsapp_poss_revenues_kind', (
            ('possessionnew_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pomsapp.PossessionNew'], unique=True, primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['pomsapp.Poss_Revenues_kind'])),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('pomsapp', ['Poss_Revenues_kind'])

        # Adding model 'Poss_General'
        db.create_table('pomsapp_poss_general', (
            ('possessionnew_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pomsapp.PossessionNew'], unique=True, primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['pomsapp.Poss_General'])),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('pomsapp', ['Poss_General'])

        # Adding model 'Poss_Office'
        db.create_table('pomsapp_poss_office', (
            ('possessionnew_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pomsapp.PossessionNew'], unique=True, primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['pomsapp.Poss_Office'])),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('pomsapp', ['Poss_Office'])

        # Adding model 'Poss_Unfree_persons'
        db.create_table('pomsapp_poss_unfree_persons', (
            ('possessionnew_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pomsapp.PossessionNew'], unique=True, primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['pomsapp.Poss_Unfree_persons'])),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('pomsapp', ['Poss_Unfree_persons'])

        # Adding model 'AssocFactoidPerson'
        db.create_table('pomsapp_assocfactoidperson', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('factoid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Factoid'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Person'])),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Role'], null=True, blank=True)),
            ('nameoriglang', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('nametranslation', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('standardmedievalform', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('orderno', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('pomsapp', ['AssocFactoidPerson'])

        # Adding model 'AssocFactoidWitness'
        db.create_table('pomsapp_assocfactoidwitness', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('factoid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Factoid'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Person'])),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(default=4, to=orm['pomsapp.Role'], null=True, blank=True)),
            ('nameoriglang', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('nametranslation', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('standardmedievalform', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('orderno', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('pomsapp', ['AssocFactoidWitness'])

        # Adding model 'AssocFactoidProanima'
        db.create_table('pomsapp_assocfactoidproanima', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('factoidtrans', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Factoid'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Person'])),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(default=14, to=orm['pomsapp.Role'], null=True, blank=True)),
            ('nameoriglang', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('nametranslation', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('standardmedievalform', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('orderno', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('pomsapp', ['AssocFactoidProanima'])

        # Adding model 'AssocHelperPerson'
        db.create_table('pomsapp_assochelperperson', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('factoid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Factoid'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Person'])),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Role'], null=True, blank=True)),
            ('nameoriglang', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('nametranslation', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('standardmedievalform', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('orderno', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('helper_oldid', self.gf('django.db.models.fields.IntegerField')()),
            ('helper_type', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('pomsapp', ['AssocHelperPerson'])

        # Adding model 'AssocFactoidPoss_alms'
        db.create_table('pomsapp_assocfactoidposs_alms', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('factoid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Factoid'])),
            ('poss_alms', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Poss_Alms'])),
            ('originaltext', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('helper_inferred', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pomsapp', ['AssocFactoidPoss_alms'])

        # Adding model 'AssocFactoidPoss_unfreep'
        db.create_table('pomsapp_assocfactoidposs_unfreep', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('factoid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Factoid'])),
            ('poss_unfree_persons', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Poss_Unfree_persons'])),
            ('originaltext', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('helper_inferred', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pomsapp', ['AssocFactoidPoss_unfreep'])

        # Adding model 'AssocFactoidPoss_revenuesilver'
        db.create_table('pomsapp_assocfactoidposs_revenuesilver', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('factoid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Factoid'])),
            ('poss_revsilver', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Poss_Revenues_silver'])),
            ('originaltext', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('helper_inferred', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pomsapp', ['AssocFactoidPoss_revenuesilver'])

        # Adding model 'AssocFactoidPoss_revenuekind'
        db.create_table('pomsapp_assocfactoidposs_revenuekind', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('factoid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Factoid'])),
            ('poss_revkind', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Poss_Revenues_kind'])),
            ('originaltext', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('helper_inferred', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pomsapp', ['AssocFactoidPoss_revenuekind'])

        # Adding model 'AssocFactoidPoss_pgeneral'
        db.create_table('pomsapp_assocfactoidposs_pgeneral', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('factoid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Factoid'])),
            ('poss_pgeneral', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Poss_General'])),
            ('originaltext', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('helper_inferred', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pomsapp', ['AssocFactoidPoss_pgeneral'])

        # Adding model 'AssocFactoidPoss_office'
        db.create_table('pomsapp_assocfactoidposs_office', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('factoid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Factoid'])),
            ('poss_office', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Poss_Office'])),
            ('originaltext', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('helper_inferred', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pomsapp', ['AssocFactoidPoss_office'])

        # Adding model 'AssocFactoidPoss_objects'
        db.create_table('pomsapp_assocfactoidposs_objects', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('factoid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Factoid'])),
            ('poss_object', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Poss_Objects'])),
            ('originaltext', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('helper_inferred', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pomsapp', ['AssocFactoidPoss_objects'])

        # Adding model 'AssocFactoidPoss_lands'
        db.create_table('pomsapp_assocfactoidposs_lands', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('factoid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Factoid'])),
            ('poss_land', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Poss_Lands'])),
            ('originaltext', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('helper_inferred', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pomsapp', ['AssocFactoidPoss_lands'])

        # Adding model 'AssocFactoidPrivileges'
        db.create_table('pomsapp_assocfactoidprivileges', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('factoid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Factoid'])),
            ('privilege', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Privileges'])),
            ('originaltext', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('helper_inferred', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pomsapp', ['AssocFactoidPrivileges'])

        # Adding model 'Person'
        db.create_table('pomsapp_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_person', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_person', null=True, to=orm['auth.User'])),
            ('persondisplayname', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('standardmedievalname', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('moderngaelicname', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('persondescription', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('floruitstartpre', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('floruitstartyr', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('floruitstartpost', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('floruitendpre', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('floruitendyr', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('floruitendpost', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('florlowkey', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='flor_lowKey', null=True, to=orm['pomsapp.Floruit'])),
            ('florhikey', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='flor_hiKey', null=True, to=orm['pomsapp.Floruit'])),
            ('genderkey', self.gf('django.db.models.fields.related.ForeignKey')(default=3, to=orm['pomsapp.Gender'], null=True, blank=True)),
            ('forename', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('sonof', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('patronym', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('ofstring', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('placeandinst', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('datestring', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('searchsurname', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('moderngaelicforename', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.ModernGaelicForename'], null=True, blank=True)),
            ('moderngaelicsurname', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('medievalgaelicforename', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.MedievalGaelicForename'], null=True, blank=True)),
            ('medievalgaelicsurname', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('relatedplace', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Place'], null=True, blank=True)),
            ('helper_floruits', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('helper_merge', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('helper_bigsurname', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('helper_searchbigsur', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('helper_keywordsearch', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('helper_totfactoids', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('helper_daterange', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('pomsapp', ['Person'])

        # Adding M2M table for field helper_places on 'Person'
        m2m_table_name = db.shorten_name('pomsapp_person_helper_places')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm['pomsapp.person'], null=False)),
            ('place', models.ForeignKey(orm['pomsapp.place'], null=False))
        ))
        db.create_unique(m2m_table_name, ['person_id', 'place_id'])

        # Adding model 'Source'
        db.create_table('pomsapp_source', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_source', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_source', null=True, to=orm['auth.User'])),
            ('source_tradid', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('sourcefordataentry', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('hammondnumber', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('hammondnumb2', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('hammondnumb3', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('hammondext', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('firmdate', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('has_firmdate', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_firmdayonly', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('undated', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('eitheror', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('from_modifier', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('from_weekday', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
            ('from_day', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('from_modifier2', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('from_month', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('from_season', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
            ('from_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('to_modifier', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('to_weekday', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
            ('to_day', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
            ('to_modifier2', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('to_month', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
            ('to_season', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
            ('to_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('probabledate', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('datingnotes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['pomsapp.Language'], null=True, blank=True)),
            ('grantor_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.GrantorCategory'], null=True, blank=True)),
            ('helper_hammond', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('helper_keywordsearch', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('helper_daterange', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('helper_totfactoids', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('pomsapp', ['Source'])

        # Adding model 'Charter'
        db.create_table('pomsapp_charter', (
            ('source_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pomsapp.Source'], unique=True, primary_key=True)),
            ('chartertypekey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Chartertype'], null=True, blank=True)),
            ('ischirograph', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('doctypenotes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('placedatemodern', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('placedatedoc', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('placefk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Place'], null=True, blank=True)),
            ('letterpatent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('origcontemp', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('duporigcontemp', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('orignoncontemp', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('duporignoncontemp', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('helper_hnumber', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('helper_copydates', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('pomsapp', ['Charter'])

        # Adding M2M table for field helper_tickboxes on 'Charter'
        m2m_table_name = db.shorten_name('pomsapp_charter_helper_tickboxes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('charter', models.ForeignKey(orm['pomsapp.charter'], null=False)),
            ('doctickboxes', models.ForeignKey(orm['pomsapp.doctickboxes'], null=False))
        ))
        db.create_unique(m2m_table_name, ['charter_id', 'doctickboxes_id'])

        # Adding model 'Matrix'
        db.create_table('pomsapp_matrix', (
            ('source_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pomsapp.Source'], unique=True, primary_key=True)),
            ('shape', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.MatrixShape'], null=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Person'], null=True, blank=True)),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('image_desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image_desc_rev', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('legend_obv', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('legend_rev', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('catalogue', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
        ))
        db.send_create_signal('pomsapp', ['Matrix'])

        # Adding model 'Seal'
        db.create_table('pomsapp_seal', (
            ('source_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pomsapp.Source'], unique=True, primary_key=True)),
            ('charter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Charter'], null=True, blank=True)),
            ('matrix', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Matrix'])),
            ('color', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.SealColor'], null=True, blank=True)),
            ('att_type_surv', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='surv_attach_of', null=True, to=orm['pomsapp.AttachmentType'])),
            ('countersealed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('archive', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('archiverefnumber', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('conditionnote', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('scranlink', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('pomsapp', ['Seal'])

        # Adding model 'Factoid'
        db.create_table('pomsapp_factoid', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_factoid', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_factoid', null=True, to=orm['auth.User'])),
            ('inferred_type', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('sourcekey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Source'])),
            ('shortdesc', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('has_firmdate', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_firmdayonly', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('firmdate', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('undated', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('eitheror', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('from_modifier', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('from_weekday', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
            ('from_day', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('from_modifier2', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('from_month', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('from_season', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
            ('from_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('to_modifier', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('to_weekday', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
            ('to_day', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
            ('to_modifier2', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('to_month', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
            ('to_season', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
            ('to_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('probabledate', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('datingnotes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('problems', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('sourceref', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('helper_floruits', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('helper_keywordsearch', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('helper_daterange', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('pomsapp', ['Factoid'])

        # Adding M2M table for field helper_places on 'Factoid'
        m2m_table_name = db.shorten_name('pomsapp_factoid_helper_places')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('factoid', models.ForeignKey(orm['pomsapp.factoid'], null=False)),
            ('place', models.ForeignKey(orm['pomsapp.place'], null=False))
        ))
        db.create_unique(m2m_table_name, ['factoid_id', 'place_id'])

        # Adding model 'FactTitle'
        db.create_table('pomsapp_facttitle', (
            ('factoid_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pomsapp.Factoid'], unique=True, primary_key=True)),
            ('titletypekey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.TitleType'])),
            ('bygraceofgod', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('byanotherdivineinvocation', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pomsapp', ['FactTitle'])

        # Adding model 'FactRelationship'
        db.create_table('pomsapp_factrelationship', (
            ('factoid_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pomsapp.Factoid'], unique=True, primary_key=True)),
            ('relationship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Relationshiptype'], null=True, blank=True)),
            ('placefielty', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Place'], null=True, blank=True)),
        ))
        db.send_create_signal('pomsapp', ['FactRelationship'])

        # Adding model 'FactReference'
        db.create_table('pomsapp_factreference', (
            ('factoid_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pomsapp.Factoid'], unique=True, primary_key=True)),
            ('reference', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Referencetype'], null=True, blank=True)),
            ('placefielty', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Place'], null=True, blank=True)),
        ))
        db.send_create_signal('pomsapp', ['FactReference'])

        # Adding model 'FactPossession'
        db.create_table('pomsapp_factpossession', (
            ('factoid_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pomsapp.Factoid'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('pomsapp', ['FactPossession'])

        # Adding model 'FactTransaction'
        db.create_table('pomsapp_facttransaction', (
            ('factoid_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pomsapp.Factoid'], unique=True, primary_key=True)),
            ('transactiontype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pomsapp.Transactiontype'], null=True, blank=True)),
            ('isprimary', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isdare', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isexchange', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('verbsnotspecified', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('conveth', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('genericwitnesses', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('testemeipso', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tenendasclauseolang', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('exemptionclauseolang', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('previouschartermention', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('previouschirographmention', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('perambulation', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('corroborationsealing', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ismalediction', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('bothaddressorsmentioned', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('warrandice', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pomsapp', ['FactTransaction'])

        # Adding M2M table for field tenendas on 'FactTransaction'
        m2m_table_name = db.shorten_name('pomsapp_facttransaction_tenendas')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('facttransaction', models.ForeignKey(orm['pomsapp.facttransaction'], null=False)),
            ('tenendasclauseoptions', models.ForeignKey(orm['pomsapp.tenendasclauseoptions'], null=False))
        ))
        db.create_unique(m2m_table_name, ['facttransaction_id', 'tenendasclauseoptions_id'])

        # Adding M2M table for field exemptions on 'FactTransaction'
        m2m_table_name = db.shorten_name('pomsapp_facttransaction_exemptions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('facttransaction', models.ForeignKey(orm['pomsapp.facttransaction'], null=False)),
            ('exemptiontype', models.ForeignKey(orm['pomsapp.exemptiontype'], null=False))
        ))
        db.create_unique(m2m_table_name, ['facttransaction_id', 'exemptiontype_id'])

        # Adding M2M table for field renderdates on 'FactTransaction'
        m2m_table_name = db.shorten_name('pomsapp_facttransaction_renderdates')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('facttransaction', models.ForeignKey(orm['pomsapp.facttransaction'], null=False)),
            ('renderdate', models.ForeignKey(orm['pomsapp.renderdate'], null=False))
        ))
        db.create_unique(m2m_table_name, ['facttransaction_id', 'renderdate_id'])

        # Adding M2M table for field rendernominal on 'FactTransaction'
        m2m_table_name = db.shorten_name('pomsapp_facttransaction_rendernominal')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('facttransaction', models.ForeignKey(orm['pomsapp.facttransaction'], null=False)),
            ('nominalrendertype', models.ForeignKey(orm['pomsapp.nominalrendertype'], null=False))
        ))
        db.create_unique(m2m_table_name, ['facttransaction_id', 'nominalrendertype_id'])

        # Adding M2M table for field sicutclauses on 'FactTransaction'
        m2m_table_name = db.shorten_name('pomsapp_facttransaction_sicutclauses')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('facttransaction', models.ForeignKey(orm['pomsapp.facttransaction'], null=False)),
            ('sicutclausetype', models.ForeignKey(orm['pomsapp.sicutclausetype'], null=False))
        ))
        db.create_unique(m2m_table_name, ['facttransaction_id', 'sicutclausetype_id'])

        # Adding M2M table for field legalpertinents on 'FactTransaction'
        m2m_table_name = db.shorten_name('pomsapp_facttransaction_legalpertinents')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('facttransaction', models.ForeignKey(orm['pomsapp.facttransaction'], null=False)),
            ('legalpertinents', models.ForeignKey(orm['pomsapp.legalpertinents'], null=False))
        ))
        db.create_unique(m2m_table_name, ['facttransaction_id', 'legalpertinents_id'])

        # Adding M2M table for field returnsmilitary on 'FactTransaction'
        m2m_table_name = db.shorten_name('pomsapp_facttransaction_returnsmilitary')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('facttransaction', models.ForeignKey(orm['pomsapp.facttransaction'], null=False)),
            ('returns_military', models.ForeignKey(orm['pomsapp.returns_military'], null=False))
        ))
        db.create_unique(m2m_table_name, ['facttransaction_id', 'returns_military_id'])

        # Adding M2M table for field returnsrenders on 'FactTransaction'
        m2m_table_name = db.shorten_name('pomsapp_facttransaction_returnsrenders')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('facttransaction', models.ForeignKey(orm['pomsapp.facttransaction'], null=False)),
            ('returns_renders', models.ForeignKey(orm['pomsapp.returns_renders'], null=False))
        ))
        db.create_unique(m2m_table_name, ['facttransaction_id', 'returns_renders_id'])

        # Adding M2M table for field commonburdens on 'FactTransaction'
        m2m_table_name = db.shorten_name('pomsapp_facttransaction_commonburdens')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('facttransaction', models.ForeignKey(orm['pomsapp.facttransaction'], null=False)),
            ('commonburdens', models.ForeignKey(orm['pomsapp.commonburdens'], null=False))
        ))
        db.create_unique(m2m_table_name, ['facttransaction_id', 'commonburdens_id'])

        # Adding M2M table for field spiritualbenefits on 'FactTransaction'
        m2m_table_name = db.shorten_name('pomsapp_facttransaction_spiritualbenefits')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('facttransaction', models.ForeignKey(orm['pomsapp.facttransaction'], null=False)),
            ('proanimagenerictypes', models.ForeignKey(orm['pomsapp.proanimagenerictypes'], null=False))
        ))
        db.create_unique(m2m_table_name, ['facttransaction_id', 'proanimagenerictypes_id'])

        # Adding M2M table for field helper_tickboxes on 'FactTransaction'
        m2m_table_name = db.shorten_name('pomsapp_facttransaction_helper_tickboxes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('facttransaction', models.ForeignKey(orm['pomsapp.facttransaction'], null=False)),
            ('transtickboxes', models.ForeignKey(orm['pomsapp.transtickboxes'], null=False))
        ))
        db.create_unique(m2m_table_name, ['facttransaction_id', 'transtickboxes_id'])

        # Adding model 'Place'
        db.create_table('pomsapp_place', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('utils.modelextra.myfields.CreationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('updated_at', self.gf('utils.modelextra.myfields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True)),
            ('editedrecord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internal_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_place', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='updated_place', null=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('genericname', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('articletext', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('specificname', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['pomsapp.Place'])),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('util_topancestor', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('helper_name', self.gf('django.db.models.fields.CharField')(max_length=765, null=True, blank=True)),
            ('helper_keywordsearch', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('pomsapp', ['Place'])


    def backwards(self, orm):
        # Deleting model 'DocTickboxes'
        db.delete_table('pomsapp_doctickboxes')

        # Deleting model 'TransTickboxes'
        db.delete_table('pomsapp_transtickboxes')

        # Deleting model 'GrantorCategory'
        db.delete_table('pomsapp_grantorcategory')

        # Deleting model 'MatrixShape'
        db.delete_table('pomsapp_matrixshape')

        # Deleting model 'SealColor'
        db.delete_table('pomsapp_sealcolor')

        # Deleting model 'AttachmentType'
        db.delete_table('pomsapp_attachmenttype')

        # Deleting model 'Role'
        db.delete_table('pomsapp_role')

        # Deleting model 'TitleType'
        db.delete_table('pomsapp_titletype')

        # Deleting model 'Floruit'
        db.delete_table('pomsapp_floruit')

        # Deleting model 'Gender'
        db.delete_table('pomsapp_gender')

        # Deleting model 'Chartertype'
        db.delete_table('pomsapp_chartertype')

        # Deleting model 'Relationshipmetatype'
        db.delete_table('pomsapp_relationshipmetatype')

        # Deleting model 'Relationshiptype'
        db.delete_table('pomsapp_relationshiptype')

        # Deleting model 'Referencetype'
        db.delete_table('pomsapp_referencetype')

        # Deleting model 'Occupationtype'
        db.delete_table('pomsapp_occupationtype')

        # Deleting model 'Exemptiontype'
        db.delete_table('pomsapp_exemptiontype')

        # Deleting model 'Nominalrendertype'
        db.delete_table('pomsapp_nominalrendertype')

        # Deleting model 'Proanimagenerictypes'
        db.delete_table('pomsapp_proanimagenerictypes')

        # Deleting model 'Renderdate'
        db.delete_table('pomsapp_renderdate')

        # Deleting model 'Sicutclausetype'
        db.delete_table('pomsapp_sicutclausetype')

        # Deleting model 'Tenendasclauseoptions'
        db.delete_table('pomsapp_tenendasclauseoptions')

        # Deleting model 'Transactiontype'
        db.delete_table('pomsapp_transactiontype')

        # Deleting model 'LegalPertinents'
        db.delete_table('pomsapp_legalpertinents')

        # Deleting model 'Returns_military'
        db.delete_table('pomsapp_returns_military')

        # Deleting model 'Returns_renders'
        db.delete_table('pomsapp_returns_renders')

        # Deleting model 'CommonBurdens'
        db.delete_table('pomsapp_commonburdens')

        # Deleting model 'Language'
        db.delete_table('pomsapp_language')

        # Deleting model 'MedievalGaelicForename'
        db.delete_table('pomsapp_medievalgaelicforename')

        # Deleting model 'ModernGaelicForename'
        db.delete_table('pomsapp_moderngaelicforename')

        # Deleting model 'Privileges'
        db.delete_table('pomsapp_privileges')

        # Deleting model 'PossessionNew'
        db.delete_table('pomsapp_possessionnew')

        # Deleting model 'Poss_Alms'
        db.delete_table('pomsapp_poss_alms')

        # Deleting model 'Poss_Lands'
        db.delete_table('pomsapp_poss_lands')

        # Deleting model 'Poss_Objects'
        db.delete_table('pomsapp_poss_objects')

        # Deleting model 'Poss_Revenues_silver'
        db.delete_table('pomsapp_poss_revenues_silver')

        # Deleting model 'Poss_Revenues_kind'
        db.delete_table('pomsapp_poss_revenues_kind')

        # Deleting model 'Poss_General'
        db.delete_table('pomsapp_poss_general')

        # Deleting model 'Poss_Office'
        db.delete_table('pomsapp_poss_office')

        # Deleting model 'Poss_Unfree_persons'
        db.delete_table('pomsapp_poss_unfree_persons')

        # Deleting model 'AssocFactoidPerson'
        db.delete_table('pomsapp_assocfactoidperson')

        # Deleting model 'AssocFactoidWitness'
        db.delete_table('pomsapp_assocfactoidwitness')

        # Deleting model 'AssocFactoidProanima'
        db.delete_table('pomsapp_assocfactoidproanima')

        # Deleting model 'AssocHelperPerson'
        db.delete_table('pomsapp_assochelperperson')

        # Deleting model 'AssocFactoidPoss_alms'
        db.delete_table('pomsapp_assocfactoidposs_alms')

        # Deleting model 'AssocFactoidPoss_unfreep'
        db.delete_table('pomsapp_assocfactoidposs_unfreep')

        # Deleting model 'AssocFactoidPoss_revenuesilver'
        db.delete_table('pomsapp_assocfactoidposs_revenuesilver')

        # Deleting model 'AssocFactoidPoss_revenuekind'
        db.delete_table('pomsapp_assocfactoidposs_revenuekind')

        # Deleting model 'AssocFactoidPoss_pgeneral'
        db.delete_table('pomsapp_assocfactoidposs_pgeneral')

        # Deleting model 'AssocFactoidPoss_office'
        db.delete_table('pomsapp_assocfactoidposs_office')

        # Deleting model 'AssocFactoidPoss_objects'
        db.delete_table('pomsapp_assocfactoidposs_objects')

        # Deleting model 'AssocFactoidPoss_lands'
        db.delete_table('pomsapp_assocfactoidposs_lands')

        # Deleting model 'AssocFactoidPrivileges'
        db.delete_table('pomsapp_assocfactoidprivileges')

        # Deleting model 'Person'
        db.delete_table('pomsapp_person')

        # Removing M2M table for field helper_places on 'Person'
        db.delete_table(db.shorten_name('pomsapp_person_helper_places'))

        # Deleting model 'Source'
        db.delete_table('pomsapp_source')

        # Deleting model 'Charter'
        db.delete_table('pomsapp_charter')

        # Removing M2M table for field helper_tickboxes on 'Charter'
        db.delete_table(db.shorten_name('pomsapp_charter_helper_tickboxes'))

        # Deleting model 'Matrix'
        db.delete_table('pomsapp_matrix')

        # Deleting model 'Seal'
        db.delete_table('pomsapp_seal')

        # Deleting model 'Factoid'
        db.delete_table('pomsapp_factoid')

        # Removing M2M table for field helper_places on 'Factoid'
        db.delete_table(db.shorten_name('pomsapp_factoid_helper_places'))

        # Deleting model 'FactTitle'
        db.delete_table('pomsapp_facttitle')

        # Deleting model 'FactRelationship'
        db.delete_table('pomsapp_factrelationship')

        # Deleting model 'FactReference'
        db.delete_table('pomsapp_factreference')

        # Deleting model 'FactPossession'
        db.delete_table('pomsapp_factpossession')

        # Deleting model 'FactTransaction'
        db.delete_table('pomsapp_facttransaction')

        # Removing M2M table for field tenendas on 'FactTransaction'
        db.delete_table(db.shorten_name('pomsapp_facttransaction_tenendas'))

        # Removing M2M table for field exemptions on 'FactTransaction'
        db.delete_table(db.shorten_name('pomsapp_facttransaction_exemptions'))

        # Removing M2M table for field renderdates on 'FactTransaction'
        db.delete_table(db.shorten_name('pomsapp_facttransaction_renderdates'))

        # Removing M2M table for field rendernominal on 'FactTransaction'
        db.delete_table(db.shorten_name('pomsapp_facttransaction_rendernominal'))

        # Removing M2M table for field sicutclauses on 'FactTransaction'
        db.delete_table(db.shorten_name('pomsapp_facttransaction_sicutclauses'))

        # Removing M2M table for field legalpertinents on 'FactTransaction'
        db.delete_table(db.shorten_name('pomsapp_facttransaction_legalpertinents'))

        # Removing M2M table for field returnsmilitary on 'FactTransaction'
        db.delete_table(db.shorten_name('pomsapp_facttransaction_returnsmilitary'))

        # Removing M2M table for field returnsrenders on 'FactTransaction'
        db.delete_table(db.shorten_name('pomsapp_facttransaction_returnsrenders'))

        # Removing M2M table for field commonburdens on 'FactTransaction'
        db.delete_table(db.shorten_name('pomsapp_facttransaction_commonburdens'))

        # Removing M2M table for field spiritualbenefits on 'FactTransaction'
        db.delete_table(db.shorten_name('pomsapp_facttransaction_spiritualbenefits'))

        # Removing M2M table for field helper_tickboxes on 'FactTransaction'
        db.delete_table(db.shorten_name('pomsapp_facttransaction_helper_tickboxes'))

        # Deleting model 'Place'
        db.delete_table('pomsapp_place')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'pomsapp.assocfactoidperson': {
            'Meta': {'ordering': "['orderno']", 'object_name': 'AssocFactoidPerson'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'factoid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Factoid']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nameoriglang': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'nametranslation': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'orderno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Person']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Role']", 'null': 'True', 'blank': 'True'}),
            'standardmedievalform': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        'pomsapp.assocfactoidposs_alms': {
            'Meta': {'object_name': 'AssocFactoidPoss_alms'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'factoid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Factoid']"}),
            'helper_inferred': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'originaltext': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'poss_alms': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Poss_Alms']"}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        'pomsapp.assocfactoidposs_lands': {
            'Meta': {'object_name': 'AssocFactoidPoss_lands'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'factoid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Factoid']"}),
            'helper_inferred': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'originaltext': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'poss_land': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Poss_Lands']"}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        'pomsapp.assocfactoidposs_objects': {
            'Meta': {'object_name': 'AssocFactoidPoss_objects'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'factoid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Factoid']"}),
            'helper_inferred': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'originaltext': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'poss_object': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Poss_Objects']"}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        'pomsapp.assocfactoidposs_office': {
            'Meta': {'object_name': 'AssocFactoidPoss_office'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'factoid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Factoid']"}),
            'helper_inferred': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'originaltext': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'poss_office': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Poss_Office']"}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        'pomsapp.assocfactoidposs_pgeneral': {
            'Meta': {'object_name': 'AssocFactoidPoss_pgeneral'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'factoid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Factoid']"}),
            'helper_inferred': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'originaltext': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'poss_pgeneral': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Poss_General']"}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        'pomsapp.assocfactoidposs_revenuekind': {
            'Meta': {'object_name': 'AssocFactoidPoss_revenuekind'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'factoid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Factoid']"}),
            'helper_inferred': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'originaltext': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'poss_revkind': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Poss_Revenues_kind']"}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        'pomsapp.assocfactoidposs_revenuesilver': {
            'Meta': {'object_name': 'AssocFactoidPoss_revenuesilver'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'factoid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Factoid']"}),
            'helper_inferred': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'originaltext': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'poss_revsilver': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Poss_Revenues_silver']"}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        'pomsapp.assocfactoidposs_unfreep': {
            'Meta': {'object_name': 'AssocFactoidPoss_unfreep'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'factoid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Factoid']"}),
            'helper_inferred': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'originaltext': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'poss_unfree_persons': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Poss_Unfree_persons']"}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        'pomsapp.assocfactoidprivileges': {
            'Meta': {'object_name': 'AssocFactoidPrivileges'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'factoid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Factoid']"}),
            'helper_inferred': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'originaltext': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'privilege': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Privileges']"}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        'pomsapp.assocfactoidproanima': {
            'Meta': {'ordering': "['orderno']", 'object_name': 'AssocFactoidProanima'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'factoidtrans': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Factoid']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nameoriglang': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'nametranslation': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'orderno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Person']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'default': '14', 'to': "orm['pomsapp.Role']", 'null': 'True', 'blank': 'True'}),
            'standardmedievalform': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        'pomsapp.assocfactoidwitness': {
            'Meta': {'ordering': "['orderno']", 'object_name': 'AssocFactoidWitness'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'factoid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Factoid']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nameoriglang': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'nametranslation': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'orderno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Person']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'default': '4', 'to': "orm['pomsapp.Role']", 'null': 'True', 'blank': 'True'}),
            'standardmedievalform': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        'pomsapp.assochelperperson': {
            'Meta': {'ordering': "['orderno']", 'object_name': 'AssocHelperPerson'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'factoid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Factoid']"}),
            'helper_oldid': ('django.db.models.fields.IntegerField', [], {}),
            'helper_type': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nameoriglang': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'nametranslation': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'orderno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Person']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Role']", 'null': 'True', 'blank': 'True'}),
            'standardmedievalform': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        'pomsapp.attachmenttype': {
            'Meta': {'ordering': "['name']", 'object_name': 'AttachmentType'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_attachmenttype'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_attachmenttype'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.charter': {
            'Meta': {'object_name': 'Charter', '_ormbases': ['pomsapp.Source']},
            'chartertypekey': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Chartertype']", 'null': 'True', 'blank': 'True'}),
            'doctypenotes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'duporigcontemp': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'duporignoncontemp': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'helper_copydates': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'helper_hnumber': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'helper_tickboxes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['pomsapp.DocTickboxes']", 'null': 'True', 'blank': 'True'}),
            'ischirograph': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'letterpatent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'origcontemp': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'orignoncontemp': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'placedatedoc': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'placedatemodern': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'placefk': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Place']", 'null': 'True', 'blank': 'True'}),
            'source_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['pomsapp.Source']", 'unique': 'True', 'primary_key': 'True'})
        },
        'pomsapp.chartertype': {
            'Meta': {'ordering': "['name']", 'object_name': 'Chartertype'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_chartertype'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_chartertype'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.commonburdens': {
            'Meta': {'ordering': "['name']", 'object_name': 'CommonBurdens'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_commonburdens'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_commonburdens'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.doctickboxes': {
            'Meta': {'ordering': "['name']", 'object_name': 'DocTickboxes'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_doctickboxes'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_doctickboxes'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.exemptiontype': {
            'Meta': {'ordering': "['name']", 'object_name': 'Exemptiontype'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_exemptiontype'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_exemptiontype'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.factoid': {
            'Meta': {'ordering': "('from_year', 'from_month', 'from_day', 'to_year')", 'object_name': 'Factoid'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_factoid'", 'null': 'True', 'to': "orm['auth.User']"}),
            'datingnotes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'eitheror': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'firmdate': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'from_day': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'from_modifier': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'from_modifier2': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'from_month': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'from_season': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'from_weekday': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'from_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'has_firmdate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_firmdayonly': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'helper_daterange': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'helper_floruits': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'helper_keywordsearch': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'helper_people': ('django.db.models.fields.related.ManyToManyField', [], {'db_index': 'True', 'related_name': "'helperfactoids'", 'symmetrical': 'False', 'through': "orm['pomsapp.AssocHelperPerson']", 'to': "orm['pomsapp.Person']"}),
            'helper_places': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'helper_factoids'", 'symmetrical': 'False', 'to': "orm['pomsapp.Place']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inferred_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'people': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'factoids'", 'symmetrical': 'False', 'through': "orm['pomsapp.AssocFactoidPerson']", 'to': "orm['pomsapp.Person']"}),
            'poss_alms': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pomsapp.Poss_Alms']", 'through': "orm['pomsapp.AssocFactoidPoss_alms']", 'symmetrical': 'False'}),
            'poss_lands': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pomsapp.Poss_Lands']", 'through': "orm['pomsapp.AssocFactoidPoss_lands']", 'symmetrical': 'False'}),
            'poss_objects': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pomsapp.Poss_Objects']", 'through': "orm['pomsapp.AssocFactoidPoss_objects']", 'symmetrical': 'False'}),
            'poss_office': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pomsapp.Poss_Office']", 'through': "orm['pomsapp.AssocFactoidPoss_office']", 'symmetrical': 'False'}),
            'poss_pgeneral': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pomsapp.Poss_General']", 'through': "orm['pomsapp.AssocFactoidPoss_pgeneral']", 'symmetrical': 'False'}),
            'poss_privileges': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pomsapp.Privileges']", 'through': "orm['pomsapp.AssocFactoidPrivileges']", 'symmetrical': 'False'}),
            'poss_revkind': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pomsapp.Poss_Revenues_kind']", 'through': "orm['pomsapp.AssocFactoidPoss_revenuekind']", 'symmetrical': 'False'}),
            'poss_revsilver': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pomsapp.Poss_Revenues_silver']", 'through': "orm['pomsapp.AssocFactoidPoss_revenuesilver']", 'symmetrical': 'False'}),
            'poss_unfreep': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pomsapp.Poss_Unfree_persons']", 'through': "orm['pomsapp.AssocFactoidPoss_unfreep']", 'symmetrical': 'False'}),
            'proanimapeople': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'factoidsproanima'", 'symmetrical': 'False', 'through': "orm['pomsapp.AssocFactoidProanima']", 'to': "orm['pomsapp.Person']"}),
            'probabledate': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'problems': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'shortdesc': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'sourcekey': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Source']"}),
            'sourceref': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'to_day': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'to_modifier': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'to_modifier2': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'to_month': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'to_season': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'to_weekday': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'to_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'undated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_factoid'", 'null': 'True', 'to': "orm['auth.User']"}),
            'witnesses': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'factoidswitness'", 'symmetrical': 'False', 'through': "orm['pomsapp.AssocFactoidWitness']", 'to': "orm['pomsapp.Person']"})
        },
        'pomsapp.factpossession': {
            'Meta': {'ordering': "('from_year', 'from_month', 'from_day', 'to_year')", 'object_name': 'FactPossession', '_ormbases': ['pomsapp.Factoid']},
            'factoid_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['pomsapp.Factoid']", 'unique': 'True', 'primary_key': 'True'})
        },
        'pomsapp.factreference': {
            'Meta': {'ordering': "('from_year', 'from_month', 'from_day', 'to_year')", 'object_name': 'FactReference', '_ormbases': ['pomsapp.Factoid']},
            'factoid_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['pomsapp.Factoid']", 'unique': 'True', 'primary_key': 'True'}),
            'placefielty': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Place']", 'null': 'True', 'blank': 'True'}),
            'reference': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Referencetype']", 'null': 'True', 'blank': 'True'})
        },
        'pomsapp.factrelationship': {
            'Meta': {'ordering': "('from_year', 'from_month', 'from_day', 'to_year')", 'object_name': 'FactRelationship', '_ormbases': ['pomsapp.Factoid']},
            'factoid_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['pomsapp.Factoid']", 'unique': 'True', 'primary_key': 'True'}),
            'placefielty': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Place']", 'null': 'True', 'blank': 'True'}),
            'relationship': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Relationshiptype']", 'null': 'True', 'blank': 'True'})
        },
        'pomsapp.facttitle': {
            'Meta': {'ordering': "('from_year', 'from_month', 'from_day', 'to_year')", 'object_name': 'FactTitle', '_ormbases': ['pomsapp.Factoid']},
            'byanotherdivineinvocation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bygraceofgod': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'factoid_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['pomsapp.Factoid']", 'unique': 'True', 'primary_key': 'True'}),
            'titletypekey': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.TitleType']"})
        },
        'pomsapp.facttransaction': {
            'Meta': {'ordering': "('from_year', 'from_month', 'from_day', 'to_year')", 'object_name': 'FactTransaction', '_ormbases': ['pomsapp.Factoid']},
            'bothaddressorsmentioned': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'commonburdens': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pomsapp.CommonBurdens']", 'symmetrical': 'False', 'blank': 'True'}),
            'conveth': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'corroborationsealing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'exemptionclauseolang': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'exemptions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pomsapp.Exemptiontype']", 'symmetrical': 'False', 'blank': 'True'}),
            'factoid_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['pomsapp.Factoid']", 'unique': 'True', 'primary_key': 'True'}),
            'genericwitnesses': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'helper_tickboxes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['pomsapp.TransTickboxes']", 'null': 'True', 'blank': 'True'}),
            'isdare': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isexchange': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ismalediction': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isprimary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'legalpertinents': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pomsapp.LegalPertinents']", 'symmetrical': 'False', 'blank': 'True'}),
            'perambulation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'previouschartermention': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'previouschirographmention': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'renderdates': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pomsapp.Renderdate']", 'symmetrical': 'False', 'blank': 'True'}),
            'rendernominal': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pomsapp.Nominalrendertype']", 'symmetrical': 'False', 'blank': 'True'}),
            'returnsmilitary': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pomsapp.Returns_military']", 'symmetrical': 'False', 'blank': 'True'}),
            'returnsrenders': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pomsapp.Returns_renders']", 'symmetrical': 'False', 'blank': 'True'}),
            'sicutclauses': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pomsapp.Sicutclausetype']", 'symmetrical': 'False', 'blank': 'True'}),
            'spiritualbenefits': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pomsapp.Proanimagenerictypes']", 'symmetrical': 'False', 'blank': 'True'}),
            'tenendas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pomsapp.Tenendasclauseoptions']", 'symmetrical': 'False', 'blank': 'True'}),
            'tenendasclauseolang': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'testemeipso': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'transactiontype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Transactiontype']", 'null': 'True', 'blank': 'True'}),
            'verbsnotspecified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'warrandice': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'pomsapp.floruit': {
            'Meta': {'object_name': 'Floruit'},
            'century': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_floruit'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'eml': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'endyear': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'startyear': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_floruit'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.gender': {
            'Meta': {'ordering': "['name']", 'object_name': 'Gender'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_gender'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_gender'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.grantorcategory': {
            'Meta': {'ordering': "['name']", 'object_name': 'GrantorCategory'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_grantorcategory'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_grantorcategory'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.language': {
            'Meta': {'ordering': "['name']", 'object_name': 'Language'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_language'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_language'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.legalpertinents': {
            'Meta': {'ordering': "['name']", 'object_name': 'LegalPertinents'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_legalpertinents'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_legalpertinents'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.matrix': {
            'Meta': {'object_name': 'Matrix', '_ormbases': ['pomsapp.Source']},
            'catalogue': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'image_desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'image_desc_rev': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'legend_obv': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'legend_rev': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Person']", 'null': 'True', 'blank': 'True'}),
            'shape': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.MatrixShape']", 'null': 'True', 'blank': 'True'}),
            'source_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['pomsapp.Source']", 'unique': 'True', 'primary_key': 'True'})
        },
        'pomsapp.matrixshape': {
            'Meta': {'ordering': "['name']", 'object_name': 'MatrixShape'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_matrixshape'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_matrixshape'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.medievalgaelicforename': {
            'Meta': {'ordering': "['name']", 'object_name': 'MedievalGaelicForename'},
            'audiofile': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_medievalgaelicforename'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_medievalgaelicforename'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.moderngaelicforename': {
            'Meta': {'ordering': "['name']", 'object_name': 'ModernGaelicForename'},
            'audiofile': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_moderngaelicforename'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_moderngaelicforename'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.nominalrendertype': {
            'Meta': {'ordering': "['name']", 'object_name': 'Nominalrendertype'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_nominalrendertype'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_nominalrendertype'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.occupationtype': {
            'Meta': {'ordering': "['name']", 'object_name': 'Occupationtype'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_occupationtype'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_occupationtype'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.person': {
            'Meta': {'ordering': "['persondisplayname']", 'object_name': 'Person'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_person'", 'null': 'True', 'to': "orm['auth.User']"}),
            'datestring': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'florhikey': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'flor_hiKey'", 'null': 'True', 'to': "orm['pomsapp.Floruit']"}),
            'florlowkey': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'flor_lowKey'", 'null': 'True', 'to': "orm['pomsapp.Floruit']"}),
            'floruitendpost': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'floruitendpre': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'floruitendyr': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'floruitstartpost': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'floruitstartpre': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'floruitstartyr': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'forename': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'genderkey': ('django.db.models.fields.related.ForeignKey', [], {'default': '3', 'to': "orm['pomsapp.Gender']", 'null': 'True', 'blank': 'True'}),
            'helper_bigsurname': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'helper_daterange': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'helper_floruits': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'helper_keywordsearch': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'helper_merge': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'helper_places': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'helper_persons'", 'symmetrical': 'False', 'to': "orm['pomsapp.Place']"}),
            'helper_searchbigsur': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'helper_totfactoids': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'medievalgaelicforename': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.MedievalGaelicForename']", 'null': 'True', 'blank': 'True'}),
            'medievalgaelicsurname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'moderngaelicforename': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.ModernGaelicForename']", 'null': 'True', 'blank': 'True'}),
            'moderngaelicname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'moderngaelicsurname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'ofstring': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'patronym': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'persondescription': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'persondisplayname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'placeandinst': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'relatedplace': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Place']", 'null': 'True', 'blank': 'True'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'searchsurname': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'sonof': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'standardmedievalname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_person'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.place': {
            'Meta': {'ordering': "['tree_id', 'lft', 'name']", 'object_name': 'Place'},
            'articletext': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_place'", 'null': 'True', 'to': "orm['auth.User']"}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'genericname': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'helper_keywordsearch': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'helper_name': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['pomsapp.Place']"}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'specificname': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_place'", 'null': 'True', 'to': "orm['auth.User']"}),
            'util_topancestor': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'})
        },
        'pomsapp.poss_alms': {
            'Meta': {'ordering': "['tree_id', 'lft']", 'object_name': 'Poss_Alms', '_ormbases': ['pomsapp.PossessionNew']},
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['pomsapp.Poss_Alms']"}),
            'possessionnew_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['pomsapp.PossessionNew']", 'unique': 'True', 'primary_key': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'pomsapp.poss_general': {
            'Meta': {'ordering': "['tree_id', 'lft']", 'object_name': 'Poss_General', '_ormbases': ['pomsapp.PossessionNew']},
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['pomsapp.Poss_General']"}),
            'possessionnew_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['pomsapp.PossessionNew']", 'unique': 'True', 'primary_key': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'pomsapp.poss_lands': {
            'Meta': {'ordering': "['tree_id', 'lft']", 'object_name': 'Poss_Lands', '_ormbases': ['pomsapp.PossessionNew']},
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['pomsapp.Poss_Lands']"}),
            'possessionnew_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['pomsapp.PossessionNew']", 'unique': 'True', 'primary_key': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'pomsapp.poss_objects': {
            'Meta': {'ordering': "['tree_id', 'lft']", 'object_name': 'Poss_Objects', '_ormbases': ['pomsapp.PossessionNew']},
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['pomsapp.Poss_Objects']"}),
            'possessionnew_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['pomsapp.PossessionNew']", 'unique': 'True', 'primary_key': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'pomsapp.poss_office': {
            'Meta': {'ordering': "['tree_id', 'lft']", 'object_name': 'Poss_Office', '_ormbases': ['pomsapp.PossessionNew']},
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['pomsapp.Poss_Office']"}),
            'possessionnew_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['pomsapp.PossessionNew']", 'unique': 'True', 'primary_key': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'pomsapp.poss_revenues_kind': {
            'Meta': {'ordering': "['tree_id', 'lft']", 'object_name': 'Poss_Revenues_kind', '_ormbases': ['pomsapp.PossessionNew']},
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['pomsapp.Poss_Revenues_kind']"}),
            'possessionnew_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['pomsapp.PossessionNew']", 'unique': 'True', 'primary_key': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'pomsapp.poss_revenues_silver': {
            'Meta': {'ordering': "['tree_id', 'lft']", 'object_name': 'Poss_Revenues_silver', '_ormbases': ['pomsapp.PossessionNew']},
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['pomsapp.Poss_Revenues_silver']"}),
            'possessionnew_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['pomsapp.PossessionNew']", 'unique': 'True', 'primary_key': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'pomsapp.poss_unfree_persons': {
            'Meta': {'ordering': "['tree_id', 'lft']", 'object_name': 'Poss_Unfree_persons', '_ormbases': ['pomsapp.PossessionNew']},
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['pomsapp.Poss_Unfree_persons']"}),
            'possessionnew_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['pomsapp.PossessionNew']", 'unique': 'True', 'primary_key': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'pomsapp.possessionnew': {
            'Meta': {'object_name': 'PossessionNew'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_possessionnew'", 'null': 'True', 'to': "orm['auth.User']"}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'extraid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'helper_name': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'nameextension': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Place']", 'null': 'True', 'blank': 'True'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_possessionnew'", 'null': 'True', 'to': "orm['auth.User']"}),
            'util_topancestor': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'})
        },
        'pomsapp.privileges': {
            'Meta': {'ordering': "['tree_id', 'lft', 'name']", 'object_name': 'Privileges'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_privileges'", 'null': 'True', 'to': "orm['auth.User']"}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'extraid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'helper_name': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'nameextension': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['pomsapp.Privileges']"}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Place']", 'null': 'True', 'blank': 'True'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_privileges'", 'null': 'True', 'to': "orm['auth.User']"}),
            'util_topancestor': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'})
        },
        'pomsapp.proanimagenerictypes': {
            'Meta': {'ordering': "['name']", 'object_name': 'Proanimagenerictypes'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_proanimagenerictypes'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'newline': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'orderno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_proanimagenerictypes'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.referencetype': {
            'Meta': {'ordering': "['name']", 'object_name': 'Referencetype'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_referencetype'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_referencetype'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.relationshipmetatype': {
            'Meta': {'ordering': "['name']", 'object_name': 'Relationshipmetatype'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_relationshipmetatype'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_relationshipmetatype'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.relationshiptype': {
            'Meta': {'ordering': "['name']", 'object_name': 'Relationshiptype'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_relationshiptype'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'metatype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Relationshipmetatype']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_relationshiptype'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.renderdate': {
            'Meta': {'ordering': "['name']", 'object_name': 'Renderdate'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_renderdate'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_renderdate'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.returns_military': {
            'Meta': {'ordering': "['name']", 'object_name': 'Returns_military'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_returns_military'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_returns_military'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.returns_renders': {
            'Meta': {'ordering': "['name']", 'object_name': 'Returns_renders'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_returns_renders'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_returns_renders'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.role': {
            'Meta': {'ordering': "['name']", 'object_name': 'Role'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_role'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'spiritualbenefit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_role'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.seal': {
            'Meta': {'object_name': 'Seal', '_ormbases': ['pomsapp.Source']},
            'archive': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'archiverefnumber': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'att_type_surv': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'surv_attach_of'", 'null': 'True', 'to': "orm['pomsapp.AttachmentType']"}),
            'charter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Charter']", 'null': 'True', 'blank': 'True'}),
            'color': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.SealColor']", 'null': 'True', 'blank': 'True'}),
            'conditionnote': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'countersealed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'matrix': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Matrix']"}),
            'scranlink': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'source_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['pomsapp.Source']", 'unique': 'True', 'primary_key': 'True'})
        },
        'pomsapp.sealcolor': {
            'Meta': {'ordering': "['name']", 'object_name': 'SealColor'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_sealcolor'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_sealcolor'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.sicutclausetype': {
            'Meta': {'ordering': "['name']", 'object_name': 'Sicutclausetype'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_sicutclausetype'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'newline': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'orderno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_sicutclausetype'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.source': {
            'Meta': {'object_name': 'Source'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_source'", 'null': 'True', 'to': "orm['auth.User']"}),
            'datingnotes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'eitheror': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'firmdate': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'from_day': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'from_modifier': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'from_modifier2': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'from_month': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'from_season': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'from_weekday': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'from_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'grantor_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.GrantorCategory']", 'null': 'True', 'blank': 'True'}),
            'hammondext': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'hammondnumb2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hammondnumb3': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hammondnumber': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'has_firmdate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_firmdayonly': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'helper_daterange': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'helper_hammond': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'helper_keywordsearch': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'helper_totfactoids': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['pomsapp.Language']", 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'probabledate': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'source_tradid': ('django.db.models.fields.CharField', [], {'max_length': '765', 'null': 'True', 'blank': 'True'}),
            'sourcefordataentry': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'to_day': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'to_modifier': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'to_modifier2': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'to_month': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'to_season': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'to_weekday': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'to_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'undated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_source'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.tenendasclauseoptions': {
            'Meta': {'ordering': "['name']", 'object_name': 'Tenendasclauseoptions'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_tenendasclauseoptions'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_tenendasclauseoptions'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.titletype': {
            'Meta': {'ordering': "['name']", 'object_name': 'TitleType'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_titletype'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'placefk': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pomsapp.Place']", 'null': 'True', 'blank': 'True'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_titletype'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.transactiontype': {
            'Meta': {'ordering': "['name']", 'object_name': 'Transactiontype'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_transactiontype'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_transactiontype'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'pomsapp.transtickboxes': {
            'Meta': {'ordering': "['name']", 'object_name': 'TransTickboxes'},
            'created_at': ('utils.modelextra.myfields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_transtickboxes'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'editedrecord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('utils.modelextra.myfields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'updated_transtickboxes'", 'null': 'True', 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['pomsapp']