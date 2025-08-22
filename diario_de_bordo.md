# Diário de Bordo do TCC

---

### 19/08/2025

**Etapa/Atividade:** Visualização da curva de loss do treinamento
**Descrição:** Ajustei o script `compare_loss.py` para plotar a curva de `train loss` e gerei o gráfico. O gráfico mostra que o erro de treinamento diminui progressivamente, indicando que o modelo está aprendendo a emular o pedal OD-3. A curva apresenta comportamento esperado: perda alta no início e queda ao longo das iterações, com pequenas oscilações naturais do processo de otimização.
**Erros Encontrados:** Inicialmente o gráfico estava vazio porque só havia um valor de `valid loss` no log. Corrigido para mostrar a curva de `train loss`.
**Soluções Aplicadas:** Modifiquei o script para incluir a curva de `train loss`.
**Ideias/Sugestões:** Seguir para a etapa de teste do modelo com dados reais e visualização de áudio processado. Documentar cada resultado e análise para o TCC.
Este documento tem como objetivo registrar todas as etapas, erros, soluções e ideias durante o desenvolvimento do TCC, focado no empacotamento de modelos de áudio para guitarra elétrica como plugin VST.

---

## Estrutura Sugerida

- **Data:**
- **Etapa/Atividade:**
- **Descrição:**
- **Erros Encontrados:**
- **Soluções Aplicadas:**
- **Ideias/Sugestões:**

---

## Entradas

### 19/08/2025

**Etapa:** Criação do diário de bordo
**Descrição:** Início da documentação do processo do TCC.
**Erros Encontrados:** Nenhum
**Soluções Aplicadas:** Nenhum
**Ideias/Sugestões:** Utilizar este arquivo para registrar todo o progresso, facilitando a escrita do relatório final.

---

_Adicione novas entradas abaixo conforme avança nas etapas._

### 19/08/2025

**Etapa/Atividade:** Leitura do README e definição do objetivo
**Descrição:** Li o README do PyNeuralFx para entender o funcionamento do toolkit. O objetivo definido é utilizar o sistema para emular o pedal Boss OD-3 e transformar essa emulação em um plugin VST.
**Erros Encontrados:** Dúvida sobre como integrar o modelo Python em um plugin VST (tecnologias diferentes).
**Soluções Aplicadas:** Mapeamento das estratégias possíveis: comunicação via API local, conversão do modelo para formato compatível, ou uso de frameworks específicos.
**Ideias/Sugestões:** Testar o modelo OD-3 localmente, criar um VST dummy com JUCE, e planejar integração Python ↔ VST. Documentar cada etapa para facilitar o desenvolvimento e o relatório final.

### 19/08/2025

**Etapa/Atividade:** Criação da pasta data e inclusão do dataset OD-3
**Descrição:** Criei a pasta `data` dentro de `frame_work/` e coloquei o dataset do Boss OD-3 nela, conforme orientações do README.
**Erros Encontrados:** Nenhum
**Soluções Aplicadas:** Organização do dataset na estrutura recomendada pelo projeto.
**Ideias/Sugestões:** Prosseguir com o preprocessamento dos dados usando o script `preproc_bossod3.py`.

### 19/08/2025

**Etapa/Atividade:** Execução do preprocessamento do dataset OD-3
**Descrição:** Executei o script `preproc_bossod3.py` para preprocessar os arquivos do dataset OD-3. O script processou todos os arquivos `.wav` conforme esperado, sem apresentar erros.
**Erros Encontrados:** Nenhum
**Soluções Aplicadas:** Execução direta do script conforme instruções do projeto.
**Ideias/Sugestões:** Verificar os arquivos gerados pelo preprocessamento e seguir para a configuração do experimento para treinamento/avaliação do modelo.

### 19/08/2025

**Etapa/Atividade:** Configuração e execução do treinamento do modelo OD-3
**Descrição:** Ajustei o arquivo de configuração `concat_gru.yml` para usar o dataset do Boss OD-3, corrigi os caminhos, taxa de amostragem, parâmetros `num_conds` e `norm_tensor`. Iniciei o treinamento do modelo, que apresentou lentidão devido ao número de épocas e tamanho do dataset.
**Erros Encontrados:**

- AssertionError devido à taxa de amostragem incorreta.
- RuntimeError relacionado ao uso de multiprocessing sem o bloco `if __name__ == '__main__'`.
- RuntimeError: input.size(-1) must be equal to input_size (ajustado alterando `num_conds`).
- AssertionError: len(norm_tensor) != num_conds (corrigido ajustando `norm_tensor`).
  **Soluções Aplicadas:**
