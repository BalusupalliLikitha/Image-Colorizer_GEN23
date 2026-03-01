from diffusers import StableDiffusionInpaintPipeline
import torch
from PIL import Image
import numpy as np
import cv2

pipe = StableDiffusionInpaintPipeline.from_pretrained(
    "runwayml/stable-diffusion-inpainting",
    torch_dtype=torch.float32
)

pipe = pipe.to("cpu")


def create_mask(image):
    image_np = np.array(image)
    mask = np.zeros(image_np.shape[:2], dtype=np.uint8)

    h, w = mask.shape
    mask[int(h * 0.4):int(h * 0.9), int(w * 0.2):int(w * 0.8)] = 255

    return Image.fromarray(mask)


def change_outfit(image, option):
    prompts = {
        "Traditional": "person wearing Indian traditional saree, high quality",
        "Western": "person wearing western casual clothes, modern",
        "Formal": "person wearing formal business suit",
        "School Uniform": "person wearing school uniform"
    }

    mask = create_mask(image)

    result = pipe(
        prompt=prompts[option],
        image=image,
        mask_image=mask
    ).images[0]

    return result