#LABVI #IA

## Tipos de Dados

**Categórico**: Contem um numero finito de categorias ou grupos. Não podem ter uma ordem lógica e não aceitam operadores aritméticos.
**Quantitativo/Numérico**: Dados numéricos ou de data/hora que possuem ordem lógica e aceitam operadores aritméticos.
	*Discreto*: Quantidade finita de inteiros.
	*Continuo* - Quantidade infinita de valores reais ou de data/hora.

## KDD (Knowledge Discovery from Database)

- Seleção
- Pré-Processamento
- Transformação
- Mineração de Dados
- Avaliação

**Dicas**
	- No Pré-Processamento, para valores nulos usar média/moda da coluna para preencher ou remover esses valores do modelo. Não válido para modelos de Regressão.
	- Para OUTLIERS tirar o desvio padrão e a média.

### Transformação

- **Discretização**: Transformar numérico para categórico.
- **One-Hot Encoding:** Gera um novo atributo quantitativo binário para cada valor de um atributo categórico.

- **Simplificação dos dados**: Um único registro para armazenar uma determinada informação.
- **Engenharia de Atributos**: criação de novos atributos, por meio da transformação/combinação de atributos.

## Mineração de Dados

**Classificação:** Dados utilizados para reconhecer padrões;
**Regressão:** Dados utilizados para prever o valor de um atributo em um momento futuro
**Agrupamento:** Dados agrupados de acordo com uma métrica de distância definida pelo usuário.