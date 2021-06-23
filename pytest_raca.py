import requests

class TestRaca:
    headers = {'Authorization': 'Token 8c331b31acbec8d42dd4e33e55681f070e76b7c1'}
    url_base_raca = 'http://localhost:8000/racas/'

    def test_get_racas(self):
        resposta = requests.get(url=self.url_base_raca, headers= self.headers)

        assert resposta.status_code == 200

    def test_get_raca(self):
        resposta = requests.get(url=f'{self.url_base_raca}1/', headers= self.headers)

        assert resposta.status_code == 200
    
    def test_post_raca(self):
        raca_novo = {
            "descricao": "Inseminação",
        }

        resposta = requests.post(url=self.url_base_raca, headers= self.headers, data=raca_novo)

        assert resposta.status_code == 201

    def test_put_raca(self):
        raca_atualizado = {
            "descricao": "Girolando",
        }

        resposta = requests.put(url=f'{self.url_base_raca}3/',headers=self.headers, data=raca_atualizado)

        assert resposta.status_code == 200

    # def test_delete_raca(self):
    #     resposta = requests.delete(url=f'{self.url_base_raca}3/', headers=self.headers)

    #     assert resposta.status_code == 204

