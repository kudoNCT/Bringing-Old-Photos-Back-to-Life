# from models import create_da_model
from pix2pixHD_model_DA import InferenceModel, Pix2PixHDModel
from pix2pixHD_model import InferenceModel, Pix2PixHDModel
import torchvision.transforms as transforms
from PIL import Image
import torch


def data_transforms(img, method=Image.BILINEAR, scale=False):
    ow, oh = img.size
    pw, ph = ow, oh
    if scale == True:
        if ow < oh:
            ow = 256
            oh = ph / pw * 256
        else:
            oh = 256
            ow = pw / ph * 256

    h = int(round(oh / 4) * 4)
    w = int(round(ow / 4) * 4)

    if (h == ph) and (w == pw):
        return img

    return img.resize((w, h), method)


def inference_model_domain_a():
    model_a = InferenceModel()

    img_transform = transforms.Compose(
        [transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]
    )
    mask_transform = transforms.ToTensor()

    input = Image.open('/media/phuonglt/DATA/276316531_5186187858069241_1446520985700743863_n.jpg').convert("RGB")
    input = img_transform(input)
    input = input.unsqueeze(0)
    mask = torch.zeros_like(input)

    inp = (input, mask)

    generated_image = model_a.forward(inp)
    print(generated_image)


