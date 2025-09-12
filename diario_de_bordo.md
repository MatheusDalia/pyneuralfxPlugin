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
**Ideias/Sugestões:** Documentar todas as adaptações no diário de bordo para justificar decisões técnicas no TCC. Validar o pipeline com menos dados e menos épocas, focando na demonstração do funcionamento.

### 22/08/2025

**Etapa/Atividade:** Inferência local com modelo pré-treinado Boss OD-3

**Descrição:**  
Optei por não realizar novo treinamento e foquei na execução do modelo pré-treinado Boss OD-3. Organizei o ambiente local, garantindo a instalação dos pacotes necessários (`torch`, `numpy`, `soundfile`, `librosa`, `pyyaml`). Ajustei os scripts para rodar a inferência, corrigindo problemas de importação de módulos e carregamento da configuração (usando `utils.load_config` para evitar erros de acesso por atributo).  
Preparei o arquivo de áudio de entrada e executei o script de inferência, que carregou corretamente o modelo pré-treinado (`best_params.pt`) e processou o áudio de exemplo. O resultado foi salvo com sucesso em `output_od3.wav`, permitindo análise subjetiva do efeito Boss OD-3 simulado.

**Erros Encontrados:**

- Importação de módulos (`frame_work.utils` vs `utils`)
- Carregamento da configuração como dict ao invés de objeto
- Dependências ausentes (`IPython`, etc.)
- Caminhos relativos e estrutura de arquivos

**Soluções Aplicadas:**

- Ajuste dos imports para refletir o diretório de execução
- Uso da função `utils.load_config` para carregar configurações corretamente
- Instalação dos pacotes necessários via pip
- Remoção de dependências desnecessárias para execução local
- Organização dos arquivos do modelo e áudio de entrada

**Resultado:**  
Consegui rodar a inferência do modelo Boss OD-3 localmente com tranquilidade, gerando o arquivo de saída `output_od3.wav` para comparação direta com o áudio original. O pipeline de inferência está funcional e pronto para ser utilizado na avaliação da qualidade da emulação do pedal OD-3.

### 22/08/2025

**Observação sobre desempenho:**  
Durante a execução local da inferência com o modelo pré-treinado Boss OD-3, notei que o tempo de processamento para gerar o arquivo de saída `output_od3.wav` foi elevado. Esse tempo de resposta é inviável para uso em tempo real, como seria necessário em um plugin de áudio (VST/AU).  
A lentidão pode estar relacionada à arquitetura do modelo, ao uso de CPU ao invés de GPU, ou à forma como o processamento em lote está implementado. Para aplicações práticas como plugins, seria necessário otimizar o modelo, converter para formatos mais leves (ex: ONNX, TorchScript), ou adaptar o pipeline para execução eficiente em tempo real.

**Sugestão:**  
Investigar alternativas de otimização e considerar limitações de desempenho na documentação e apresentação.

### 22/08/2025

**Etapa/Atividade:** Teste e exportação do modelo pré-treinado Boss OD-3

**Descrição detalhada:**  
Decidi focar na execução do modelo pré-treinado Boss OD-3, sem realizar novos treinamentos. Organizei o ambiente local, instalei todas as dependências necessárias e corrigi problemas de importação e configuração. Consegui rodar a inferência localmente, gerando o arquivo de saída `output_od3.wav` para análise subjetiva do efeito simulado.  
Avancei para a etapa de exportação do modelo, visando encapsular o sistema para uso em tempo real (ex: plugin VST/AU). Tentei exportar para TorchScript e ONNX, mas encontrei dificuldades técnicas: o método `forward` do modelo exige argumentos adicionais (`h0`), tornando o processo de exportação menos direto.  
Além disso, observei que o tempo de processamento para gerar o áudio é elevado, o que inviabiliza o uso do modelo em tempo real como plugin DSP. Esse gargalo pode estar relacionado à arquitetura do modelo, ao uso de CPU, ou à falta de otimizações específicas para inferência rápida.

**Erros Encontrados:**

- Importação de módulos e configuração como dict ao invés de objeto.
- Dependências ausentes e caminhos relativos.
- Exportação do modelo falhou por falta do argumento `h0` no método `forward`.
- Tempo de processamento muito alto para uso em tempo real.

**Soluções Aplicadas:**

- Ajuste dos imports e uso da função `utils.load_config`.
- Instalação dos pacotes necessários via pip.
- Remoção de dependências desnecessárias para execução local.
- Organização dos arquivos do modelo e áudio de entrada.
- Tentativa de exportação do modelo com inclusão do argumento `h0`.

**Resultado:**  
Consegui rodar a inferência do modelo Boss OD-3 localmente e gerar o arquivo de saída para análise. Identifiquei que a exportação do modelo requer ajustes adicionais e que o desempenho atual inviabiliza o uso como plugin em tempo real.  
Estou preocupado com a viabilidade da ideia original de encapsular o sistema como ferramenta DSP/plugin, pois o tempo de processamento não atende aos requisitos de latência para áudio em tempo real.  
Sugiro investigar alternativas de otimização, simplificação do modelo, ou uso de técnicas de compressão e aceleração de modelos para viabilizar a proposta do TCC.

### 22/08/2025

**Registro de dúvidas, inseguranças e dificuldades técnicas:**

Durante o processo de validação e exportação do modelo pré-treinado Boss OD-3, enfrentei diversas dificuldades técnicas e conceituais que levantaram preocupações sobre a viabilidade do projeto como ferramenta de áudio em tempo real (plugin DSP):

