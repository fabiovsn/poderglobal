# Generated by Django 4.1.7 on 2023-02-28 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TbGlobalPower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_pais', models.CharField(blank=True, max_length=100, null=True)),
                ('codigo_pais', models.CharField(blank=True, max_length=5, null=True)),
                ('qtd_pessoal_ativo', models.IntegerField(blank=True, null=True)),
                ('qtd_porta_avioes', models.IntegerField(blank=True, null=True)),
                ('qtd_veiculos_blindados', models.IntegerField(blank=True, null=True)),
                ('qtd_helicopteros_de_ataque', models.IntegerField(blank=True, null=True)),
                ('qtd_pessoal_disponivel', models.IntegerField(blank=True, null=True)),
                ('qtd_corvetas', models.IntegerField(blank=True, null=True)),
                ('orcamento_de_defesa', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('qtd_contratorpedeiro', models.IntegerField(blank=True, null=True)),
                ('qtd_cacas_interceptadores', models.IntegerField(blank=True, null=True)),
                ('qtd_disponivel_para_servico_militar', models.IntegerField(blank=True, null=True)),
                ('qtd_fragatas', models.IntegerField(blank=True, null=True)),
                ('qtd_porta_helicopteros', models.IntegerField(blank=True, null=True)),
                ('qtd_helicopteros', models.IntegerField(blank=True, null=True)),
                ('qtd_forca_de_trabalho', models.IntegerField(blank=True, null=True)),
                ('qtd_navios_da_marinha', models.IntegerField(blank=True, null=True)),
                ('qtd_forcas_paramilitares', models.IntegerField(blank=True, null=True)),
                ('qtd_navios_de_patrulha', models.IntegerField(blank=True, null=True)),
                ('qtd_portos', models.IntegerField(blank=True, null=True)),
                ('qtd_pessoal_da_reserva', models.IntegerField(blank=True, null=True)),
                ('qtd_lancadores_de_foguete', models.IntegerField(blank=True, null=True)),
                ('qtd_artilharia_autopropulsada', models.IntegerField(blank=True, null=True)),
                ('qtd_avioes_missoes_especiais', models.IntegerField(blank=True, null=True)),
                ('area_total_m2', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('qtd_submarinos', models.IntegerField(blank=True, null=True)),
                ('qtd_tanques', models.IntegerField(blank=True, null=True)),
                ('qtd_forca_total_de_aeronaves', models.IntegerField(blank=True, null=True)),
                ('qtd_populacao_total', models.IntegerField(blank=True, null=True)),
                ('qtd_artilharia_rebocada', models.IntegerField(blank=True, null=True)),
                ('qtd_avioes_de_treinamento', models.IntegerField(blank=True, null=True)),
                ('qtd_cargueiros', models.IntegerField(blank=True, null=True)),
                ('qtd_hidrovias', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tb_global_power',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Paises',
        ),
    ]