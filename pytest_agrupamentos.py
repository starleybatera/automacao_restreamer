import requests

class TestAgrupamento:
    headers = {'Authorization': 'Token 8c331b31acbec8d42dd4e33e55681f070e76b7c1'}
    url_base_agrupamento = 'http://localhost:8000/agrupamentos/'

    def test_get_agrupamentos(self):
        resposta = requests.get(url=self.url_base_agrupamento, headers= self.headers)

        assert resposta.status_code == 200

    def test_get_agrupamento(self):
        resposta = requests.get(url=f'{self.url_base_agrupamento}1/', headers= self.headers)

        assert resposta.status_code == 200
    
    def test_post_agrupamento(self):
        agrupamento_novo = {
            "identificacao": "Engorda",
        }

        resposta = requests.post(url=self.url_base_agrupamento, headers= self.headers, data=agrupamento_novo)

        assert resposta.status_code == 201

    def test_put_agrupamento(self):
        agrupamento_atualizado = {
            "identificacao": "Engorda",
        }

        resposta = requests.put(url=f'{self.url_base_agrupamento}4/',headers=self.headers, data=agrupamento_atualizado)

        assert resposta.status_code == 200

    # def test_delete_agrupamento(self):
    #     resposta = requests.delete(url=f'{self.url_base_agrupamento}4/', headers=self.headers)

    #     assert resposta.status_code == 204

