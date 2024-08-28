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
	- Para *OUTLIERS* tirar o desvio padrão e a média.

### Transformação

- **Discretização**: Transformar numérico para categórico.
- **One-Hot Encoding:** Gera um novo atributo quantitativo binário para cada valor de um atributo categórico.

- **Simplificação dos dados**: Um único registro para armazenar uma determinada informação.
- **Engenharia de Atributos**: criação de novos atributos, por meio da transformação/combinação de atributos.

## Mineração de Dados

**Classificação:** Dados utilizados para reconhecer padrões;
**Regressão:** Dados utilizados para prever o valor de um atributo em um momento futuro
**Agrupamento:** Dados agrupados de acordo com uma métrica de distância definida pelo usuário.

#### Padrão de IA
Treinar  = X maiúsculo
Descobrir = y minúsculo

* Não colocar colunas identificadoras em algoritmos
* Se a quantidade de valores strings, inteiros for semelhante a ao número de registros eliminar coluna (max=50%)
* Gerar cópias a medida do tratamento para economizar processamento

#### Normalização
- **Normalização**: Dados numéricos ficam no intervalo entre 0 e 1.
	- Retirar outliers antes.
- **Padronização**: Dados numéricos passam e a ter média 0 e desvio de padrão 1
- **One hot enconding**: Gera uma coluna binária para cada valor.
- **Discretização**: Transforma uma coluna numérica em categórica.
- **Explode**: Divide um campo multivalorado em várias linhas
- **Melt**: Transforma coluna em linhas