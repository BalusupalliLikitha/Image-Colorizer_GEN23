# AI Image Colorizer and Outfit Generator using CNN and Stable Diffusion

## Group Project Team

- B. Likitha , G Lakshmi Pavani , Charitardha , Mukthar Basha 

---

## Overview

This project develops an AI-based system that performs automatic image colorization and outfit generation using deep learning and Generative AI techniques.

The system converts black and white images into realistic color images using a Convolutional Neural Network (CNN) colorization model. Additionally, it generates new outfits on a person’s image using a Stable Diffusion Inpainting model based on text prompts.

The system helps enhance image quality and enables intelligent fashion transformation.

---

## Features

- Automatic black and white image colorization
- AI-based outfit generation
- Multiple outfit options (Traditional, Western, Formal, Uniform)
- High-quality and realistic output
- Mask-based clothing replacement
- Text-guided outfit generation
- Interactive Streamlit web application
- Works on CPU

---

## Tech Stack

Frontend:

- Streamlit

Backend:

- Python

Libraries Used:

- OpenCV
- NumPy
- PIL
- PyTorch
- HuggingFace Diffusers

---

## Model and Algorithm Used

### Image Colorization Model

Algorithm: CNN (Convolutional Neural Network)

Workflow:

- Input grayscale image
- Convert image into LAB color space
- Extract L channel
- CNN predicts a and b color channels
- Combine channels
- Convert LAB to RGB
- Generate final color image

Dataset Used:

- ImageNet Dataset
- Pretrained Caffe Model

---
## Architecture

<p align="center">
<img width="500" alt="Colorization Architecture" src="https://github.com/user-attachments/assets/140db497-b440-4c25-a006-9b6ce4aace1e" />
</p>

### Outfit Generator Model

Algorithm: Stable Diffusion Inpainting

Workflow:

- Input image
- Create mask on clothing region
- Provide text prompt
- Diffusion model generates new outfit
- Decoder converts latent to image
- Final output generated

Dataset Used:

- LAION-5B Dataset

---

## Architecture

<p align="center">
<img width="550" alt="Outfit Architecture" src="https://github.com/user-attachments/assets/42c36907-6688-47bf-9c88-c855db86db34" />
</p>
---

## Project Structure

```
image-colorizer-app/
│
├── assets/
│   ├── home.mp4
│   ├── col.jpeg
│   ├── fit.jpg
│   ├── colorization_architecture.png
│   └── outfit_architecture.png
│
├── dataset/
│
├── outfit/
│   └── outfit_model.py
│
├── pages/
│   ├── home.py
│   ├── colorizer.py
│   └── outfit.py
│
├── utils/
│   └── model.py
│
├── app.py
├── requirements.txt
└── README.md
```


## Applications

- Photo Restoration
- Fashion Industry
- Film and Media
- Historical Image Enhancement
- Virtual Try-On Systems

---

## Conclusion

This project demonstrates that deep learning and diffusion-based generative models significantly improve image quality and realism.

The CNN model successfully colorizes grayscale images, while the Stable Diffusion Inpainting model generates realistic outfits using text prompts and masked regions.

The system produces visually appealing and high-quality results and has applications in fashion, media, restoration, and creative AI fields.

Future improvements include GPU acceleration, higher resolution output, and more outfit generation options.

---
