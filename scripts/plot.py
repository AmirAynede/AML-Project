import matplotlib.pyplot as plt
import json
import sys
import os

def plot_training_curves(train_losses, val_losses, train_accuracies, val_accuracies, output_dir="outputs", prefix="training_curve"):
    os.makedirs(output_dir, exist_ok=True)
    epochs = range(1, len(train_losses) + 1)

    # === Plot Loss ===
    plt.figure(figsize=(6, 5))
    plt.plot(epochs, train_losses, 'b-', label='Training Loss')
    plt.plot(epochs, val_losses, 'r-', label='Validation Loss')
    plt.title("Loss Over Epochs")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()
    loss_plot_path = os.path.join(output_dir, f"{prefix}_loss.png")
    plt.savefig(loss_plot_path)
    plt.close()

    # === Plot Accuracy ===
    plt.figure(figsize=(6, 5))
    plt.plot(epochs, train_accuracies, 'b-', label='Training Accuracy')
    plt.plot(epochs, val_accuracies, 'r-', label='Validation Accuracy')
    plt.title("Accuracy Over Epochs")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.legend()
    acc_plot_path = os.path.join(output_dir, f"{prefix}_accuracy.png")
    plt.savefig(acc_plot_path)
    plt.close()

    print(f"✅ Saved loss plot to {loss_plot_path}")
    print(f"✅ Saved accuracy plot to {acc_plot_path}")

def load_metrics(json_path):
    if not os.path.exists(json_path):
        print(f"❌ File not found: {json_path}")
        sys.exit(1)
    with open(json_path, 'r') as f:
        metrics = json.load(f)
    return metrics

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 -m scripts.plot path/to/training_metrics.json")
        sys.exit(1)

    metrics_path = sys.argv[1]
    metrics = load_metrics(metrics_path)

    plot_training_curves(
        metrics["train_losses"],
        metrics["val_losses"],
        metrics["train_accuracies"],
        metrics["val_accuracies"],
        output_dir="outputs",
        prefix=os.path.splitext(os.path.basename(metrics_path))[0]
    )