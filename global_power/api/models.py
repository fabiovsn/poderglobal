# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PoderGlobal(models.Model):
    nome_pais = models.CharField(blank=True, max_length=100, primary_key=True)
    codigo_pais = models.CharField(blank=True, null=True, max_length=5)
    qtd_pessoal_ativo = models.IntegerField(blank=True, null=True)
    qtd_porta_avioes = models.IntegerField(blank=True, null=True)
    qtd_veiculos_blindados = models.IntegerField(blank=True, null=True)
    qtd_helicopteros_de_ataque = models.IntegerField(blank=True, null=True)
    qtd_pessoal_disponivel = models.IntegerField(blank=True, null=True)
    qtd_corvetas = models.IntegerField(blank=True, null=True)
    orcamento_de_defesa = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    qtd_contratorpedeiro = models.IntegerField(blank=True, null=True)
    qtd_cacas_interceptadores = models.IntegerField(blank=True, null=True)
    qtd_disponivel_para_servico_militar = models.IntegerField(blank=True, null=True)
    qtd_fragatas = models.IntegerField(blank=True, null=True)
    qtd_porta_helicopteros = models.IntegerField(blank=True, null=True)
    qtd_helicopteros = models.IntegerField(blank=True, null=True)
    qtd_forca_de_trabalho = models.IntegerField(blank=True, null=True)
    qtd_navios_da_marinha = models.IntegerField(blank=True, null=True)
    qtd_forcas_paramilitares = models.IntegerField(blank=True, null=True)
    qtd_navios_de_patrulha = models.IntegerField(blank=True, null=True)
    qtd_portos = models.IntegerField(blank=True, null=True)
    qtd_pessoal_da_reserva = models.IntegerField(blank=True, null=True)
    qtd_lancadores_de_foguete = models.IntegerField(blank=True, null=True)
    qtd_artilharia_autopropulsada = models.IntegerField(blank=True, null=True)
    qtd_avioes_missoes_especiais = models.IntegerField(blank=True, null=True)
    area_total_m2 = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    qtd_submarinos = models.IntegerField(blank=True, null=True)
    qtd_tanques = models.IntegerField(blank=True, null=True)
    qtd_forca_total_de_aeronaves = models.IntegerField(blank=True, null=True)
    qtd_populacao_total = models.IntegerField(blank=True, null=True)
    qtd_artilharia_rebocada = models.IntegerField(blank=True, null=True)
    qtd_avioes_de_treinamento = models.IntegerField(blank=True, null=True)
    qtd_cargueiros = models.IntegerField(blank=True, null=True)
    qtd_hidrovias = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_global_power'
