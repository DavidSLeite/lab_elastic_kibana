# pip install elasticsearch==6.3.1
from elasticsearch import Elasticsearch, helpers
from datetime import datetime
from utils.gerador_eventos import gera_eventos
from utils.elastic_utils import create_index_mapping_if_not_exists
import uuid
from random import randrange
import time

def main(qtd_registros_carga):
    """ Função principal """
    es = Elasticsearch(
            'http://localhost:9200'
        )

    # Gera lista com eventos
    events = gera_eventos(qtd_registros_carga)

    actions = []

    for event in events:

        data_index = event['data_infracao'].date()
        index = f"ix_infracoes_{data_index}"
        id = uuid.uuid4().hex

        action = {
            '_index': index,
            #'_type': '_doc',
            '_id': id,
            '_source': event
        }

        actions.append(action)

    # cria o index caso não exista
    create_index_mapping_if_not_exists(es, index)

    # insere dados no index
    try:
        bulk_response = helpers.bulk(es, actions)
        msg = bulk_response[0]
        return msg
    except:
        raise 'Erro de Carga no Elasticsearch'
    
if __name__ == '__main__':
    
    while True:
        qtd_registros_carga = randrange(1, 20)
    
        msg = main(qtd_registros_carga)

        print(f"Quantidade de registros inseridos {msg}")
        
        time.sleep(5)
