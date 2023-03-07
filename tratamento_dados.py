import pandas as pd
import sqlite3

# carrega arquivo
df = pd.read_csv('C:\Workspace\Django\global_power\global_firepower.csv')

# exclui colunas desnecessárias
df = df.drop(columns=['Coastline Coverage', 'Dedicated Attack',
                      'External Debt', 'Foreign Exchange/Gold',
                      'Merchant Marine Fleet', 'Mine Warfare',
                      'Oil Consumption', 'Oil Production',
                      'Oil Proven Reserves', 'Purchasing Power Parity',
                      'Railway Coverage', 'Reaching Mil Age Annually',
                      'Roadway Coverage', 'Shared Borders', 'Tanker Fleet'])

# traduz colunas para português
df = df.rename(columns={'country': 'pais',
                        'country_code': 'codigo_pais',
                        'Active Personnel': 'pessoal_ativo',
                        'Aircraft Carriers': 'porta_avioes',
                        'Armored Vehicles': 'veiculos_blindados',
                        'Attack Helicopters': 'helicopteros_de_ataque',
                        'Available Manpower': 'pessoal_disponivel',
                        'Corvettes': 'corvetas',
                        'Defense Budget': 'orcamento_de_defesa',
                        'Destroyers': 'contratorpedeiro',
                        'Fighters/Interceptors': 'cacas_interceptadores',
                        'Fit-for-Service': 'disponiveis_para_servico_militar',
                        'Frigates': 'fragatas',
                        'Helicopter Carriers': 'porta_helicopteros',
                        'Helicopters': 'helicopteros',
                        'Labor Force': 'forca_de_trabalho',
                        'Navy Ships': 'navios_da_marinha',
                        'Paramilitary': 'forcas_paramilitares',
                        'Patrol Vessels': 'navios_de_patrulha',
                        'Ports / Trade Terminals': 'portos',
                        'Reserve Personnel': 'pessoal_da_reserva',
                        'Rocket Projectors': 'lancadores_de_foguete',
                        'Self-Propelled Artillery': 'artilharia_autopropulsada',
                        'Special-Mission': 'avioes_missoes_especiais',
                        'Square Land Area': 'area_total_m2',
                        'Submarines': 'submarinos',
                        'Tanks': 'tanques',
                        'Total Aircraft Strength': 'forca_total_de_aeronaves',
                        'Total Population': 'populacao_total',
                        'Towed Artillery': 'artilharia_rebocada',
                        'Trainers': 'avioes_de_treinamento',
                        'Transports': 'cargueiros',
                        'Waterways (usable)': 'hidrovias'})

# cria conexão com banco
connection = sqlite3.connect('global_power/paises.db')
con = connection.cursor()

# cria a tabela tb_global_power

con.execute('''create table if not exists tb_global_power (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_pais VARCHAR(100),
    codigo_pais VARCHAR(5),
    qtd_pessoal_ativo INTEGER,
    qtd_porta_avioes INTEGER, 
    qtd_veiculos_blindados INTEGER,
    qtd_helicopteros_de_ataque INTEGER,
    qtd_pessoal_disponivel INTEGER, 
    qtd_corvetas INTEGER, 
    orcamento_de_defesa DECIMAL(16,2), 
    qtd_contratorpedeiro INTEGER, 
    qtd_cacas_interceptadores INTEGER,
    qtd_disponivel_para_servico_militar INTEGER, 
    qtd_fragatas, qtd_porta_helicopteros INTEGER, 
    qtd_helicopteros INTEGER, 
    qtd_forca_de_trabalho INTEGER,
    qtd_navios_da_marinha INTEGER, 
    qtd_forcas_paramilitares INTEGER, 
    qtd_navios_de_patrulha INTEGER, 
    qtd_portos INTEGER, 
    qtd_pessoal_da_reserva INTEGER,
    qtd_lancadores_de_foguete INTEGER, 
    qtd_artilharia_autopropulsada INTEGER, 
    qtd_avioes_missoes_especiais INTEGER, 
    area_total_m2 DECIMAL(16,2),
    qtd_submarinos INTEGER, 
    qtd_tanques INTEGER, 
    qtd_forca_total_de_aeronaves INTEGER, 
    qtd_populacao_total INTEGER, 
    qtd_artilharia_rebocada INTEGER,
    qtd_avioes_de_treinamento INTEGER, 
    qtd_cargueiros INTEGER, 
    qtd_hidrovias INTEGER
    );''')

connection.commit()

print('Tabela criada com sucesso!')

#insere valores na tabela
for index, row in df.iterrows():
    con.execute('''insert into tb_global_power (
        nome_pais, codigo_pais, qtd_pessoal_ativo, qtd_porta_avioes, qtd_veiculos_blindados, qtd_helicopteros_de_ataque,
        qtd_pessoal_disponivel, qtd_corvetas, orcamento_de_defesa, qtd_contratorpedeiro, qtd_cacas_interceptadores,
        qtd_disponivel_para_servico_militar, qtd_fragatas, qtd_porta_helicopteros, qtd_helicopteros, qtd_forca_de_trabalho,
        qtd_navios_da_marinha, qtd_forcas_paramilitares, qtd_navios_de_patrulha, qtd_portos, qtd_pessoal_da_reserva,
        qtd_lancadores_de_foguete, qtd_artilharia_autopropulsada, qtd_avioes_missoes_especiais, area_total_m2,
        qtd_submarinos, qtd_tanques, qtd_forca_total_de_aeronaves, qtd_populacao_total, qtd_artilharia_rebocada,
        qtd_avioes_de_treinamento, qtd_cargueiros, qtd_hidrovias 
    ) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);''',
                (row.pais, row.codigo_pais, row.pessoal_ativo, row.porta_avioes, row.veiculos_blindados, row.helicopteros_de_ataque,
                row.pessoal_disponivel, row.corvetas, row.orcamento_de_defesa, row.contratorpedeiro, row.cacas_interceptadores,
                row.disponiveis_para_servico_militar, row.fragatas, row.porta_helicopteros, row.helicopteros,
                row.forca_de_trabalho, row.navios_da_marinha, row.forcas_paramilitares, row.navios_de_patrulha,
                row.portos, row.pessoal_da_reserva, row.lancadores_de_foguete, row.artilharia_autopropulsada,
                row.avioes_missoes_especiais, row.area_total_m2, row.submarinos, row.tanques, row.forca_total_de_aeronaves,
                row.populacao_total, row.artilharia_rebocada, row.avioes_de_treinamento, row.cargueiros, row.hidrovias))

connection.commit()
con.close()

print('Valores inseridos com sucesso!')

