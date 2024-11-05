1. Porque é necessário desnormalizar as tabelas de dimensão num sistema de BI e porque isto não fere a integridade referencial do sistema.
	*Para otimizar agregações massivas retirando joins. Porque o sistema de BI é Read Only. Normalização serve para garantir a integridade referencial num sistema*.

2. Como é feita a persistência de hierarquias de clientes corporativos e atributos multivalorados em bancos de dados relacionais 
	*Tabela ponte*.

3. Cite alguns motivos pelos quais é difícil a persistência de dados de redes sociais em bancos de dados relacionais.
	*Schema Flexível e Dinâmico*.

4.  Cite dois objetivos pelos quais bancos de dados semi-estruturados são procurados pelas empresas nos dias atuais.
	*Schema Flexível e Dinâmico, Escalabilidade Horizontal; Resolvem bem Problemas Específicos, além disso são todos open source.*

5. Diferencie a escalabilidade horizontal e vertical para banco de dados. Exemplifique.
	 *Escalabilidade horizontal implica Banco de Dados Distribuído. Exemplo: Amazon,Google, TikTok.*
	 *Arquitetura vertical (monolítica) é exemplificada nos mainframes de bancos de dados tradicionais, como Itaú, Bradesco, Mastercard.*

6. Bancos não-relacionais são antigos, citando como exemplos IMS da década de 60. Cite alguns motivos pelos quais bancos NoSQL ganharam tanto destaque nos dias  de hoje.
	*1. São open source. 2. Escalabilidade horizontal. 3. Schema Flexível e Dinâmico. 4. Resolvem problemas bem específicos.*

7. O que é consistência eventual. Qual é uma tradução errada em pt-br que deve ser evitada.
	 *O que eu escrevo no nó primário, tem um delay para ser replicado nos nós secundários. A tradução errada para eventualmente consistência é pode não gravar*.

8. Enuncie o teorema CAP.
	*Num sistema distribuído, num instante, só é possível termos duas das 3 características (Consistência, Disponibilidade, Particionamento). Em geral abro mão da consistência forte para ter mais disponibilidade.*

9. Por que é difícil comparar bancos NoSQL entre si.
	*Porque atendem necessidades específicas.*

10. Dizemos que fazemos a modelagem no banco relacional Botton Up e no MongoDB Top Down. Explique.
	*No relacional partimos da tupla definida na normalização para o objeto, via ORM, de baixo pra cima. No Mongo DB  preciso saber qual o uso do dado, para definir as collections, de "cima" para baixc.*

11. O MongoDB não aceita "transações" (a partir da versão 4 existe um certo tipo de transação), porém ele é muito utilizado. Em que cenários ele é competitivo e quais ele não é recomendável.
	*Competitivo para aplicação específicas, bem definidas, não recomendável para sistemas grandes e genéricos, como Sistemas de Cartão de Crédito.*

12. O que é um upsert.
	 *Se o documento já existe, atualiza, senão insere.*

13. Disserte sobre Schema Design no MongoDB. 1:1, 1:N e N:N. Preencher os comentários acerca de frequencia de uso e tamanho do documento, ou da cardinalidade abaixo.
	*RH:CV 1:1*
	*Se o CV é muito acessado ou grande demais faço outra collection, senão insiro em RH*
	*Post:comentários 1:N* 
	*Se a cardinalidade é pequena, insiro comentários como uma lista de Post*
	*Cidade: Habitantes*
	*Se a cardinalidade é alta Habitantes é uma collection separada*
	*Autores:Livros N:N*
	*Ambas cardinalidades são pequenas, então posso inserir livros em autores ou vice-versa, de acordo com o maior uso*

14. O que é o sharding no MongoDB. Isso pressupõe algum gargalo no banco de dados.
	*Particionamento horizontal da Collection. Tudo tem que passar pelo MongoS.*

15. Cite duas vantagens de um banco colunar para agregações massivas de um sistema de BI.
	1. *Não preciso fazer FULL SCAN do registro todo, com todas as .*
	2. *Posso colocar indices na coluna.*
	3. *Fator de compactação em disco é muito maior.*

16. Fale sobre as opções de persistência do Redis. O que significa in memory database.
	*a. Sem persistência (basicamente cache de um sistema persistido em banco relacional)*
	*b. A cada X gravações ou Y milisegundos atualiza a base*
	*c. Grava tudo no append log.*

17. Qual é uma grande "desvantagem" do MongoDB em relação ao CouchDB. Explique.
	*CouchDB é ACID, porém isso torna o banco bem mais lento.*

18. No Redis explique a vantagem de inserts TTL (Time To Live). Como é feito o namespace dos databases.
	*TTL = Time To Live, o que gravo tem um tempo de vida definido*
	*Namespace = 0 1 2 ...*

19. No MongoDB qual é a função do _id.
	Vantagem da collection ser schema free.
	_id é a chave única do documento no cluster, produtividade no desenvolvimento.

20. O que são “fire-and-forget functions” e sua vantagem.
	*Gravo sem esperar resposta do servidor, vantagem é ser muito rápido.*

21. No MongoDB detalhe o findOne. O que são hint e explain. 
	*Encontra o primeiro documento que segue a sua query no cluster. Hint dá a ordem dos índices ao fazer uma query. Explain dá um log da última query para efeito de profile.*

22. Explique o que significa ser “linearmente escalável” no caso do Cassandra. Qual é a limitação deste NoSQL.
	*Ao aumentar o número de nós, aumenta proporcionalmente a disponibilidade. A limitação é que o Cassandra é Eventualmente Consistente, isto é, gravo um primário e tenho um delay para atualizar todos os secundários.*

23. O que é BASE e qual sua relação com ACID.
	*BASE é a relaxação (afrouxar) do ACID para ter maior escalabilidade.*

24. Exemplifique uma situação onde bancos NoSQL não são adequados.
	*Sistemas grandes e genéricos, como um sistema de cartão de crédito. Devido à modelagem TOP-DOWN que parte do uso dos dados.*

****Próximas questões são respondidas vendo o mini tutorial FISL ou os cursos M1 M2 M3, responder antes da prova P1****

