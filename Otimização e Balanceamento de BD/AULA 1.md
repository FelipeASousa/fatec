#OtimizacaoEBalanceamentoBD

**Objetivo**: Analisar e otimizar o desempenho de Banco de Dados.

## Otimização
Princípios básicos da otimização:
 - Pensar globalmente, corrija localmente.
 - Particionamento evita gargalos.
 - Custos de inicialização são altos, custos de execução são baixos.
 - Aprimore a utilização do servidor.
 - prepare-se para os ajustes e desvios.

### Pensar globalmente, corrija localmente.
- Compreensão global do problema e intervenção mínima.
- Quando corrigindo uma transação lenta, um modo  de pensar global é conhecer as transações envolvidas com aquela consulta.
- Conhecimento no projeto da aplicação.

### Particionamento evita gargalos
- Particionamento é a técnica utilizada para reduzir a carga em certo componente do sistema.
- Usualmente uma parte do sistema limita o seu funcionamento geral.
- É raro que um sistema esteja lento porque todas as usa partes estão.
- Particionamento pode levar a excesso de comunicação entre as frações.

### Custos de inicialização são altos, custos de execução são baixos.
- Bancos de dados:
	- Iniciar leitura em disco;
	- Latência no envio de mensagens;
	- Custo de parte e verificação de semântica do comandos;
	- Abertura de conexões.

 ### Aprimore a utilização do servidor.
 Alocação adequada dos recursos de um servidor se implica em três principais aspectos:
 - Os recursos disponíveis do cliente
 - Onde a informação está disponível
 - A interação do BD com as telas

*Pooling:* Checagem de registros a cada tempo.

