# ...run_inference.py...
import utils
from pyneuralfx.models.rnn.gru import *
import torch
import librosa
import soundfile as sf
import yaml
import sys
import IPython.display as ipd

sys.path.append('./src')  # Ajuste se necessário

cmd = {'config': 'pre_trained/statichyper_gru_32/statichyper_gru.yml'}
args = utils.load_config(cmd['config'])

# Inicialize o modelo
nn_model = utils.setup_models(args)
nn_model = utils.load_model(
    'pre_trained/statichyper_gru_32',
    nn_model,
    device='cuda',
    name='best_params.pt'
)

# Carregue o áudio de exemplo
wav_x, sr = librosa.load('example_wavs/example.wav',
                         sr=nn_model.sample_rate, mono=True)
wav_x = torch.from_numpy(wav_x).unsqueeze(0).unsqueeze(0)

# Parâmetros de controle do pedal
cond = [0, 0]  # -1 ~ 1

# Inferência
wav_y_pred = utils.forward_func(
    wav_x, cond, nn_model, args['model']['arch'], 'cuda')
wav_y_pred = utils.convert_tensor_to_numpy(wav_y_pred, is_squeeze=True)

# Salve o áudio processado
sf.write('output_od3.wav', wav_y_pred, nn_model.sample_rate)

print('Processamento concluído! Ouça o arquivo output_od3.wav')

# Carregue a configuração e o modelo treinado
cmd = {'config': 'pre_trained/statichyper_gru_32/statichyper_gru.yml'}
args = utils.load_config(cmd['config'])
nn_model = utils.setup_models(args)
nn_model = utils.load_model(
    'pre_trained/statichyper_gru_32',
    nn_model,
    device='cuda',
    name='best_params.pt'
)

# Prepare exemplo de entrada para exportação
# Ajuste para o tamanho do seu áudio real
example_input = torch.randn(1, 1, 16000)
# Exemplo de condição (distortion, tone)
cond = torch.tensor([[0.0, 0.0]])

batch_size = example_input.shape[0]
hidden_size = nn_model.hidden_size if hasattr(
    nn_model, 'hidden_size') else 32  # ajuste conforme seu modelo
num_layers = nn_model.num_layers if hasattr(
    nn_model, 'num_layers') else 1      # ajuste conforme seu modelo

h0 = torch.zeros(num_layers, batch_size, hidden_size)

# Exporta para TorchScript
traced = torch.jit.trace(nn_model, (example_input, cond, h0))
traced.save("boss_od3_traced.pt")

# Exporta para ONNX
torch.onnx.export(
    nn_model,
    (example_input, cond),
    "boss_od3.onnx",
    input_names=['audio', 'cond'],
    output_names=['output'],
    opset_version=17
)

print("Exportação concluída! Arquivos boss_od3_traced.pt e boss_od3.onnx foram salvos.")
