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
    id = models.TextField(db_column='ID', blank=True, primary_key=True)  # Field name made lowercase.
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


class Fish(models.Model):
    id = models.TextField(db_column='ID', blank=True, primary_key=True)  # Field name made lowercase.
    gene = models.TextField(blank=True, null=True)
    chr = models.TextField(blank=True, null=True)
    strand = models.TextField(blank=True, null=True)
    genome_coord = models.TextField(blank=True, null=True)
    aa_target = models.TextField(blank=True, null=True)
    codon = models.TextField(blank=True, null=True)
    n_tx_in_gene = models.TextField(blank=True, null=True)
    percent_tx = models.TextField(blank=True, null=True)
    percent_nmd = models.TextField(db_column='percent_NMD', blank=True, null=True)  # Field name made lowercase.
    rel_pos_largest_isoform = models.TextField(blank=True, null=True)
    no_upstream_g = models.TextField(db_column='no_upstream_G', blank=True, null=True)  # Field name made lowercase.
    rflp_loss = models.TextField(db_column='RFLP_Loss', blank=True, null=True)  # Field name made lowercase.
    rflp_gain = models.TextField(db_column='RFLP_Gain', blank=True, null=True)  # Field name made lowercase.
    sgngg = models.TextField(db_column='sgNGG', blank=True, null=True)  # Field name made lowercase.
    sgngg_spacing = models.TextField(db_column='sgNGG_spacing', blank=True, null=True)  # Field name made lowercase.
    sgngg_matches = models.TextField(db_column='sgNGG_matches', blank=True, null=True)  # Field name made lowercase.
    sgnga = models.TextField(db_column='sgNGA', blank=True, null=True)  # Field name made lowercase.
    sgnga_spacing = models.TextField(db_column='sgNGA_spacing', blank=True, null=True)  # Field name made lowercase.
    sgnga_matches = models.TextField(db_column='sgNGA_matches', blank=True, null=True)  # Field name made lowercase.
    sgngcg = models.TextField(db_column='sgNGCG', blank=True, null=True)  # Field name made lowercase.
    sgngcg_spacing = models.TextField(db_column='sgNGCG_spacing', blank=True, null=True)  # Field name made lowercase.
    sgngcg_matches = models.TextField(db_column='sgNGCG_matches', blank=True, null=True)  # Field name made lowercase.
    sgngag = models.TextField(db_column='sgNGAG', blank=True, null=True)  # Field name made lowercase.
    sgngag_spacing = models.TextField(db_column='sgNGAG_spacing', blank=True, null=True)  # Field name made lowercase.
    sgngag_matches = models.TextField(db_column='sgNGAG_matches', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt = models.TextField(db_column='sgNNGRRT', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt_spacing = models.TextField(db_column='sgNNGRRT_spacing', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt_matches = models.TextField(db_column='sgNNGRRT_matches', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt = models.TextField(db_column='sgNNNRRT', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt_spacing = models.TextField(db_column='sgNNNRRT_spacing', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt_matches = models.TextField(db_column='sgNNNRRT_matches', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fish'


class Fly(models.Model):
    id = models.TextField(db_column='ID', blank=True, primary_key=True)  # Field name made lowercase.
    gene = models.TextField(blank=True, null=True)
    chr = models.TextField(blank=True, null=True)
    strand = models.TextField(blank=True, null=True)
    genome_coord = models.TextField(blank=True, null=True)
    aa_target = models.TextField(blank=True, null=True)
    codon = models.TextField(blank=True, null=True)
    n_tx_in_gene = models.TextField(blank=True, null=True)
    percent_tx = models.TextField(blank=True, null=True)
    percent_nmd = models.TextField(db_column='percent_NMD', blank=True, null=True)  # Field name made lowercase.
    rel_pos_largest_isoform = models.TextField(blank=True, null=True)
    no_upstream_g = models.TextField(db_column='no_upstream_G', blank=True, null=True)  # Field name made lowercase.
    rflp_loss = models.TextField(db_column='RFLP_Loss', blank=True, null=True)  # Field name made lowercase.
    rflp_gain = models.TextField(db_column='RFLP_Gain', blank=True, null=True)  # Field name made lowercase.
    sgngg = models.TextField(db_column='sgNGG', blank=True, null=True)  # Field name made lowercase.
    sgngg_spacing = models.TextField(db_column='sgNGG_spacing', blank=True, null=True)  # Field name made lowercase.
    sgngg_matches = models.TextField(db_column='sgNGG_matches', blank=True, null=True)  # Field name made lowercase.
    sgnga = models.TextField(db_column='sgNGA', blank=True, null=True)  # Field name made lowercase.
    sgnga_spacing = models.TextField(db_column='sgNGA_spacing', blank=True, null=True)  # Field name made lowercase.
    sgnga_matches = models.TextField(db_column='sgNGA_matches', blank=True, null=True)  # Field name made lowercase.
    sgngcg = models.TextField(db_column='sgNGCG', blank=True, null=True)  # Field name made lowercase.
    sgngcg_spacing = models.TextField(db_column='sgNGCG_spacing', blank=True, null=True)  # Field name made lowercase.
    sgngcg_matches = models.TextField(db_column='sgNGCG_matches', blank=True, null=True)  # Field name made lowercase.
    sgngag = models.TextField(db_column='sgNGAG', blank=True, null=True)  # Field name made lowercase.
    sgngag_spacing = models.TextField(db_column='sgNGAG_spacing', blank=True, null=True)  # Field name made lowercase.
    sgngag_matches = models.TextField(db_column='sgNGAG_matches', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt = models.TextField(db_column='sgNNGRRT', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt_spacing = models.TextField(db_column='sgNNGRRT_spacing', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt_matches = models.TextField(db_column='sgNNGRRT_matches', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt = models.TextField(db_column='sgNNNRRT', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt_spacing = models.TextField(db_column='sgNNNRRT_spacing', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt_matches = models.TextField(db_column='sgNNNRRT_matches', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fly'


class Humans(models.Model):
    id = models.TextField(db_column='ID', blank=True, primary_key=True)  # Field name made lowercase.
    gene = models.TextField(blank=True, null=True)
    chr = models.TextField(blank=True, null=True)
    strand = models.TextField(blank=True, null=True)
    genome_coord = models.TextField(blank=True, null=True)
    aa_target = models.TextField(blank=True, null=True)
    codon = models.TextField(blank=True, null=True)
    n_tx_in_gene = models.TextField(blank=True, null=True)
    percent_tx = models.TextField(blank=True, null=True)
    percent_nmd = models.TextField(db_column='percent_NMD', blank=True, null=True)  # Field name made lowercase.
    rel_pos_largest_isoform = models.TextField(blank=True, null=True)
    no_upstream_g = models.TextField(db_column='no_upstream_G', blank=True, null=True)  # Field name made lowercase.
    rflp_loss = models.TextField(db_column='RFLP_Loss', blank=True, null=True)  # Field name made lowercase.
    rflp_gain = models.TextField(db_column='RFLP_Gain', blank=True, null=True)  # Field name made lowercase.
    cancer_type = models.TextField(blank=True, null=True)
    sgngg = models.TextField(db_column='sgNGG', blank=True, null=True)  # Field name made lowercase.
    sgngg_spacing = models.TextField(db_column='sgNGG_spacing', blank=True, null=True)  # Field name made lowercase.
    sgngg_matches = models.TextField(db_column='sgNGG_matches', blank=True, null=True)  # Field name made lowercase.
    sgnga = models.TextField(db_column='sgNGA', blank=True, null=True)  # Field name made lowercase.
    sgnga_spacing = models.TextField(db_column='sgNGA_spacing', blank=True, null=True)  # Field name made lowercase.
    sgnga_matches = models.TextField(db_column='sgNGA_matches', blank=True, null=True)  # Field name made lowercase.
    sgngcg = models.TextField(db_column='sgNGCG', blank=True, null=True)  # Field name made lowercase.
    sgngcg_spacing = models.TextField(db_column='sgNGCG_spacing', blank=True, null=True)  # Field name made lowercase.
    sgngcg_matches = models.TextField(db_column='sgNGCG_matches', blank=True, null=True)  # Field name made lowercase.
    sgngag = models.TextField(db_column='sgNGAG', blank=True, null=True)  # Field name made lowercase.
    sgngag_spacing = models.TextField(db_column='sgNGAG_spacing', blank=True, null=True)  # Field name made lowercase.
    sgngag_matches = models.TextField(db_column='sgNGAG_matches', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt = models.TextField(db_column='sgNNGRRT', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt_spacing = models.TextField(db_column='sgNNGRRT_spacing', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt_matches = models.TextField(db_column='sgNNGRRT_matches', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt = models.TextField(db_column='sgNNNRRT', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt_spacing = models.TextField(db_column='sgNNNRRT_spacing', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt_matches = models.TextField(db_column='sgNNNRRT_matches', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'humans'


class Mouse(models.Model):
    id = models.TextField(db_column='ID', blank=True, primary_key=True)  # Field name made lowercase.
    gene = models.TextField(blank=True, null=True)
    chr = models.TextField(blank=True, null=True)
    strand = models.TextField(blank=True, null=True)
    genome_coord = models.TextField(blank=True, null=True)
    aa_target = models.TextField(blank=True, null=True)
    codon = models.TextField(blank=True, null=True)
    n_tx_in_gene = models.TextField(blank=True, null=True)
    percent_tx = models.TextField(blank=True, null=True)
    percent_nmd = models.TextField(db_column='percent_NMD', blank=True, null=True)  # Field name made lowercase.
    rel_pos_largest_isoform = models.TextField(blank=True, null=True)
    no_upstream_g = models.TextField(db_column='no_upstream_G', blank=True, null=True)  # Field name made lowercase.
    rflp_loss = models.TextField(db_column='RFLP_Loss', blank=True, null=True)  # Field name made lowercase.
    rflp_gain = models.TextField(db_column='RFLP_Gain', blank=True, null=True)  # Field name made lowercase.
    sgngg = models.TextField(db_column='sgNGG', blank=True, null=True)  # Field name made lowercase.
    sgngg_spacing = models.TextField(db_column='sgNGG_spacing', blank=True, null=True)  # Field name made lowercase.
    sgngg_matches = models.TextField(db_column='sgNGG_matches', blank=True, null=True)  # Field name made lowercase.
    sgnga = models.TextField(db_column='sgNGA', blank=True, null=True)  # Field name made lowercase.
    sgnga_spacing = models.TextField(db_column='sgNGA_spacing', blank=True, null=True)  # Field name made lowercase.
    sgnga_matches = models.TextField(db_column='sgNGA_matches', blank=True, null=True)  # Field name made lowercase.
    sgngcg = models.TextField(db_column='sgNGCG', blank=True, null=True)  # Field name made lowercase.
    sgngcg_spacing = models.TextField(db_column='sgNGCG_spacing', blank=True, null=True)  # Field name made lowercase.
    sgngcg_matches = models.TextField(db_column='sgNGCG_matches', blank=True, null=True)  # Field name made lowercase.
    sgngag = models.TextField(db_column='sgNGAG', blank=True, null=True)  # Field name made lowercase.
    sgngag_spacing = models.TextField(db_column='sgNGAG_spacing', blank=True, null=True)  # Field name made lowercase.
    sgngag_matches = models.TextField(db_column='sgNGAG_matches', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt = models.TextField(db_column='sgNNGRRT', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt_spacing = models.TextField(db_column='sgNNGRRT_spacing', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt_matches = models.TextField(db_column='sgNNGRRT_matches', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt = models.TextField(db_column='sgNNNRRT', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt_spacing = models.TextField(db_column='sgNNNRRT_spacing', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt_matches = models.TextField(db_column='sgNNNRRT_matches', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mouse'


class Nematode(models.Model):
    id = models.TextField(db_column='ID', blank=True, primary_key=True)  # Field name made lowercase.
    gene = models.TextField(blank=True, null=True)
    chr = models.TextField(blank=True, null=True)
    strand = models.TextField(blank=True, null=True)
    genome_coord = models.TextField(blank=True, null=True)
    aa_target = models.TextField(blank=True, null=True)
    codon = models.TextField(blank=True, null=True)
    n_tx_in_gene = models.TextField(blank=True, null=True)
    percent_tx = models.TextField(blank=True, null=True)
    percent_nmd = models.TextField(db_column='percent_NMD', blank=True, null=True)  # Field name made lowercase.
    rel_pos_largest_isoform = models.TextField(blank=True, null=True)
    no_upstream_g = models.TextField(db_column='no_upstream_G', blank=True, null=True)  # Field name made lowercase.
    rflp_loss = models.TextField(db_column='RFLP_Loss', blank=True, null=True)  # Field name made lowercase.
    rflp_gain = models.TextField(db_column='RFLP_Gain', blank=True, null=True)  # Field name made lowercase.
    sgngg = models.TextField(db_column='sgNGG', blank=True, null=True)  # Field name made lowercase.
    sgngg_spacing = models.TextField(db_column='sgNGG_spacing', blank=True, null=True)  # Field name made lowercase.
    sgngg_matches = models.TextField(db_column='sgNGG_matches', blank=True, null=True)  # Field name made lowercase.
    sgnga = models.TextField(db_column='sgNGA', blank=True, null=True)  # Field name made lowercase.
    sgnga_spacing = models.TextField(db_column='sgNGA_spacing', blank=True, null=True)  # Field name made lowercase.
    sgnga_matches = models.TextField(db_column='sgNGA_matches', blank=True, null=True)  # Field name made lowercase.
    sgngcg = models.TextField(db_column='sgNGCG', blank=True, null=True)  # Field name made lowercase.
    sgngcg_spacing = models.TextField(db_column='sgNGCG_spacing', blank=True, null=True)  # Field name made lowercase.
    sgngcg_matches = models.TextField(db_column='sgNGCG_matches', blank=True, null=True)  # Field name made lowercase.
    sgngag = models.TextField(db_column='sgNGAG', blank=True, null=True)  # Field name made lowercase.
    sgngag_spacing = models.TextField(db_column='sgNGAG_spacing', blank=True, null=True)  # Field name made lowercase.
    sgngag_matches = models.TextField(db_column='sgNGAG_matches', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt = models.TextField(db_column='sgNNGRRT', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt_spacing = models.TextField(db_column='sgNNGRRT_spacing', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt_matches = models.TextField(db_column='sgNNGRRT_matches', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt = models.TextField(db_column='sgNNNRRT', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt_spacing = models.TextField(db_column='sgNNNRRT_spacing', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt_matches = models.TextField(db_column='sgNNNRRT_matches', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nematode'


class Plant(models.Model):
    id = models.TextField(db_column='ID', blank=True, primary_key=True)  # Field name made lowercase.
    gene = models.TextField(blank=True, null=True)
    chr = models.TextField(blank=True, null=True)
    strand = models.TextField(blank=True, null=True)
    genome_coord = models.TextField(blank=True, null=True)
    aa_target = models.TextField(blank=True, null=True)
    codon = models.TextField(blank=True, null=True)
    n_tx_in_gene = models.TextField(blank=True, null=True)
    percent_tx = models.TextField(blank=True, null=True)
    percent_nmd = models.TextField(db_column='percent_NMD', blank=True, null=True)  # Field name made lowercase.
    rel_pos_largest_isoform = models.TextField(blank=True, null=True)
    no_upstream_g = models.TextField(db_column='no_upstream_G', blank=True, null=True)  # Field name made lowercase.
    rflp_loss = models.TextField(db_column='RFLP_Loss', blank=True, null=True)  # Field name made lowercase.
    rflp_gain = models.TextField(db_column='RFLP_Gain', blank=True, null=True)  # Field name made lowercase.
    sgngg = models.TextField(db_column='sgNGG', blank=True, null=True)  # Field name made lowercase.
    sgngg_spacing = models.TextField(db_column='sgNGG_spacing', blank=True, null=True)  # Field name made lowercase.
    sgngg_matches = models.TextField(db_column='sgNGG_matches', blank=True, null=True)  # Field name made lowercase.
    sgnga = models.TextField(db_column='sgNGA', blank=True, null=True)  # Field name made lowercase.
    sgnga_spacing = models.TextField(db_column='sgNGA_spacing', blank=True, null=True)  # Field name made lowercase.
    sgnga_matches = models.TextField(db_column='sgNGA_matches', blank=True, null=True)  # Field name made lowercase.
    sgngcg = models.TextField(db_column='sgNGCG', blank=True, null=True)  # Field name made lowercase.
    sgngcg_spacing = models.TextField(db_column='sgNGCG_spacing', blank=True, null=True)  # Field name made lowercase.
    sgngcg_matches = models.TextField(db_column='sgNGCG_matches', blank=True, null=True)  # Field name made lowercase.
    sgngag = models.TextField(db_column='sgNGAG', blank=True, null=True)  # Field name made lowercase.
    sgngag_spacing = models.TextField(db_column='sgNGAG_spacing', blank=True, null=True)  # Field name made lowercase.
    sgngag_matches = models.TextField(db_column='sgNGAG_matches', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt = models.TextField(db_column='sgNNGRRT', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt_spacing = models.TextField(db_column='sgNNGRRT_spacing', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt_matches = models.TextField(db_column='sgNNGRRT_matches', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt = models.TextField(db_column='sgNNNRRT', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt_spacing = models.TextField(db_column='sgNNNRRT_spacing', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt_matches = models.TextField(db_column='sgNNNRRT_matches', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'plant'


class Rat(models.Model):
    id = models.TextField(db_column='ID', blank=True, primary_key=True)  # Field name made lowercase.
    gene = models.TextField(blank=True, null=True)
    chr = models.TextField(blank=True, null=True)
    strand = models.TextField(blank=True, null=True)
    genome_coord = models.TextField(blank=True, null=True)
    aa_target = models.TextField(blank=True, null=True)
    codon = models.TextField(blank=True, null=True)
    n_tx_in_gene = models.TextField(blank=True, null=True)
    percent_tx = models.TextField(blank=True, null=True)
    percent_nmd = models.TextField(db_column='percent_NMD', blank=True, null=True)  # Field name made lowercase.
    rel_pos_largest_isoform = models.TextField(blank=True, null=True)
    no_upstream_g = models.TextField(db_column='no_upstream_G', blank=True, null=True)  # Field name made lowercase.
    rflp_loss = models.TextField(db_column='RFLP_Loss', blank=True, null=True)  # Field name made lowercase.
    rflp_gain = models.TextField(db_column='RFLP_Gain', blank=True, null=True)  # Field name made lowercase.
    sgngg = models.TextField(db_column='sgNGG', blank=True, null=True)  # Field name made lowercase.
    sgngg_spacing = models.TextField(db_column='sgNGG_spacing', blank=True, null=True)  # Field name made lowercase.
    sgngg_matches = models.TextField(db_column='sgNGG_matches', blank=True, null=True)  # Field name made lowercase.
    sgnga = models.TextField(db_column='sgNGA', blank=True, null=True)  # Field name made lowercase.
    sgnga_spacing = models.TextField(db_column='sgNGA_spacing', blank=True, null=True)  # Field name made lowercase.
    sgnga_matches = models.TextField(db_column='sgNGA_matches', blank=True, null=True)  # Field name made lowercase.
    sgngcg = models.TextField(db_column='sgNGCG', blank=True, null=True)  # Field name made lowercase.
    sgngcg_spacing = models.TextField(db_column='sgNGCG_spacing', blank=True, null=True)  # Field name made lowercase.
    sgngcg_matches = models.TextField(db_column='sgNGCG_matches', blank=True, null=True)  # Field name made lowercase.
    sgngag = models.TextField(db_column='sgNGAG', blank=True, null=True)  # Field name made lowercase.
    sgngag_spacing = models.TextField(db_column='sgNGAG_spacing', blank=True, null=True)  # Field name made lowercase.
    sgngag_matches = models.TextField(db_column='sgNGAG_matches', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt = models.TextField(db_column='sgNNGRRT', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt_spacing = models.TextField(db_column='sgNNGRRT_spacing', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt_matches = models.TextField(db_column='sgNNGRRT_matches', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt = models.TextField(db_column='sgNNNRRT', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt_spacing = models.TextField(db_column='sgNNNRRT_spacing', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt_matches = models.TextField(db_column='sgNNNRRT_matches', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rat'


class Yeast(models.Model):
    id = models.TextField(db_column='ID', blank=True, primary_key=True)  # Field name made lowercase.
    gene = models.TextField(blank=True, null=True)
    chr = models.TextField(blank=True, null=True)
    strand = models.TextField(blank=True, null=True)
    genome_coord = models.TextField(blank=True, null=True)
    aa_target = models.TextField(blank=True, null=True)
    codon = models.TextField(blank=True, null=True)
    n_tx_in_gene = models.TextField(blank=True, null=True)
    percent_tx = models.TextField(blank=True, null=True)
    percent_nmd = models.TextField(db_column='percent_NMD', blank=True, null=True)  # Field name made lowercase.
    rel_pos_largest_isoform = models.TextField(blank=True, null=True)
    no_upstream_g = models.TextField(db_column='no_upstream_G', blank=True, null=True)  # Field name made lowercase.
    rflp_loss = models.TextField(db_column='RFLP_Loss', blank=True, null=True)  # Field name made lowercase.
    rflp_gain = models.TextField(db_column='RFLP_Gain', blank=True, null=True)  # Field name made lowercase.
    sgngg = models.TextField(db_column='sgNGG', blank=True, null=True)  # Field name made lowercase.
    sgngg_spacing = models.TextField(db_column='sgNGG_spacing', blank=True, null=True)  # Field name made lowercase.
    sgngg_matches = models.TextField(db_column='sgNGG_matches', blank=True, null=True)  # Field name made lowercase.
    sgnga = models.TextField(db_column='sgNGA', blank=True, null=True)  # Field name made lowercase.
    sgnga_spacing = models.TextField(db_column='sgNGA_spacing', blank=True, null=True)  # Field name made lowercase.
    sgnga_matches = models.TextField(db_column='sgNGA_matches', blank=True, null=True)  # Field name made lowercase.
    sgngcg = models.TextField(db_column='sgNGCG', blank=True, null=True)  # Field name made lowercase.
    sgngcg_spacing = models.TextField(db_column='sgNGCG_spacing', blank=True, null=True)  # Field name made lowercase.
    sgngcg_matches = models.TextField(db_column='sgNGCG_matches', blank=True, null=True)  # Field name made lowercase.
    sgngag = models.TextField(db_column='sgNGAG', blank=True, null=True)  # Field name made lowercase.
    sgngag_spacing = models.TextField(db_column='sgNGAG_spacing', blank=True, null=True)  # Field name made lowercase.
    sgngag_matches = models.TextField(db_column='sgNGAG_matches', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt = models.TextField(db_column='sgNNGRRT', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt_spacing = models.TextField(db_column='sgNNGRRT_spacing', blank=True, null=True)  # Field name made lowercase.
    sgnngrrt_matches = models.TextField(db_column='sgNNGRRT_matches', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt = models.TextField(db_column='sgNNNRRT', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt_spacing = models.TextField(db_column='sgNNNRRT_spacing', blank=True, null=True)  # Field name made lowercase.
    sgnnnrrt_matches = models.TextField(db_column='sgNNNRRT_matches', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'yeast'
