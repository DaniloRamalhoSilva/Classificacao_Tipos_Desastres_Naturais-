# AGENTS.md

## Projeto
Classificação de Tipos de Desastres Naturais usando CNN

## Etapas Recomendadas

1. **Exploração e Entendimento do Dataset**
   - Analisar a quantidade de imagens por classe e possíveis desbalanceamentos.
   - Observar exemplos visuais.

2. **Pré-processamento das Imagens**
   - Redimensionar (ex.: 128x128 ou 224x224).
   - Normalizar valores dos pixels (0-1).
   - Aplicar data augmentation: rotação, flip, zoom, etc.

3. **Construção e Treinamento do Modelo CNN**
   - Definir arquitetura com camadas convolucionais, pooling, ReLU, dropout e camada final softmax.
   - Utilizar TensorFlow/Keras ou PyTorch.
   - Treinar com validação para monitorar desempenho.

4. **Avaliação do Modelo**
   - Métricas: Acurácia, Precision, Recall, F1-Score por classe.
   - Matriz de Confusão.
   - Análise de erros (quais classes são mais confundidas).

5. **Otimização**
   - Ajustar hiperparâmetros (camadas, filtros, taxa de aprendizado, etc.).
   - Testar transfer learning (ResNet, VGG, etc.).


---

## Entrega Esperada

- **Relatório Técnico** (no Google Colab ou Jupyter Notebook) contendo:

  - Descrição do dataset e análise exploratória.

  - Estrutura do modelo e justificativas.

  - Métricas de avaliação e gráficos.

  - Análise crítica dos resultados e sugestões de melhoria.

- **Código-fonte comentado** (preferencialmente em Notebook).

---

## Critérios de Avaliação
- Qualidade técnica da CNN.

- Clareza e profundidade da análise.

- Boas práticas de pré-processamento e data augmentation.

- Reflexão crítica sobre resultados e implicações.
