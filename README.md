# Laboratório Elasticsearch + Kibana

Neste repositório está disponível os arquivos necessários para configuração do ambiente de desenvolvimento.

## Pré requisitos:
* Docker
* Git
* Python

## Arquivo infra/docker-compose.yml
É um arquivo yml que contém as configurações para subir os recursos de Elasticsearch e Kibana com o Docker.

**Observação:** Ao clonar esse repositório, por favor criar os diretórios ```/infra/elasticsearch``` e ```/infra/kibana```

### Como executar o docker compose.
Com o docker e o docker-compose instalados basta baixar este repositório entrar na pasta ```/infra``` e rodar o comando abaixo:

```
sudo docker-compose up -d
```

Após o comando é necessário aguardar o download das imagens caso não exista.

Com os serviços iniciados, já é possível acessar os recusros pelo navegador.

Elasticsearch
```http://localhost:9200```

Kibana
```http://localhost:5601```

## Aplicação que cria indice e insere dados no Elasticsearch

No arquivo ```app/carga_elasticsearch.py``` contém um código pyhton com exemplos de como interagir com o Elasticsearch.

Basicamente é um código que a cada 5 segundos insere dados fictícios no index.
