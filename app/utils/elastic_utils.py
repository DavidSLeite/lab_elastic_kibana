# Arquivo para funções elasticsearch

def create_index_mapping_if_not_exists(es, index):
    """ Função cria index caso não exista """
    mapping = {
        "mappings": {
            "properties": {
                "cor_veiculo": {"type": "text", "fields" : {"keyword" : {"type" : "keyword","ignore_above" : 256}}},
                "data_infracao": {"type": "date"},
                "geo_loc": {"type": "geo_point"},
                "local": {"type": "text", "fields" : {"keyword" : {"type" : "keyword","ignore_above" : 256}}},
                "placa_veiculo": {"type": "text", "fields" : {"keyword" : {"type" : "keyword","ignore_above" : 256}}},
                "tipo_infracao": {"type": "text", "fields" : {"keyword" : {"type" : "keyword","ignore_above" : 256}}}
            }
        }
    }

    if es.indices.exists(index = index):
        pass
        print(f'Index {index} found!')
    else:
        print('index not exists')
        try:
            print(f"Try create index: {index}, mapping: {mapping}")
            es.indices.create(index = index, body = mapping) 
        except:
            raise print("Error create index")
