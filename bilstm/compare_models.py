
import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def compare_models(bilstm_metrics_path, bert_metrics_path):
    """
    So sánh BiLSTM với BERT từ các file metrics JSON
    """
    # Load metrics
    with open(bilstm_metrics_path, 'r') as f:
        bilstm_metrics = json.load(f)
    
    with open(bert_metrics_path, 'r') as f:
        bert_metrics = json.load(f)
    
    # Tạo bảng so sánh
    comparison_data = {
        'Metric': [
            'Test Accuracy',
            'Precision', 
            'Recall',
            'F1-Score',
            'AUC-ROC',
            'Model Size (MB)',
            'Parameters',
            'Inference Time (ms)',
            'Training Time (s)',
            'Memory Usage (MB)'
        ],
        'BiLSTM + Attention': [
            bilstm_metrics['accuracy_metrics']['accuracy'],
            bilstm_metrics['accuracy_metrics']['precision'],
            bilstm_metrics['accuracy_metrics']['recall'],
            bilstm_metrics['accuracy_metrics']['f1_score'],
            bilstm_metrics['accuracy_metrics']['auc_roc'],
            bilstm_metrics['performance_metrics']['model_size_mb'],
            bilstm_metrics['complexity_metrics']['total_parameters'],
            bilstm_metrics['performance_metrics']['inference_time_per_sample_ms'],
            bilstm_metrics['performance_metrics']['estimated_training_time_seconds'],
            bilstm_metrics['performance_metrics']['memory_usage_mb']
        ],
        'BERT': [
            # Sẽ được điền khi có dữ liệu BERT
            bert_metrics.get('accuracy_metrics', {}).get('accuracy', 0),
            bert_metrics.get('accuracy_metrics', {}).get('precision', 0),
            bert_metrics.get('accuracy_metrics', {}).get('recall', 0),
            bert_metrics.get('accuracy_metrics', {}).get('f1_score', 0),
            bert_metrics.get('accuracy_metrics', {}).get('auc_roc', 0),
            bert_metrics.get('performance_metrics', {}).get('model_size_mb', 0),
            bert_metrics.get('complexity_metrics', {}).get('total_parameters', 0),
            bert_metrics.get('performance_metrics', {}).get('inference_time_per_sample_ms', 0),
            bert_metrics.get('performance_metrics', {}).get('training_time_seconds', 0),
            bert_metrics.get('performance_metrics', {}).get('memory_usage_mb', 0)
        ]
    }
    
    df = pd.DataFrame(comparison_data)
    print("MODEL COMPARISON TABLE:")
    print("=" * 60)
    print(df.to_string(index=False))
    
    # Vẽ biểu đồ so sánh
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # Accuracy metrics
    accuracy_metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'AUC-ROC']
    bilstm_acc = df.iloc[0:5]['BiLSTM + Attention'].values
    bert_acc = df.iloc[0:5]['BERT'].values
    
    x = np.arange(len(accuracy_metrics))
    width = 0.35
    
    axes[0,0].bar(x - width/2, bilstm_acc, width, label='BiLSTM', color='lightblue')
    axes[0,0].bar(x + width/2, bert_acc, width, label='BERT', color='lightcoral')
    axes[0,0].set_title('Accuracy Metrics Comparison')
    axes[0,0].set_xlabel('Metrics')
    axes[0,0].set_ylabel('Score')
    axes[0,0].set_xticks(x)
    axes[0,0].set_xticklabels(accuracy_metrics, rotation=45)
    axes[0,0].legend()
    axes[0,0].set_ylim(0, 1)
    
    # Performance metrics
    perf_metrics = ['Model Size (MB)', 'Inference Time (ms)', 'Memory Usage (MB)']
    bilstm_perf = [df.iloc[5]['BiLSTM + Attention'], df.iloc[7]['BiLSTM + Attention'], df.iloc[9]['BiLSTM + Attention']]
    bert_perf = [df.iloc[5]['BERT'], df.iloc[7]['BERT'], df.iloc[9]['BERT']]
    
    x = np.arange(len(perf_metrics))
    axes[0,1].bar(x - width/2, bilstm_perf, width, label='BiLSTM', color='lightgreen')
    axes[0,1].bar(x + width/2, bert_perf, width, label='BERT', color='orange')
    axes[0,1].set_title('Performance Metrics Comparison')
    axes[0,1].set_xlabel('Metrics')  
    axes[0,1].set_ylabel('Value')
    axes[0,1].set_xticks(x)
    axes[0,1].set_xticklabels(perf_metrics, rotation=45)
    axes[0,1].legend()
    
    # Parameters comparison
    models = ['BiLSTM + Attention', 'BERT']
    params = [df.iloc[6]['BiLSTM + Attention'], df.iloc[6]['BERT']]
    
    axes[1,0].bar(models, params, color=['purple', 'gold'])
    axes[1,0].set_title('Model Parameters Comparison')
    axes[1,0].set_ylabel('Number of Parameters')
    
    # Training time comparison
    train_times = [df.iloc[8]['BiLSTM + Attention'], df.iloc[8]['BERT']]
    
    axes[1,1].bar(models, train_times, color=['teal', 'crimson'])
    axes[1,1].set_title('Training Time Comparison')
    axes[1,1].set_ylabel('Training Time (seconds)')
    
    plt.tight_layout()
    plt.savefig('model_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return df

# Sử dụng:
# df = compare_models('bilstm/bilstm_comprehensive_metrics.json', 'bert/bert_comprehensive_metrics.json')
