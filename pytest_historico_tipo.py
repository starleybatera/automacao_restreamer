import requests

class TestHistoricoTipo:
    headers = {'Authorization': 'Token 8c331b31acbec8d42dd4e33e55681f070e76b7c1'}
    url_base_historicos_tipos = 'http://localhost:8000/historicos_tipos/'

    def test_get_historicos_tipos(self):
        resposta = requests.get(url=self.url_base_historicos_tipos, headers= self.headers)

        assert resposta.status_code == 200

    def test_get_historico_tipo(self):
        resposta = requests.get(url=f'{self.url_base_historicos_tipos}1/', headers= self.headers)

        assert resposta.status_code == 200
    
    def test_post_historico_tipo(self):
        historico_tipo_novo = {
            "descricao": "Inseminação",
        }

        resposta = requests.post(url=self.url_base_historicos_tipos, headers= self.headers, data=historico_tipo_novo)

        assert resposta.status_code == 201

    def test_put_historico_tipo(self):
        historico_tipo_atualizado = {
            "descricao": "Inseminação Artificial",
        }

        resposta = requests.put(url=f'{self.url_base_historicos_tipos}6/',headers=self.headers, data=historico_tipo_atualizado)

        assert resposta.status_code == 200

    # def test_delete_historico_tipo(self):
    #     resposta = requests.delete(url=f'{self.url_base_historicos_tipos}6/', headers=self.headers)

    #     assert resposta.status_code == 204

