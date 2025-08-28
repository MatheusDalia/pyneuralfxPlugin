import torch
import utils

# =========================
# Carregar o modelo treinado
# =========================
cmd = {'config': 'pre_trained/statichyper_gru_32/statichyper_gru.yml'}
args = utils.load_config(cmd['config'])
nn_model = utils.setup_models(args)

nn_model = utils.load_model(
    'pre_trained/statichyper_gru_32',
    nn_model,
    device='cpu',  # força CPU para exportação
    name='best_params.pt'
)

nn_model.eval()  # modo avaliação

# =========================
# Parâmetros do modelo
# =========================
num_layers = getattr(nn_model, 'num_layers', 1)
hidden_size = getattr(nn_model, 'hidden_size', 32)

# =========================
# Exemplo de entrada "dummy" para exportação rápida
# =========================
# Input menor só para TorchScript, não precisa ser 16k
example_input = torch.randn(1, 1, 16000)
cond = torch.tensor([[0.0, 0.0]])
batch_size = example_input.shape[0]
h0 = torch.zeros(num_layers, batch_size, hidden_size)

# =========================
# Exporta para TorchScript com otimização
# =========================
with torch.no_grad():
    # Trace (usado para exportar com GRU/RNN)
    traced = torch.jit.trace(nn_model, (example_input, cond, h0))

    # Salva o modelo final
    traced.save("boss_od3_traced.pt")

print("Exportação TorchScript concluída! Arquivo boss_od3_traced.pt gerado.")
