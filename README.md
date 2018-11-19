# Sistema de Gestão de Ordem de Serviço

O SIGOS é um sistema de gestão de ordem de serviço voltado para Parques Regionais de Manutenção. Ele foi desenvolvido durante a Operação Ricardo Franco, no ano de 2017. A versão inicial sofreu algumas modificações pela equipe de informática do Parque Regional de Manutenção 12. Mesmo assim, durante o uso verificou-se a necessidade de algumas melhorias, as quais foram feitas durante a operação em 2018. A ideia principal é que ele possa auxiliar no fluxo de uma ordem de serviço, substituindo um trabalho que era feito com papel e em planilhas por um processo informatizado.

**Cenário Inicial/Demanda**

Durante a Operação Ricardo Franco, no ano de 2017, criou-se um sistema voltado para o Parque Regional de Manutenção 12 (Pq R Mnt/12). O sistema desenvolvido recebeu o nome de Sistema de Gestão de Ordens de Serviço (SIGOS). Ele foi implementado, validado e aprovado. Entretanto, surgiram algumas oportunidades de melhorias, tais como atualizações do sistema e a correção de bugs. Dessa maneira, o presente projeto se justifica para que o SIGOS possa acompanhar as mudanças e crescer. Continuando assim a ser empregado e ampliando sua aplicação.  O projeto é de grande importância para o Pq R Mnt/12, uma vez que o sistema quando de sua implantação representou um grande avanço na gestão das ordens de serviço, entretanto com o passar do tempo algumas necessidades mudaram, e alguns bugs foram descobertos. A não correção pode levar o cliente a abandonar o sistema.


**Escopo**

O software especificado neste documento é uma ferramenta de gestão de ordens de serviço voltada à manutenção de viaturas e armamento. Atualmente o sistema só está funcionando para uma das oficinas do Pq R Mnt/12, apesar de ter sido projetado para ser um sistema genérico. A atualização software permitirá que pequenos erros no código sejam consertados, além de adicionar algumas funcionalidades pedidas pelo cliente.

O Software permite:

●	Adicionar Ordens de Serviço - permite que uma OS seja criada, especificando-se o que será feito, prazo e responsável. Iniciando-se o ciclo da manutenção (serviço);

●	Atualizar uma Ordem de Serviço - cada fase da manutenção possui um responsável e um status, o sistema permite que a OS mude de status e responsável à cada fase;

●	Consultar Ordens de Serviço - O Software permite que sejam feitas consultas com filtros, de forma que o cliente possa pesquisar por diversos critérios, como fase, status, período, responsável, etc, e;

●	Arquivar uma Ordem de Serviço - Ao final do ciclo e conclusão do serviço, a ordem de serviço deve ser arquivada. Ela permanecendo no banco de dados permite sua consulta para aferição de informações como prazo médio de conclusão, uso de peças e demandas mais comuns.    
	
O SIGOS 1.2.0 permite que tais tarefas sejam realizadas de maneira adequada, atendendo as atuais necessidades do cliente. Foram corrigidos erros de:

●	 permissão de visualização de OS, o adjunto de CP não conseguia visualizar, e;

●	 pequenos erros de indentação.

Além disso, foram adicionadas:

●	 novas caixas de OS, uma caixa de OS abertas e uma caixa de OS fechadas e na área de consulta, 

●	foi adicionada a funcionalidade exportar como csv, onde o usuário pode decidir quais campos do banco de dados deseja que conste na planilha.

**Equipe**

O projeto da versão 1.2.0 contou com uma equipe de 4 militares. O 1º Ten Voltan, a 1º Ten Marina Pessoa e a 1º Ten Fischer formaram a equipe de desenvolvimento do Software. O Cap Campana foi o consultor. Além desse, o  Pq R Mnt/12 disponibilizou o Sargento Leite para acompanhar o projeto.
A versão inicial do SIGOS tinha na sua equipe: Cap Narcélio, 1º Ten Pedro Lucas, 1º Ten Andrade, 1º Ten Victor.
Nas duas versões, contou-se ainda com o  apoio do Cap Campana, e do Ten Alves.

**Descrição do Software**

O SIGOS é um sistema de gestão de ordem de serviço voltado para os Parques Regionais de Manutenção. Ele foi desenvolvido durante a Operação Ricardo Franco, no ano de 2017. A versão inicial sofreu algumas modificações pela equipe de informática do Parque Regional de Manutenção 12. A ideia principal é que ele possa auxiliar no fluxo de uma ordem de serviço, substituindo um trabalho que era feito com papel e em planilhas por um processo informatizado.  Os materiais são divididos em classes, as Normas Administrativas Relativas ao Suprimento (NARSUP), estabelece o que seria cada uma das classes.

O Parque Regional de Manutenção 12 trabalha com as seguintes classes de materiais:

● Cl II  -      	Material de Intendência;

● Cl V - 		Armamento e Munição;

● Cl VI - 		Material de Engenharia e Cartografia;

● Cl VII - 		Material de Comunicações, Eletrônica e de Informática; e

● Cl  IX - 		Material de Motomecanização e Aviação.

O status de uma ordem de serviço(OS) pode ser:

1.	Aguardando ciente de abertura
2.	Aguardando inspeção
3.	Realizando inspeção
4.	Aguardando manutenção
5.	Em manutenção
6.	Aguardando testes
7.	Testes em execução
8.	Remanutenção
9.	Aguardando remessa
10.	Fechada - aguardando ciente
11.	Fechada - ciente dado

Inicialmente a Ordem de Serviço (OS) é aberta pelo o Chefe de Classe. Depois disso é enviado para o Chefe de Controle de Produção (Ch CP) que é quem autoriza a abertura da OS. Em seguida essa ordem é encaminhada para o Cmt de Pel responsável. Esse é o militar que  altera o status da OS de 2 à 8. Depois é encaminhada para o Chefe de Classe que verifica se está tudo como esperado, e encaminha para o Ch de CP que autoriza o fechamento da OS.
Durante a atualização do status é gravado o horário da operação, isso é importante para ter dados estatísticos de duração da manutenção. 


**Dependências**

A estrutura do sistema utilizou principalmente a framework Django, a linguagem de programação Python e o banco de dado MySQL.  No manual de instalação, por vezes se utilizaram comandos que instalam as versões mais recentes das ferramentas.  Entretanto, o sistema não se mostrou compatível com essas versões. As versões utilizadas durante o desenvolvimento foram as seguintes:

● Python 3.5.2

● Mysql ver 14.14 dist 5.7.20 for linux (x86_64) using Editline wrapper

● Django 1.11.7

Cabe aqui destacar que o Django utilizado foi a versão 1.11.7 , essa explicação é importante, pois o Django teve importantes modificações entre a versão 1 e a 2. Pelos testes, verificaram-se muitos problemas ao se tentar a utilização da versão mais recente do Django.

`sudo pip3 install django`

O comando a cima, instala a versão mais recente do Django. Ele deve ser substituído pelo seguinte comando. 

`sudo pip3 install django==1.11.7`


Outro ponto, é que a versão do Django utilizada, apresentou-se mais estável com a versão 3.5 do Python.  Assim, o comando:

`sudo apt-get install python3`

Deve ser substituído pelo comando:

`sudo apt-get install python3.5`


**Requisitos de Hardware e Sistema Operacional**

Realizaram-se testes com as seguintes configurações:

● Hardware (físico ou virtual): 4 GB de RAM e 50 GB de armazenamento;

● Sistema Operacional: Testado com sucesso em Ubuntu Server LTS 16.0.4
