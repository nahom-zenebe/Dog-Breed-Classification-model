import torch
from torchvision import transforms
from PIL import Image

class_names = ["husky", "labrador", "poodle", "bulldog"]

model = ...  # define same architecture
model.load_state_dict(torch.load("model.pth", map_location="cpu"))
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

def predict(image: Image.Image):
    img = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(img)
        _, predicted = torch.max(outputs, 1)

    return class_names[predicted.item()]