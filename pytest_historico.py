import requests

class TestHistorico:
    headers = {'Authorization': 'Token 8c331b31acbec8d42dd4e33e55681f070e76b7c1'}
    url_base_historicos = 'http://localhost:8000/historicos/'

    def test_get_historicos(self):
        resposta = requests.get(url=self.url_base_historicos, headers= self.headers)

        assert resposta.status_code == 200

    def test_get_historico(self):
        resposta = requests.get(url=f'{self.url_base_historicos}1/', headers= self.headers)

        assert resposta.status_code == 200
    
    def test_post_historico(self):
        historico_novo = {
            "descricao": "Animal foi inseminado",
            "data": "2021-01-24",
            "cod_tipo": "1"
        }

        resposta = requests.post(url=self.url_base_historicos, headers= self.headers, data=historico_novo)

        assert resposta.status_code == 201

    def test_put_historico(self):
        historico_atualizado = {
            "descricao": "Animal foi inseminado",
            "data": "2021-01-21",
            "cod_tipo": "2"
        }

        resposta = requests.put(url=f'{self.url_base_historicos}1/',headers=self.headers, data=historico_atualizado)

        assert resposta.status_code == 200

    # def test_delete_historico(self):
    #     resposta = requests.delete(url=f'{self.url_base_historicos}1/', headers=self.headers)

    #     assert resposta.status_code == 204

