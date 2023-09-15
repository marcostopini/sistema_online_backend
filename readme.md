### No Pycharm Criamos o projeto "Sistema_online"

### Instalando o Djando
```` 
pip install django
```` 

### Para atualizar o pip
```` 
 python -m pip install --upgrade pip
````

### Criando um projeto django
```` 
django-admin startproject sistema .
```` 

### Iniciando o Servidor (rodar a aplicação)
```` 
python manage.py runserver <porta>
O número da porta é opcional
```` 

### Para desligar o Servidor
```` 
Ctrl + break 
Ctrl + C
```` 

### Criando um App
```` 
Um app é responsável por um módulo da aplicação
e permite uma maior organização e legibilidade do projeto.
Para criar o app, utilizaremos o comando:

python manage.py startapp <nome_do_app>
Ex: python manage.py startapp cadastro

```` 

### Para criar o "urls.py"
```` 
Clicar com o botão direito em cima de "Cadastro"
Opção "New"
"Python file"
Colocar apenas "urls"
```` 

### Usuário e senha do Django
````
usuário : mvtopini
senha : 392549
````

### Para rodar a migração ....
```` 
 python manage.py migrate
 python manage.py createsuperuser
 
 python manage.py makemigrations
 python manage.py migrate
 

```` 




