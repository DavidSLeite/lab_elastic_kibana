# pip install Faker
from faker import Faker
from datetime import datetime, timedelta
from random import randrange

fake = Faker(['pt_BR'])

def gera_eventos(num: int) -> list:
    """ Função retorna lista com eventos """

    lista_tipo_infracao = [
        'Estacionar veículo em acostamento',
        'Parar Veiculo na calçada',
        'Usar buzina fora dos padrões estabelecidos pelo Contran',
        'Conduzir veículo sem os documentos obrigatórios (CNH e CRLV)',
        'Ter veículo imobilizado na via por falta de combustível (pane seca)',
        'Estacionar o veículo em locais com placa de proibido estacionar',
        'Ultrapassar pela direita',
        'Transitar em velocidade até 20% superior ao limite da via',
        'Transitar em velocidade inferior à metade do limite estabelecido para a via',
        'Usar aparelho de alarme que produza ruído que perturbe o sossego público',
        'Conduzir veículo com defeito de iluminação, sinalização ou lâmpadas queimadas',
        'Transitar em veículo com excesso de peso',
        'Dirigir o veículo usando calçado que não se firme nos pés',
        'Não usar cinto de segurança',
        'Deixar de prestar socorro à vítima de acidente de trânsito',
        'Estacionar veículo onde há placa de proibido estacionar',
        'Transitar pela contramão em vias com duplo sentido de circulação',
        'Deixar de dar preferência de passagem a pedestre quando este houver iniciado a travessia',
        'Transitar em velocidade mais de 20% até 50% superior à máxima permitida na via'
        'Conduzir veículo sem equipamentos obrigatórios',
        'Dirigir veículo com habilitação de categoria diferente',
        'Dirigir embriagado',
        'Usar veículo para apostar corrida na rua',
        'Recusar-se a fazer o exame de bafômetro',
        'Ultrapassar pela contramão',
    ]

    lista_eventos = []

    for i in range(num):
        numAleatorio = randrange(0, len(lista_tipo_infracao)-1)
        
        eventos = {
            'data_infracao': datetime.now()  + timedelta(hours=3),
            'geo_loc' : str(fake.local_latlng()[0]) + ', ' + str(fake.local_latlng()[1]),
            'local' : str(fake.local_latlng()[4]),
            'placa_veiculo': fake.license_plate(),
            'cor_veiculo': fake.safe_color_name(),
            'tipo_infracao': lista_tipo_infracao[numAleatorio]
        }
        lista_eventos.append(eventos)

    return lista_eventos