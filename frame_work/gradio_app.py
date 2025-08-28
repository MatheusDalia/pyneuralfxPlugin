import gradio as gr
import torch
import librosa
import soundfile as sf
import utils
from pyneuralfx.models.rnn.gru import *

# Inicialize o modelo uma vez
cmd = {'config': 'pre_trained/statichyper_gru_32/statichyper_gru.yml'}
args = utils.load_config(cmd['config'])
nn_model = utils.setup_models(args)
nn_model = utils.load_model(
    'pre_trained/statichyper_gru_32',
    nn_model,
    device='cpu',
    name='best_params.pt'
)


def process_audio(input_audio, cond1, cond2):
    # Carrega o áudio enviado pelo usuário
    wav_x, sr = librosa.load(input_audio, sr=nn_model.sample_rate, mono=True)
    wav_x = torch.from_numpy(wav_x).unsqueeze(0).unsqueeze(0)
    cond = [cond1, cond2]  # Parâmetros do usuário
    wav_y_pred = utils.forward_func(
        wav_x, cond, nn_model, args['model']['arch'], 'cpu')
    wav_y_pred = utils.convert_tensor_to_numpy(wav_y_pred, is_squeeze=True)
    output_path = "output_od3.wav"
    sf.write(output_path, wav_y_pred, nn_model.sample_rate)
    return output_path


iface = gr.Interface(
    fn=process_audio,
    inputs=[
        gr.Audio(type="filepath"),
        gr.Slider(-1, 1, value=0, label="Ganho"),
        gr.Slider(-1, 1, value=0, label="Tone")
    ],
    outputs=gr.Audio(type="filepath"),
    title="Boss OD-3 Neural Audio Processor",
    description="Faça upload de um arquivo de áudio e ajuste os parâmetros do modelo Boss OD-3."
)

if __name__ == "__main__":
    iface.launch()
