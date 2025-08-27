import torch

# --------------------------
# 1. Fake batch of images
# --------------------------
# Shape: (batch_size=5, channels=1, height=224, width=224)
images = torch.randn(5, 1, 224, 224)   # 5 fake grayscale X-rays
print("Images shape:", images.shape)

# --------------------------
# 2. Labels (ground truth)
# --------------------------
# 0 = normal, 1 = pneumonia
labels = torch.tensor([0, 1, 1, 0, 1])
print("Labels:", labels)

# --------------------------
# 3. Fake model outputs (logits)
# --------------------------
# Shape: (batch_size, num_classes) -> (5, 2)
outputs = torch.tensor([[ 2.1, -0.3],   # model thinks class 0 ("normal")
                        [-0.5,  1.7],   # model thinks class 1 ("pneumonia")
                        [ 0.2,  0.1],   # model thinks class 0
                        [-1.2,  2.8],   # model thinks class 1
                        [ 0.5,  0.9]])  # model thinks class 1
print("Outputs (logits):\n", outputs)

# --------------------------
# 4. Predictions with torch.max
# --------------------------
# max returns (max_value, index) for each row (sample)
_, predicted = torch.max(outputs, 1)
print("Predicted classes:", predicted)

# --------------------------
# 5. Accuracy calculation
# --------------------------
correct = (predicted == labels).sum().item()
total = labels.size(0)
accuracy = 100 * correct / total

print(f"Correct predictions: {correct}/{total}")
print(f"Accuracy: {accuracy:.2f} %")