- Corrigi a taxa de amostragem para 48000.
- Adicionei o bloco `if __name__ == '__main__'` ao script principal.
- Ajustei `num_conds` para 2 e `norm_tensor` para dois elementos.
- Iniciei o treinamento, que está rodando corretamente.
  **Ideias/Sugestões:**
- Reduzir o número de épocas para acelerar testes.
- Usar o modelo salvo até o momento para validação do pipeline e visualização dos resultados.
- Documentar todas as adaptações e decisões para facilitar o desenvolvimento e o relatório final.

### Explicações técnicas

**norm_tensor:**
É uma lista de valores usada para normalizar os parâmetros de controle do modelo. Cada elemento representa o intervalo de normalização para uma condição (ex: [[0, 100], [0, 100]] para dois controles). O número de elementos deve ser igual ao valor de `num_conds`.

**num_conds:**
Indica quantos parâmetros de controle (condições) o modelo recebe como entrada. Por exemplo, se o modelo usa dois controles (ex: ganho e tonalidade), `num_conds` deve ser 2. Isso afeta o formato dos dados e a arquitetura do modelo.

**Taxa de amostragem:**
É a frequência (em Hz) com que os dados de áudio são amostrados. O valor deve ser igual ao dos arquivos `.wav` do dataset. Se houver diferença entre o valor no arquivo de configuração e o dataset, o modelo não consegue processar os dados corretamente, gerando erros de incompatibilidade.

---

### 19/08/2025

**Etapa/Atividade:** Mapeamento inicial do repositório e definição do objetivo do TCC
**Descrição:** Explorei a estrutura do repositório PyNeuralFx, identifiquei os principais scripts, pastas e arquivos de configuração. O objetivo do TCC foi definido: emular o pedal Boss OD-3 usando redes neurais e encapsular o modelo como plugin VST para guitarra elétrica.
**Erros Encontrados:** Nenhum
**Soluções Aplicadas:** Mapeamento da estrutura e leitura do README para entender o fluxo de uso.
**Ideias/Sugestões:** Documentar cada etapa no diário, focar em reprodutibilidade e clareza para facilitar o relatório final.

### 19/08/2025

**Etapa/Atividade:** Download e organização do dataset Boss OD-3
**Descrição:** Baixei o dataset do pedal Boss OD-3 e organizei na pasta `frame_work/data/overdrive/boss_od3/` conforme instruções do projeto.
**Erros Encontrados:** Nenhum
**Soluções Aplicadas:** Estrutura de pastas ajustada para compatibilidade com scripts de preprocessamento.
**Ideias/Sugestões:** Garantir que os arquivos estejam corretamente nomeados e separados em subpastas `train`, `valid` e `test`.

### 19/08/2025

**Etapa/Atividade:** Preprocessamento do dataset
**Descrição:** Executei o script `preproc_bossod3.py` para dividir e preparar os dados de áudio. O script rodou sem erros, gerando os arquivos necessários para treinamento, validação e teste.
**Erros Encontrados:** Nenhum
**Soluções Aplicadas:** Execução direta do script, conferência dos arquivos gerados.
**Ideias/Sugestões:** Validar os dados preprocessados antes de iniciar o treinamento.

### 19/08/2025

**Etapa/Atividade:** Ajuste dos arquivos de configuração para treinamento
**Descrição:** Editei o arquivo `concat_gru.yml` para corrigir caminhos dos dados, taxa de amostragem, parâmetros `num_conds` e `norm_tensor`. Ajustei para garantir compatibilidade entre dados e modelo.
**Erros Encontrados:**

- AssertionError: taxa de amostragem incorreta
- RuntimeError: multiprocessing sem bloco `if __name__ == '__main__'`
- RuntimeError: input.size(-1) != input_size (ajuste de `num_conds`)
- AssertionError: len(norm_tensor) != num_conds
  **Soluções Aplicadas:**
- Corrigi taxa de amostragem para 48000
- Adicionei bloco `if __name__ == '__main__'` ao script principal
- Ajustei `num_conds` para 2 e `norm_tensor` para dois elementos
  **Ideias/Sugestões:** Reduzir número de épocas para testes rápidos, documentar todas as mudanças para facilitar reprodutibilidade.

### 19/08/2025

