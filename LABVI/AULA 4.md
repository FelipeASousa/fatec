#LabIV #IA #RedesNeurais
# Redes Neurais

Perceptron -> Neurônio artificial

Somatório de 1 vezes os pesos e verificação da função de ativação.

## Treinamento

20% do total para validação
20% para teste
60% para treinamento
**Época**: Conjunto total de dados.
![[RedesNeurais.jpeg]]
O treinamento de uma FFN pode ser visualizado como um ponto caminhado por um plano em um espaço tridimensional.
As soluções são buracos nesses espaço> Quanto mais profundo o buraco, melhor é a solução.
Dois fatores afetam o treinamento: taxa de aprendizagem e momentum

**Taxa de aprendizagem:** Define o passo no espaço. Um valor muito alto pode fazer com que voce pule um buraco, passando direto pela solução. Um valor muito baixo faz com que voce demore muito para encontrar um solução.

**Momentum:** Inércia. Um termo que evira mudanças bruscas de direção. Quanto maior o momentum, menor a troca de direção.
![[plano.jpeg]]

### Treinamento 

1. Inicia com pesos aleatórios
2. Para cada registro:
	1. Apresenta a Rede neural e verifica a saída.
	2. Calcula o erro com base na saída.
	3. Atualiza os pesos, com base na contribuição da base, taxa de aprendizagem e momentum
3. Verifica a Rede Neural
4. Se o resultado for negativo volta ao passo 2


