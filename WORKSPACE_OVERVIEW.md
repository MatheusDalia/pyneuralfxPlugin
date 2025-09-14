# PyNeuralFxPlugin: Documentação Completa

## Propósito do Projeto

O PyNeuralFxPlugin é uma toolkit para modelagem neural de efeitos de áudio, com foco em simular pedais de guitarra (ex: Boss OD-3) usando redes neurais profundas. O objetivo é permitir experimentos, treinamento, avaliação e inferência de modelos que emulam efeitos analógicos, com possibilidade de encapsular o resultado como plugin VST/DSP para uso em DAWs.

## Principais Funcionalidades

- Treinamento de modelos neurais para emulação de efeitos de áudio.
- Inferência: processa arquivos de áudio aplicando o efeito neural.
- Interface Gradio para uso interativo (upload, ajuste de parâmetros, download do resultado).
- Scripts para visualização, análise de perdas e comparação de resultados.
- Suporte a diferentes arquiteturas (GRU, LSTM, TCN, GCN, etc).
- Configuração flexível via arquivos YAML.

## Estrutura do Workspace

- `frame_work/`: scripts principais (treinamento, inferência, utilitários, visualização).
- `src/pyneuralfx/`: código dos modelos, funções de perda, etc.
- `pre_trained/`: modelos e configs prontos para inferência.
- `example_wavs/`: exemplos de áudio para teste.
- `docs/`: documentação detalhada (dataset, configuração, treinamento, avaliação).
- `tests/`: testes unitários.
- `assets/`: imagens para README e documentação.
- `gradio_app.py`: interface web para processamento neural interativo.

## Pipeline de Uso

### 1. Instalação

- Requer Python 3.10 (PyTorch não suporta 3.12+).
- Instale dependências:
  ```bash
  pip install torch gradio numpy soundfile librosa einops pyloudnorm ipython
  ```
- Recomenda-se uso de ambiente virtual.

### 2. Treinamento

- Edite o arquivo de configuração YAML em `configs/` para definir dataset, arquitetura, hiperparâmetros.
- Execute:
  ```bash
  cd frame_work
  python main_snapshot.py  # para snapshot modeling
  python main_full.py      # para full modeling
  ```
- O modelo treinado será salvo em `pre_trained/{nome}/best_params.pt`.

### 3. Inferência

- Use o script `run_inference.py` ou a interface Gradio:
  ```bash
  python gradio_app.py --config frame_work/pre_trained/statichyper_gru_32/statichyper_gru.yml
  ```
- Na interface Gradio:
  - Faça upload do áudio.
  - Ajuste os sliders de parâmetros (ganho, tone).
  - Baixe o resultado processado.

### 4. Visualização e Avaliação

- Use scripts em `frame_work/visualization.py` para comparar espectros, formas de onda e analisar o resultado.
- Analise curvas de perda com `loss_analysis/compare_loss.py`.

## Principais Scripts

- `gradio_app.py`: interface web para processamento neural.
- `frame_work/run_inference.py`: inferência via linha de comando.
- `frame_work/utils.py`: funções utilitárias (carregamento de modelo, conversão de tensores, etc).
- `frame_work/visualization.py`: geração de gráficos e comparação de áudio.
- `frame_work/saver.py`: salvar modelos e checkpoints.

## Configuração

- Arquivos YAML definem todos os parâmetros do experimento.
- Exemplo de configuração:
  ```yaml
  data:
    buffer_size: 8192
    sampling_rate: 44100
    inp_channels: 1
    out_channels: 1
    train_x_path: ...
    train_y_path: ...
    valid_x_path: ...
    valid_y_path: ...
    test_x_path: ...
    test_y_path: ...
  model:
    arch: gru
    rnn_size: 32
    ...
  ```
- Veja `docs/configuration.md` para detalhes de cada parâmetro.

## Dicas de Uso

- Sempre ajuste o PYTHONPATH para incluir `src/` ao rodar scripts que importam `pyneuralfx`.
- Para usar GPU, defina `device='cuda'` nos scripts e verifique se o modelo/tensores estão na GPU.
- Para Colab, use:
  ```python
  !PYTHONPATH=/content/pyneuralfxPlugin/src python gradio_app.py --share
  ```
- Se encontrar erros de importação, cheque o diretório de execução e o PYTHONPATH.

## Exemplos de Uso

- Processar áudio com o modelo Boss OD-3:
  ```bash
  python gradio_app.py --config frame_work/pre_trained/statichyper_gru_32/statichyper_gru.yml
  ```
- Treinar novo modelo:
  ```bash
  python main_snapshot.py --config configs/rnn/gru/novo_experimento.yml
  ```

## Limitações e Considerações

- O pipeline atual não é otimizado para tempo real (latência alta).
- Para uso como plugin VST/DSP, será necessário exportar o modelo e adaptar o pipeline para C++/JUCE/HISE.
- Compatibilidade de pacotes é crítica (PyTorch, NumPy <2, Python 3.10).

## Referências

- [PyNeuralFx paper](https://arxiv.org/abs/2408.06053)
- [Hyper Recurrent Neural Network](https://arxiv.org/abs/2408.04829)

## Créditos

- Projeto original por yytung, adaptado e expandido para TCC por Matheus Dalia.
- Licença MIT.

---

Para dúvidas, consulte os arquivos em `docs/` e o diário de bordo (`diario_de_bordo.md`).
