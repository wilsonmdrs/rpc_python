# RPC - REMOTE PROCEDURE CALL IN PYTHON

Exemplo simples de uma chamada remota entre cliente e servidor 
simulando a comunicação entre dois clientes e o servidor, o qual armazena
a resposta dos dois clientes para responder de acordo

## Problema Proposto
* Fazer uma aplicação com dois clientes e um servidor
* cada cliente informa ao servidor se vai testemunhar;
* após o servidor ouvir os dois clientes retorna uma resposta contendo o veredito;

## Combinações de Respostas do Servidor após as inferências
* O juiz (servidor) julgará os prisioneiros (clientes) e decidirá a pena dos mesmos.

* Caso os dois clientes testemunhem um contra o outro (**SIM**) recebem 5 anos de prisão;

* Caso nenhum dos clientes testemunhe (**NÃO**) eles recebem 3 anos de prisão

* Caso um testemunhar e o outro não (**SIM** E **NÃO**)
    * Quem testemunhou (**SIM**) será solto
    * Quem não testemunhou (**NÃO**) receberá 10 anos de prisão 

# Preparando o Ambiente

### Ubuntu:

#### pip3
    $ sudo apt-get -y install python3-pip
    $ sudo apt-get update

#### Mac OS:

##### Homebrew

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    
#### pip3
    brew install python3


#### Windows:
    https://www.python.org/downloads/
   Install Python latest version from the link above
    
## Virtual Enviroment - Ambiente Virtual
    pip install virtualenv
    
## Iniciar Teste

Abrir 3 terminais na pasta **rpc_pyhthon** de comando e criar trës ambientes virtuais um em cada janela

#### servidor
    virtualenv server
    source server/bin/activate
    cd server
    python3 rpc_server.py run

#### Testemunha 01
    virtualenv testemunha_1
    source testemunha_1/bin/activate
    cd testemunha
    python3 testemunha.py run
    
#### Testemunha 02
    virtualenv testemunha_2
    source testemunha_2/bin/activate
    cd testemunha
    python3 testemunha.py run
    
Ao rodar **testemunha.py** irá abrir duas janelas.
Preencha o campo nome de ambas as telas e clique no botão que
sinaliza a resposta.
Abaixo na Label **Veredito** sairá a resposta do Juiz de acordo
com as combinações de resposta

    
