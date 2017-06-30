# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Cosmic(models.Model):
    id = models.TextField(db_column='ID', blank=True, null=True, primary_key=True)  # Field name made lowercase.
    gene = models.TextField(blank=True, null=True)
    cancer_type = models.TextField(blank=True, null=True)
    mutation_aa = models.TextField(blank=True, null=True)
    chr = models.TextField(blank=True, null=True)
    strand = models.TextField(blank=True, null=True)
    coord = models.TextField(blank=True, null=True)
    pam = models.TextField(db_column='PAM', blank=True, null=True)  # Field name made lowercase.
    istop = models.TextField(db_column='iSTOP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cosmic'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Fly(models.Model):
    id = models.TextField(db_column='ID', blank=True, null=True, primary_key=True)  # Field name made lowercase.
    txs = models.TextField(blank=True, null=True)
    gene = models.TextField(blank=True, null=True)
    chr = models.TextField(blank=True, null=True)
    strand = models.TextField(blank=True, null=True)
    sg_strand = models.TextField(blank=True, null=True)
    aa_target = models.TextField(blank=True, null=True)
    codon = models.TextField(blank=True, null=True)
    genome_coord = models.TextField(blank=True, null=True)
    n_tx_in_gene = models.TextField(blank=True, null=True)
    n_tx = models.TextField(blank=True, null=True)
    percent_tx = models.TextField(blank=True, null=True)
    searched = models.TextField(blank=True, null=True)
    sgngg = models.TextField(db_column='sgNGG', blank=True, null=True)  # Field name made lowercase.
    sgnga = models.TextField(db_column='sgNGA', blank=True, null=True)  # Field name made lowercase.
    sgngcg = models.TextField(db_column='sgNGCG', blank=True, null=True)  # Field name made lowercase.
    sgngag = models.TextField(db_column='sgNGAG', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt = models.TextField(db_column='sgNNGRRT', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt = models.TextField(db_column='sgNNNRRT', blank=True, null=True)  # Field name made lowercase.
    exons = models.TextField(blank=True, null=True)
    pep_lengths = models.TextField(blank=True, null=True)
    cds_lengths = models.TextField(blank=True, null=True)
    aa_coords = models.TextField(blank=True, null=True)
    cds_coords = models.TextField(blank=True, null=True)
    nmd_pred = models.TextField(db_column='NMD_pred', blank=True, null=True)  # Field name made lowercase.
    rflp_150 = models.TextField(db_column='RFLP_150', blank=True, null=True)  # Field name made lowercase.
    rflp_100 = models.TextField(db_column='RFLP_100', blank=True, null=True)  # Field name made lowercase.
    rflp_50 = models.TextField(db_column='RFLP_50', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fly'


class Frog(models.Model):
    id = models.TextField(db_column='ID', blank=True, null=True, primary_key=True)  # Field name made lowercase.
    txs = models.TextField(blank=True, null=True)
    gene = models.TextField(blank=True, null=True)
    chr = models.TextField(blank=True, null=True)
    strand = models.TextField(blank=True, null=True)
    sg_strand = models.TextField(blank=True, null=True)
    aa_target = models.TextField(blank=True, null=True)
    codon = models.TextField(blank=True, null=True)
    genome_coord = models.TextField(blank=True, null=True)
    n_tx_in_gene = models.TextField(blank=True, null=True)
    n_tx = models.TextField(blank=True, null=True)
    percent_tx = models.TextField(blank=True, null=True)
    searched = models.TextField(blank=True, null=True)
    sgngg = models.TextField(db_column='sgNGG', blank=True, null=True)  # Field name made lowercase.
    sgnga = models.TextField(db_column='sgNGA', blank=True, null=True)  # Field name made lowercase.
    sgngcg = models.TextField(db_column='sgNGCG', blank=True, null=True)  # Field name made lowercase.
    sgngag = models.TextField(db_column='sgNGAG', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt = models.TextField(db_column='sgNNGRRT', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt = models.TextField(db_column='sgNNNRRT', blank=True, null=True)  # Field name made lowercase.
    exons = models.TextField(blank=True, null=True)
    pep_lengths = models.TextField(blank=True, null=True)
    cds_lengths = models.TextField(blank=True, null=True)
    aa_coords = models.TextField(blank=True, null=True)
    cds_coords = models.TextField(blank=True, null=True)
    nmd_pred = models.TextField(db_column='NMD_pred', blank=True, null=True)  # Field name made lowercase.
    rflp_150 = models.TextField(db_column='RFLP_150', blank=True, null=True)  # Field name made lowercase.
    rflp_100 = models.TextField(db_column='RFLP_100', blank=True, null=True)  # Field name made lowercase.
    rflp_50 = models.TextField(db_column='RFLP_50', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'frog'


class Humans(models.Model):
    id = models.TextField(db_column='ID', blank=True, null=True, primary_key=True)  # Field name made lowercase.
    txs = models.TextField(blank=True, null=True)
    gene = models.TextField(blank=True, null=True)
    chr = models.TextField(blank=True, null=True)
    strand = models.TextField(blank=True, null=True)
    sg_strand = models.TextField(blank=True, null=True)
    aa_target = models.TextField(blank=True, null=True)
    codon = models.TextField(blank=True, null=True)
    genome_coord = models.TextField(blank=True, null=True)
    n_tx_in_gene = models.TextField(blank=True, null=True)
    n_tx = models.TextField(blank=True, null=True)
    percent_tx = models.TextField(blank=True, null=True)
    searched = models.TextField(blank=True, null=True)
    sgngg = models.TextField(db_column='sgNGG', blank=True, null=True)  # Field name made lowercase.
    sgnga = models.TextField(db_column='sgNGA', blank=True, null=True)  # Field name made lowercase.
    sgngcg = models.TextField(db_column='sgNGCG', blank=True, null=True)  # Field name made lowercase.
    sgngag = models.TextField(db_column='sgNGAG', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt = models.TextField(db_column='sgNNGRRT', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt = models.TextField(db_column='sgNNNRRT', blank=True, null=True)  # Field name made lowercase.
    exons = models.TextField(blank=True, null=True)
    pep_lengths = models.TextField(blank=True, null=True)
    cds_lengths = models.TextField(blank=True, null=True)
    aa_coords = models.TextField(blank=True, null=True)
    cds_coords = models.TextField(blank=True, null=True)
    nmd_pred = models.TextField(db_column='NMD_pred', blank=True, null=True)  # Field name made lowercase.
    rflp_150 = models.TextField(db_column='RFLP_150', blank=True, null=True)  # Field name made lowercase.
    rflp_100 = models.TextField(db_column='RFLP_100', blank=True, null=True)  # Field name made lowercase.
    rflp_50 = models.TextField(db_column='RFLP_50', blank=True, null=True)  # Field name made lowercase.
    cancer_type = models.TextField(blank=True, null=True)
    cosmic_nonsense = models.TextField(db_column='COSMIC_nonsense', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'humans'


class Mouse(models.Model):
    id = models.TextField(db_column='ID', blank=True, null=True, primary_key=True)  # Field name made lowercase.
    txs = models.TextField(blank=True, null=True)
    gene = models.TextField(blank=True, null=True)
    chr = models.TextField(blank=True, null=True)
    strand = models.TextField(blank=True, null=True)
    sg_strand = models.TextField(blank=True, null=True)
    aa_target = models.TextField(blank=True, null=True)
    codon = models.TextField(blank=True, null=True)
    genome_coord = models.TextField(blank=True, null=True)
    n_tx_in_gene = models.TextField(blank=True, null=True)
    n_tx = models.TextField(blank=True, null=True)
    percent_tx = models.TextField(blank=True, null=True)
    searched = models.TextField(blank=True, null=True)
    sgngg = models.TextField(db_column='sgNGG', blank=True, null=True)  # Field name made lowercase.
    sgnga = models.TextField(db_column='sgNGA', blank=True, null=True)  # Field name made lowercase.
    sgngcg = models.TextField(db_column='sgNGCG', blank=True, null=True)  # Field name made lowercase.
    sgngag = models.TextField(db_column='sgNGAG', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt = models.TextField(db_column='sgNNGRRT', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt = models.TextField(db_column='sgNNNRRT', blank=True, null=True)  # Field name made lowercase.
    exons = models.TextField(blank=True, null=True)
    pep_lengths = models.TextField(blank=True, null=True)
    cds_lengths = models.TextField(blank=True, null=True)
    aa_coords = models.TextField(blank=True, null=True)
    cds_coords = models.TextField(blank=True, null=True)
    nmd_pred = models.TextField(db_column='NMD_pred', blank=True, null=True)  # Field name made lowercase.
    rflp_150 = models.TextField(db_column='RFLP_150', blank=True, null=True)  # Field name made lowercase.
    rflp_100 = models.TextField(db_column='RFLP_100', blank=True, null=True)  # Field name made lowercase.
    rflp_50 = models.TextField(db_column='RFLP_50', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mouse'


class Nematode(models.Model):
    id = models.TextField(db_column='ID', blank=True, null=True, primary_key=True)  # Field name made lowercase.
    txs = models.TextField(blank=True, null=True)
    gene = models.TextField(blank=True, null=True)
    chr = models.TextField(blank=True, null=True)
    strand = models.TextField(blank=True, null=True)
    sg_strand = models.TextField(blank=True, null=True)
    aa_target = models.TextField(blank=True, null=True)
    codon = models.TextField(blank=True, null=True)
    genome_coord = models.TextField(blank=True, null=True)
    n_tx_in_gene = models.TextField(blank=True, null=True)
    n_tx = models.TextField(blank=True, null=True)
    percent_tx = models.TextField(blank=True, null=True)
    searched = models.TextField(blank=True, null=True)
    sgngg = models.TextField(db_column='sgNGG', blank=True, null=True)  # Field name made lowercase.
    sgnga = models.TextField(db_column='sgNGA', blank=True, null=True)  # Field name made lowercase.
    sgngcg = models.TextField(db_column='sgNGCG', blank=True, null=True)  # Field name made lowercase.
    sgngag = models.TextField(db_column='sgNGAG', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt = models.TextField(db_column='sgNNGRRT', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt = models.TextField(db_column='sgNNNRRT', blank=True, null=True)  # Field name made lowercase.
    exons = models.TextField(blank=True, null=True)
    pep_lengths = models.TextField(blank=True, null=True)
    cds_lengths = models.TextField(blank=True, null=True)
    aa_coords = models.TextField(blank=True, null=True)
    cds_coords = models.TextField(blank=True, null=True)
    nmd_pred = models.TextField(db_column='NMD_pred', blank=True, null=True)  # Field name made lowercase.
    rflp_150 = models.TextField(db_column='RFLP_150', blank=True, null=True)  # Field name made lowercase.
    rflp_100 = models.TextField(db_column='RFLP_100', blank=True, null=True)  # Field name made lowercase.
    rflp_50 = models.TextField(db_column='RFLP_50', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nematode'


class Plant(models.Model):
    id = models.TextField(db_column='ID', blank=True, null=True, primary_key=True)  # Field name made lowercase.
    txs = models.TextField(blank=True, null=True)
    gene = models.TextField(blank=True, null=True)
    chr = models.TextField(blank=True, null=True)
    strand = models.TextField(blank=True, null=True)
    sg_strand = models.TextField(blank=True, null=True)
    aa_target = models.TextField(blank=True, null=True)
    codon = models.TextField(blank=True, null=True)
    genome_coord = models.TextField(blank=True, null=True)
    n_tx_in_gene = models.TextField(blank=True, null=True)
    n_tx = models.TextField(blank=True, null=True)
    percent_tx = models.TextField(blank=True, null=True)
    searched = models.TextField(blank=True, null=True)
    sgngg = models.TextField(db_column='sgNGG', blank=True, null=True)  # Field name made lowercase.
    sgnga = models.TextField(db_column='sgNGA', blank=True, null=True)  # Field name made lowercase.
    sgngcg = models.TextField(db_column='sgNGCG', blank=True, null=True)  # Field name made lowercase.
    sgngag = models.TextField(db_column='sgNGAG', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt = models.TextField(db_column='sgNNGRRT', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt = models.TextField(db_column='sgNNNRRT', blank=True, null=True)  # Field name made lowercase.
    exons = models.TextField(blank=True, null=True)
    pep_lengths = models.TextField(blank=True, null=True)
    cds_lengths = models.TextField(blank=True, null=True)
    aa_coords = models.TextField(blank=True, null=True)
    cds_coords = models.TextField(blank=True, null=True)
    nmd_pred = models.TextField(db_column='NMD_pred', blank=True, null=True)  # Field name made lowercase.
    rflp_150 = models.TextField(db_column='RFLP_150', blank=True, null=True)  # Field name made lowercase.
    rflp_100 = models.TextField(db_column='RFLP_100', blank=True, null=True)  # Field name made lowercase.
    rflp_50 = models.TextField(db_column='RFLP_50', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'plant'


class Rat(models.Model):
    id = models.TextField(db_column='ID', blank=True, null=True, primary_key=True)  # Field name made lowercase.
    txs = models.TextField(blank=True, null=True)
    gene = models.TextField(blank=True, null=True)
    chr = models.TextField(blank=True, null=True)
    strand = models.TextField(blank=True, null=True)
    sg_strand = models.TextField(blank=True, null=True)
    aa_target = models.TextField(blank=True, null=True)
    codon = models.TextField(blank=True, null=True)
    genome_coord = models.TextField(blank=True, null=True)
    n_tx_in_gene = models.TextField(blank=True, null=True)
    n_tx = models.TextField(blank=True, null=True)
    percent_tx = models.TextField(blank=True, null=True)
    searched = models.TextField(blank=True, null=True)
    sgngg = models.TextField(db_column='sgNGG', blank=True, null=True)  # Field name made lowercase.
    sgnga = models.TextField(db_column='sgNGA', blank=True, null=True)  # Field name made lowercase.
    sgngcg = models.TextField(db_column='sgNGCG', blank=True, null=True)  # Field name made lowercase.
    sgngag = models.TextField(db_column='sgNGAG', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt = models.TextField(db_column='sgNNGRRT', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt = models.TextField(db_column='sgNNNRRT', blank=True, null=True)  # Field name made lowercase.
    exons = models.TextField(blank=True, null=True)
    pep_lengths = models.TextField(blank=True, null=True)
    cds_lengths = models.TextField(blank=True, null=True)
    aa_coords = models.TextField(blank=True, null=True)
    cds_coords = models.TextField(blank=True, null=True)
    nmd_pred = models.TextField(db_column='NMD_pred', blank=True, null=True)  # Field name made lowercase.
    rflp_150 = models.TextField(db_column='RFLP_150', blank=True, null=True)  # Field name made lowercase.
    rflp_100 = models.TextField(db_column='RFLP_100', blank=True, null=True)  # Field name made lowercase.
    rflp_50 = models.TextField(db_column='RFLP_50', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rat'


class Yeast(models.Model):
    id = models.TextField(db_column='ID', blank=True, null=True, primary_key=True)  # Field name made lowercase.
    txs = models.TextField(blank=True, null=True)
    gene = models.TextField(blank=True, null=True)
    chr = models.TextField(blank=True, null=True)
    strand = models.TextField(blank=True, null=True)
    sg_strand = models.TextField(blank=True, null=True)
    aa_target = models.TextField(blank=True, null=True)
    codon = models.TextField(blank=True, null=True)
    genome_coord = models.TextField(blank=True, null=True)
    n_tx_in_gene = models.TextField(blank=True, null=True)
    n_tx = models.TextField(blank=True, null=True)
    percent_tx = models.TextField(blank=True, null=True)
    searched = models.TextField(blank=True, null=True)
    sgngg = models.TextField(db_column='sgNGG', blank=True, null=True)  # Field name made lowercase.
    sgnga = models.TextField(db_column='sgNGA', blank=True, null=True)  # Field name made lowercase.
    sgngcg = models.TextField(db_column='sgNGCG', blank=True, null=True)  # Field name made lowercase.
    sgngag = models.TextField(db_column='sgNGAG', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt = models.TextField(db_column='sgNNGRRT', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt = models.TextField(db_column='sgNNNRRT', blank=True, null=True)  # Field name made lowercase.
    exons = models.TextField(blank=True, null=True)
    pep_lengths = models.TextField(blank=True, null=True)
    cds_lengths = models.TextField(blank=True, null=True)
    aa_coords = models.TextField(blank=True, null=True)
    cds_coords = models.TextField(blank=True, null=True)
    nmd_pred = models.TextField(db_column='NMD_pred', blank=True, null=True)  # Field name made lowercase.
    rflp_150 = models.TextField(db_column='RFLP_150', blank=True, null=True)  # Field name made lowercase.
    rflp_100 = models.TextField(db_column='RFLP_100', blank=True, null=True)  # Field name made lowercase.
    rflp_50 = models.TextField(db_column='RFLP_50', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'yeast'
