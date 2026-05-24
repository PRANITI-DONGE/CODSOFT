Image Captioning AI

Automatically generates text captions for images using deep learning.

How it works: ResNet50 extracts visual features from an image → LSTM decoder generates a caption word by word.

Demo

*"a dog running through the grass"*

Upload an image → model reads it → outputs a caption.

Tech Stack

-Dataset — Flickr8k (8,000 images, 5 captions each)
-Image model —  ResNet50 (pre-trained on ImageNet)
-Caption model — LSTM with Embedding layer
-Framework — TensorFlow / Keras
-Notebook — Google Colab

How to Run

1. Open the notebook in Google Colab
2. Set runtime to GPU (Runtime → Change runtime type → T4 GPU)
3. Run all cells top to bottom
4. Test with your own image using generate_caption()

Project Structure

image-captioning-ai/
├── image_captioning.ipynb   # Main notebook
├── best_model.h5            # Trained model weights
├── tokenizer.pkl            # Vocabulary tokenizer
└── README.md

Results

| Metric | Score |
|--------|-------|
| BLEU-1 | ~0.55 |
| BLEU-2 | ~0.35 |

Author

Made by 
Praniti Donge
