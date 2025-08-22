import os
import time
import collections
import numpy as np
import matplotlib.pyplot as plt


def load_loss(path_log):
    monitor_vals = collections.defaultdict(list)
    with open(path_log, 'r') as f:
        for line in f:
            try:
                line = line.strip()
                key, val, step, acc_time = line.split(' | ')
                monitor_vals[key].append((float(val), int(step), acc_time))
            except:
                continue
    data_val = dict()
    data_tra = dict()
    data_val['vals'] = [item[0] for item in monitor_vals['valid loss']]
    data_val['step'] = [item[1] for item in monitor_vals['valid loss']]
    data_val['time'] = [item[2] for item in monitor_vals['valid loss']]

    data_tra['vals'] = [item[0] for item in monitor_vals['train loss']]
    data_tra['step'] = [item[1] for item in monitor_vals['train loss']]
    data_tra['time'] = [item[2] for item in monitor_vals['train loss']]

    return data_val, data_tra


def make_loss_report(
    exp_list,
    title,
    path_fig='compare_result.png'
):

    fig = plt.figure(dpi=150)
    plt.title(title)
#     colors = ['b', 'r', 'g', 'black']
    for idx, (exp, exp_label) in enumerate(exp_list):
        path_log = os.path.join(exp, 'log_loss.txt')
        data_val, data_tra = load_loss(path_log)
        # Plotar curva de valid loss (se houver)
        if len(data_val['step']) > 0:
            plt.plot(data_val['step'], data_val['vals'],
                     label=exp_label + ' (valid)', linestyle='-')
        # Plotar curva de train loss
        if len(data_tra['step']) > 0:
            plt.plot(data_tra['step'], data_tra['vals'],
                     label=exp_label + ' (train)', linestyle=':')

    plt.yscale('log')
    plt.legend(loc='upper right')
    plt.tight_layout()
    # plt.xlim([0, 100000])
    # plt.ylim([0.001, 0.5])
    plt.savefig(path_fig)


if __name__ == '__main__':

    base_dir = './exp/compressor'
    path_fig = './loss_analysis/compare_result.png'
    exp_list = [
        (os.path.join(base_dir, 'test'), 'concat_gru'),
    ]
    make_loss_report(exp_list, f'Validation Loss Comparison', path_fig)
