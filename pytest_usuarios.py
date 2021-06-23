import requests

class TestUsuarios:
    headers = {'Authorization': 'Token 37f1a4cb241f8fc2821149307fe5b7516057a598'}
    url_base_usuarios = 'http://localhost:8000/usuarios/'

    def test_get_usuarios(self):
        resposta = requests.get(url=self.url_base_usuarios, headers= self.headers)

        assert resposta.status_code == 200

    def test_get_usuario(self):
        resposta = requests.get(url='http://localhost:8000/usuarios/1/', headers= self.headers)

        assert resposta.status_code == 200
    
    def test_post_usuario(self):
        usuario_novo ={
            "username": "paulo",
            "email": "paulo@gmail.com",
            "password": "paulo123"
        }

        resposta = requests.post(url=self.url_base_usuarios, headers= self.headers, data=usuario_novo)

        assert resposta.status_code == 201

    def test_put_usuario(self):
        usuario_atualizado = {
            "username": "paulo",
            "email": "paulo@gmail.com",
            "password": "paulo1234"
        }

        resposta = requests.put(url='http://localhost:8000/usuarios/6/',headers=self.headers, data=usuario_atualizado)

        assert resposta.status_code == 200

    # def test_delete_usuario(self):
    #     resposta = requests.delete(url=f'{self.url_base_usuarios}5/', headers=self.headers)

    #     assert resposta.status_code == 204

