# -*- coding: utf-8 -*-
import numpy as np
import soundfile as sf
import torch
import utils
from pyneuralfxPlugin.vis.plotting import *
from pyneuralfxPlugin.vis.sysplotting import *


path_outdir = '.'
num_channel = 1

nn_model = None
num_conds = 2
sr = 48000
gain = 1
freq = 100


cmd = {
    'config': './exp/compressor/test/concat_gru.yml'
}

args = utils.load_config(cmd['config'])
nn_model = utils.setup_models(args)
nn_model = utils.load_model(
    args.env.expdir,
    nn_model,
    device='cpu',
    name='best_params.pt')

# device
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# system plotting
# plot_harmonic_response(path_outdir, args.data.sampling_rate, gain, freq, utils.forward_func, [1, 1], nn_model,  args.model.arch, device)
plot_sine_sweep_response_spec(path_outdir, args.data.sampling_rate, utils.forward_func, [
                              1, 1], nn_model,  args.model.arch,  device)

# wav comparison
# path_pred = '/home/yytung/projects/pyneuralfx/frame_work/exp/boss_od3/concat_gru_32/valid_gen/pred/output10_3.0_4.0.wav'
# path_anno = '/home/yytung/projects/pyneuralfx/frame_work/exp/boss_od3/concat_gru_32/valid_gen/anno/output10_3.0_4.0.wav'
# plot_spec_diff(path_anno, path_pred, '.', args.data.sampling_rate, 1)

# Caminhos dos arquivos de exemplo
input_wav = './example_wavs/snapshot_examples/input.wav'
output_wav = './example_wavs/snapshot_examples/output.wav'

# Gerar áudio processado pelo modelo

# Carregar áudio de entrada
x, sr_x = sf.read(input_wav)
assert sr_x == sr, f"Taxa de amostragem do input ({sr_x}) diferente do modelo ({sr})"

# Normalizar e preparar para o modelo
x_tensor = torch.from_numpy(x).float().unsqueeze(0).unsqueeze(0)
cond = [1, 1]  # Exemplo de condição, pode ser ajustado conforme o modelo

# Inferência
with torch.no_grad():
    y_pred = utils.forward_func(
        x_tensor, cond, nn_model, args.model.arch, device)
    y_pred_np = y_pred.squeeze().cpu().numpy()

# Salvar áudio processado
sf.write('output_model.wav', y_pred_np, sr)

# Comparar espectros e formas de onda
plot_spec_diff(output_wav, 'output_model.wav', '.', sr, num_channel)
plot_wav_displayment(output_wav, 'output_model.wav', '.', sr, num_channel)
