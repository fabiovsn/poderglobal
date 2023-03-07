from rest_framework import serializers
from .models import PoderGlobal

class PoderGlobalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoderGlobal
        fields = [
            'nome_pais',
            'codigo_pais',
            'qtd_pessoal_ativo',
            'qtd_porta_avioes',
            'qtd_veiculos_blindados',
            'qtd_helicopteros_de_ataque',
            'qtd_pessoal_disponivel',
            'qtd_corvetas',
            'orcamento_de_defesa',
            'qtd_contratorpedeiro',
            'qtd_cacas_interceptadores',
            'qtd_disponivel_para_servico_militar',
            'qtd_fragatas',
            'qtd_porta_helicopteros',
            'qtd_helicopteros',
            'qtd_forca_de_trabalho',
            'qtd_navios_da_marinha',
            'qtd_forcas_paramilitares',
            'qtd_navios_de_patrulha',
            'qtd_portos',
            'qtd_pessoal_da_reserva',
            'qtd_lancadores_de_foguete',
            'qtd_artilharia_autopropulsada',
            'qtd_avioes_missoes_especiais',
            'area_total_m2',
            'qtd_submarinos',
            'qtd_tanques',
            'qtd_forca_total_de_aeronaves',
            'qtd_populacao_total',
            'qtd_artilharia_rebocada',
            'qtd_avioes_de_treinamento',
            'qtd_cargueiros',
            'qtd_hidrovias'
        ]