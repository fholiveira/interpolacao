Interpolações
============

Implementações idiomáticas de alguns métodos de interpolação - mesmo que menos performáticas.

Para rodar você precisará do Python 3.3 e do virtualenv instalados. 

1. Preparando ambiente
    ```
    git clone https://github.com/fholiveira/interpolacao.git
    cd interpolacao
    virtualenv .sci
    source .sci/bin/activate
    ```
2. Instalando as dependências
    ``` 
    pip install -r requirements.txt
    ```
3. Rodando os testes
    ```
    nosetests testes/
    ```
