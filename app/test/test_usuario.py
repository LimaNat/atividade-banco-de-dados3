import pytest
from app.models.usuario_model import Usuario

@pytest.fixture
def usuario_valido():
    return Usuario("Maria", "maria@gmail.com", "12345")

def test_nome_invalido():
    with pytest.raises(TypeError, match="erro: o nome deve ser um texto"):
        Usuario(nome=13, email="maria@gmail.com", senha="12345")

def test_nome_vazio():
    with pytest.raises(TypeError, match="erro: o nome não pode estar vazio"):
        Usuario(nome="", email="maria@gmail.com", senha= "12345")

def test_email_invalido():
    with pytest.raises(TypeError, match="erro: o email deve ser um texto"):
        Usuario(nome="Maria", email=12345, senha="12345")

def test_email_vazio():
    with pytest.raises(TypeError, match="erro: o email não pode estar vazio"):
        Usuario(nome="Maria", email= "", senha="12345")

def test_senha_invalida():
    with pytest.raises(TypeError, match="erro: a senha deve ser um texto"):
        Usuario(nome="Maria", email= "maria@gmail.com", senha=12345)

def test_senha_vazia():
    with pytest.raises(TypeError, match="erro: a senha não pode estar vazia"):
        Usuario(nome="Maria", email= "maria@gmail.com", senha="")