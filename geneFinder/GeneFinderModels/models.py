# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Fly(models.Model):
    id = models.TextField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
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
    id = models.TextField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
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
    id = models.TextField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
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
        db_table = 'humans'


class Mouse(models.Model):
    id = models.TextField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
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
    id = models.TextField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
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
    id = models.TextField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
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
    id = models.TextField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
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
    id = models.TextField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
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
