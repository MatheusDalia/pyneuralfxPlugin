import gradio as gr
import torch
import librosa
import soundfile as sf
from frame_work import utils
from pyneuralfx.models.rnn.gru import *
import sys
import os
import argparse

# Argument parser for config path


def get_config_path():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default=None,
                        help='Path to config file')
    args, _ = parser.parse_known_args()
    if args.config:
        return args.config
    # Default absolute path for Colab and local
    default_path = os.path.join(os.path.dirname(
        __file__), 'frame_work', 'pre_trained', 'statichyper_gru_32', 'statichyper_gru.yml')
    if os.path.exists(default_path):
        return default_path
    # Fallback to relative path
    return 'frame_work/pre_trained/statichyper_gru_32/statichyper_gru.yml'


# Inicialize o modelo uma vez
config_path = get_config_path()
args = utils.load_config(config_path)
nn_model = utils.setup_models(args)
nn_model = utils.load_model(
    os.path.dirname(config_path),
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
    iface.launch(share=True)