- **Exportação do modelo:**  
  Tive dificuldades para exportar o modelo treinado para TorchScript e ONNX devido à lógica dinâmica do método `forward`, especialmente o tratamento de tuplas de tensores para LSTM/GRU. O TorchScript não aceita certas operações dinâmicas, exigindo adaptações no código ou uso do `torch.jit.trace` com entradas específicas.

- **Dependências e ambiente:**  
  Enfrentei problemas de compatibilidade de pacotes, especialmente com o PyTorch em Python 3.12, exigindo migração para Python 3.10. Também houve dificuldades com importação de módulos e organização dos arquivos do projeto.

- **Desempenho:**  
  O tempo de processamento para gerar o áudio de saída é elevado, tornando inviável o uso do modelo em tempo real como plugin. Isso gera preocupação sobre a possibilidade de encapsular o sistema para uso prático em DAWs ou como DSP.

- **Inseguranças conceituais:**  
  Estou inseguro sobre a viabilidade de transformar o modelo em uma ferramenta que processe áudio em tempo real, com controle de parâmetros, devido à latência e limitações técnicas do pipeline atual.

- **Dúvidas sobre integração:**  
  Não está claro como exportar e integrar o modelo em frameworks de plugin (JUCE, HISE, etc.), nem como garantir que o processamento seja suficientemente rápido para uso profissional.

---

**Mensagem para o orientador:**

Olá professor,

Gostaria de compartilhar algumas dúvidas e preocupações que surgiram durante o desenvolvimento do projeto:

- Estou enfrentando dificuldades técnicas para exportar o modelo treinado em PyTorch para formatos como TorchScript ou ONNX, devido à lógica dinâmica do método `forward` e à necessidade de argumentos adicionais (como o estado oculto `h0`). O TorchScript não aceita certas operações, o que exige adaptações que não domino completamente.
- Tive problemas de compatibilidade de pacotes, especialmente com o PyTorch em Python 3.12, e precisei migrar para Python 3.10 para conseguir instalar e rodar tudo corretamente.
- O tempo de processamento do modelo para gerar o áudio de saída é muito alto, o que inviabiliza o uso em tempo real como plugin de áudio. Isso me preocupa, pois a ideia original era encapsular o sistema como uma ferramenta DSP, com controle de parâmetros e resposta rápida.
- Estou inseguro sobre como exportar e integrar o modelo em frameworks de plugin (como JUCE ou HISE), e não sei se o pipeline atual pode ser otimizado para atender aos requisitos de latência de aplicações profissionais.
- Tenho dúvidas se a arquitetura do modelo ou o próprio conceito do projeto são viáveis para uso prático, ou se seria necessário simplificar ou repensar a abordagem.

Gostaria de discutir alternativas, possíveis caminhos de otimização, ou até mesmo ajustes no escopo do projeto para garantir que o resultado seja aplicável e relevante.  
Agradeço pela orientação e estou aberto a sugestões para superar essas dificuldades.

---

28/08/2025
Etapa/Atividade: Empacotamento do modelo Boss OD-3 em Gradio App
Descrição:

Adaptei o script de inferência para funcionar como uma interface web usando Gradio.
Implementei sliders para controle dos parâmetros do modelo (cond1 e cond2), permitindo ajuste dinâmico pelo usuário.
O usuário pode fazer upload de um arquivo de áudio, ajustar os parâmetros e baixar o resultado processado.
Erros Encontrados:

Player do Gradio não tocava o áudio: resolvido garantindo que o arquivo de saída fosse válido.
Argumento source="upload" não suportado nas versões recentes do Gradio: removido.
Erro de importação do pacote torch devido à incompatibilidade com Python 3.12: resolvido criando ambiente virtual com Python 3.10.
Erro de incompatibilidade entre PyTorch e NumPy 2.x: resolvido fazendo downgrade do NumPy para versão 1.x.
Erro de importação do módulo pyneuralfx: resolvido ajustando o PYTHONPATH para incluir o diretório src e rodando o script da raiz do projeto.
Erro de caminho relativo do arquivo de configuração: resolvido rodando o script do diretório correto.
Falta de dependências (gradio, torch, einops, pyloudnorm, etc.): instaladas manualmente no ambiente virtual.
Soluções Aplicadas:

Criação de ambiente virtual com Python 3.10.
Instalação manual das dependências necessárias.
Downgrade do NumPy para garantir compatibilidade com PyTorch.
Ajuste do PYTHONPATH e diretório de execução para garantir importação dos módulos.
Adaptação do código para interface Gradio, removendo argumentos obsoletos e implementando sliders para parâmetros de controle.
Ideias/Sugestões:

Melhorar o design da interface Gradio, adicionar nomes descritivos para os sliders e garantir que o arquivo de saída seja único a cada execução.
Documentar todo o fluxo para facilitar reprodutibilidade e apresentação do TCC.
Testar com diferentes arquivos de áudio e valores de parâmetros para avaliar o comportamento do modelo.

28/08/2025
Observação sobre desempenho:
Durante testes com o Gradio App rodando localmente, notei que o tempo de processamento do modelo para áudios curtos (ex: 6 segundos) é muito elevado, chegando a cerca de 170 segundos para processar um único arquivo. Esse desempenho inviabiliza o uso prático do sistema para aplicações interativas ou em tempo real.

Possíveis causas:

O modelo é pesado e não otimizado para inferência rápida.
O processamento está sendo feito na CPU, sem uso de GPU.
O pipeline pode estar processando amostra por amostra ou com loops ineficientes.
O modelo RNN/GRU pode ser naturalmente lento para áudios longos.
Sugestões:

Testar uso de GPU, se disponível.
Reduzir taxa de amostragem dos áudios para acelerar testes.
Investigar otimizações no pipeline e processamento em lote.
Documentar essa limitação como desafio técnico no TCC e discutir alternativas.
