# Python em Django com Vue Js
> Projeto Python3 na web com o Framework Django e Vue Js

## Configurações do projeto
### É recomendável isolar todo esse projeto em um ambiente Virtual(Miniconda),link do ambiente: https://docs.conda.io/en/latest/miniconda.html 
#### Todos os passos a seguir são feitos no cmd do Windows

``` bash

# Criando o ambiente virtual
conda create -n env python=3.7

# Ativando o ambiente
conda activate env

```
### Se preferir pode instalar o projeto na sua própria máquina, sem ambiente virtual, mas o Miniconda nos fornece Python e Pip(Gerenciador de pacotes python), esse ultimo que será muito utilizado. Lembre-se que terá que instalar o Python e o Pip separadamente.

``` bash

# Instalando Framework Django com o ambiente virtual já ativado
pip install django

# Instalando Biblioteca python para dar suporte a tipos de imagens
pip install Pillow

```

### Depois de instalar tudo, é só executar o projeto.

``` bash

# Dentro da pasta do projeto execute
python manage.py runserver

```