**Etapa/Atividade:** Treinamento do modelo OD-3
**Descrição:** Executei o treinamento do modelo usando o script principal. O processo foi monitorado, e a curva de loss foi gerada para análise do aprendizado.
**Erros Encontrados:** Inicialmente, o gráfico de loss estava vazio (apenas um valor de `valid loss`).
**Soluções Aplicadas:** Modifiquei o script de visualização para incluir a curva de `train loss`, tornando o gráfico informativo.
**Ideias/Sugestões:** Usar o modelo treinado para gerar outputs e comparar com áudio original.

### 19/08/2025

**Etapa/Atividade:** Visualização da resposta espectral do modelo
**Descrição:** Ajustei e executei o script `visualization.py` para restaurar o modelo treinado e gerar o gráfico de resposta espectral. O gráfico mostra que o modelo aprendeu características relevantes do pedal OD-3.
**Erros Encontrados:** Nenhum
**Soluções Aplicadas:** Conferência dos caminhos do modelo e config, execução do script e análise do gráfico gerado.
**Ideias/Sugestões:** Avançar para comparação de áudio processado (output do modelo vs. original) e iniciar planejamento para empacotamento como plugin VST.

### 19/08/2025

**Etapa/Atividade:** Tentativa de automação da geração e comparação de áudio processado
**Descrição:** Automatizei o script `visualization.py` para gerar o áudio processado pelo modelo e comparar com o original. Instalei as dependências necessárias (`numpy`, `soundfile`, `torch`).
**Erros Encontrados:**

- Erro de importação do pacote `torch` devido à incompatibilidade com Python 3.13.
- Não foi possível instalar `torch` via pip.
- Python 3.10 não estava instalado no sistema.
  **Soluções Aplicadas:**
- Sugeri migração do ambiente para Python 3.10 usando Homebrew.
- Instruí sobre criação de novo ambiente virtual e reinstalação das dependências.
  **Ideias/Sugestões:**
- Registrar o bloqueio de versão no diário de bordo.
- Retomar amanhã após instalar Python 3.10 e configurar o ambiente.

### 19/08/2025

**Etapa/Atividade:** Orientação para migração de ambiente Python
**Descrição:** Orientei sobre instalação do Python 3.10 via Homebrew, criação de ambiente virtual e reinstalação dos pacotes necessários para rodar PyTorch.
**Erros Encontrados:**

- Comando `python3.10` não encontrado.
- Ambiente virtual não foi criado corretamente.
  **Soluções Aplicadas:**
- Recomendei instalação do Python 3.10 e verificação do executável.
- Detalhei comandos para ativação do ambiente e instalação dos pacotes.
  **Ideias/Sugestões:**
- Retomar a automação dos testes de áudio após ambiente corrigido.

### 22/08/2025

**Etapa/Atividade:** Retomada do projeto e finalização da configuração do ambiente Python
**Descrição:** Retomei o projeto após registrar todas as etapas anteriores. Instalei o Python 3.10, criei e ativei o ambiente virtual, e reinstalei as dependências necessárias (`torch`, `numpy`, `soundfile`). O ambiente está pronto para continuar os testes de áudio e avançar para as próximas etapas do TCC.
**Erros Encontrados:** Inicialmente, o Python 3.10 não estava instalado e o ambiente virtual não foi criado corretamente.
**Soluções Aplicadas:** Instalei o Python 3.10 via Homebrew (ou pyenv), criei o ambiente virtual e instalei os pacotes necessários.
**Ideias/Sugestões:** Prosseguir com a geração e comparação dos áudios processados pelo modelo, validar a emulação do pedal OD-3 e avançar para o empacotamento como plugin VST.

### 22/08/2025

**Etapa/Atividade:** Revisão do processo de treinamento do modelo concat_gru
**Descrição:** Confirmei que o modelo concat_gru já foi treinado anteriormente, utilizando o arquivo de configuração `concat_gru.yml`, que define o número de épocas (`epochs`). Esclareci o conceito de época: cada época corresponde a uma passagem completa pelo dataset de treinamento, permitindo que o modelo ajuste seus parâmetros a cada ciclo. No experimento, o número de épocas estava alto (200), o que resultou em tempo de treinamento elevado (cerca de 4 horas para 2 épocas).
**Erros Encontrados:** Tempo de treinamento excessivo para o hardware disponível.
**Soluções Aplicadas:** Recomendei reduzir o número de épocas para 5 ou 10, diminuir o tamanho do dataset e o batch size para acelerar o processo. Sugeri interromper o treinamento quando necessário e usar o modelo salvo até o momento para validação do pipeline.
**Ideias/Sugestões:** Documentar todas as adaptações no diário de bordo para justificar decisões técnicas no TCC. Validar o pipeline com menos dados e menos épocas, focando na demonstração do funcionamento
