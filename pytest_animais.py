import requests

class TestAnimais:
    headers = {'Authorization': 'Token 8c331b31acbec8d42dd4e33e55681f070e76b7c1'}
    url_base_animais = 'http://localhost:8000/animais/'

    def test_get_animais(self):
        resposta = requests.get(url=self.url_base_animais, headers= self.headers)

        assert resposta.status_code == 200

    def test_get_animal(self):
        resposta = requests.get(url=f'{self.url_base_animais}5/', headers= self.headers)

        assert resposta.status_code == 200
    
    # def test_post_animal(self):
    #     animal_novo = {
    #         "identificacao": "004",
    #         "descricao": "Pintada",
    #         "cod_raca": "Holandesa",
    #         "cod_agrupamento": "Novilhas",
    #         "cod_historico": "Animal foi inseminado",
           
    #     }

    #     resposta = requests.post(url=self.url_base_animais, headers= self.headers, data=animal_novo)

    #     assert resposta.status_code == 201

    def test_put_animal(self):
        animal_atualizado = {
            "identificacao": "004",
            "descricao": "Manhosa",
            "cod_raca": "Holandesa",
            "cod_agrupamento": "Novilhas",
            "cod_historico": "Animal entrou em estágio de secagem",
            
        }

        resposta = requests.put(url=f'{self.url_base_animais}9/',headers=self.headers, data=animal_atualizado)

        assert resposta.status_code == 200

    # def test_delete_animal(self):
    #     resposta = requests.delete(url=f'{self.url_base_animais}1/', headers=self.headers)

    #     assert resposta.status_code == 204

