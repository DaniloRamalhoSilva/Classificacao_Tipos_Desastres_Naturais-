# 🌎 Classificação de Desastres Naturais com CNN

Este projeto utiliza **Redes Neurais Convolucionais (CNNs)** para classificar imagens de desastres naturais, como:

- 🌪️ Tornados  
- 🔥 Incêndios florestais  
- 🌊 Inundações  
- 🌋 Erupções vulcânicas  

Dataset: [Disaster Images Dataset (Kaggle)](https://www.kaggle.com/datasets/varpit94/disaster-images-dataset)

---

## 🚀 Objetivo
Desenvolver um modelo capaz de identificar automaticamente o tipo de desastre natural a partir de imagens reais, aplicando boas práticas de **deep learning** e **visão computacional**.

---

## 📂 Estrutura Recomendada
```bash
repo/
├─ notebooks/              # Jupyter/Colab Notebooks
├─ src/                    # Scripts auxiliares (pré-processamento, treino, avaliação)
├─ reports/                # Resultados, gráficos e métricas
├─ dataset/                # Dados
├─ README.md               # Este arquivo
├─ AGENTS.md               # Guia para execução do projeto
├─ main.py                 # Arquivo principal
└─ requirements.txt        # Bibliotecas
```

---

## 🛠️ Etapas Principais
1. **Exploração do Dataset** → análise de classes, exemplos e desbalanceamento.  
2. **Pré-processamento** → redimensionamento, normalização e *data augmentation*.  
3. **Construção da CNN** → camadas convolucionais + pooling + softmax.  
4. **Treinamento** → monitorar com validação, callbacks e checkpoints.  
5. **Avaliação** → acurácia, precision, recall, F1-Score, matriz de confusão.  
6. **Reflexão** → análise crítica e sugestões de melhoria.  

---

## 📊 Entregáveis
- **Relatório Técnico** (Colab/Notebook) com dataset, modelo, métricas e gráficos.  
- **Código-fonte comentado**.  
- **Análise crítica dos resultados** com propostas de otimização.  

---

## ⚙️ Tecnologias
- Python 3.10+  
- TensorFlow/Keras ou PyTorch  
- Scikit-learn, Matplotlib, Pandas, Seaborn  
- Albumentations (para *data augmentation*)  

---

## ▶️ Como Executar
### Google Colab
1. Abra o notebook principal.  
2. Conecte a GPU em *Runtime > Change Runtime Type*.  
3. Execute todas as células (o dataset será baixado automaticamente).  

### Local
```bash
# Criar ambiente virtual
python -m venv .venv
source .venv/bin/activate   # (Windows: .venv\Scripts\activate)

# Instalar dependências
pip install -r requirements.txt

# Executar treino (exemplo PyTorch)
python -m src.train --config configs/base.yaml
```

---

## 🏆 Critérios de Avaliação
- Qualidade técnica da CNN.  
- Clareza do relatório.  
- Uso adequado de pré-processamento e *augmentation*.  
- Reflexão crítica dos resultados.  

---

## ✨ Créditos
Desenvolvido como parte da disciplina **GS 2025.01 - 2TIA VC**.  
Inspirado pela importância da visão computacional na **prevenção e resposta a desastres naturais**.
