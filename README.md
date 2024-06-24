## Project Overview

Welcome to our Product Recommender System project for the Amazon Hack-on! This project showcases a product recommendation system that analyzes video content to detect clothing items and recommends top products based on image similarity. We utilize the YOLO model for image detection and the ResNet50 model for feature extraction. The recommendations are generated using cosine similarity to find the most similar products.

## How It Works

1. *Video Analysis:* The system processes a video file to detect clothing items using the YOLO model.
2. *Feature Extraction:* Detected images of clothing items are passed through the ResNet50 model to extract features.
3. *Similarity Calculation:* Using cosine similarity, the system compares the extracted features with a database of product images to find the top 10 most similar products.
4. *Recommendation:* The top 10 recommended products are displayed.

## Getting Started

### Prerequisites

Ensure you have the following dependencies installed:

- Python 3.0
- Required Python libraries (specified in requirements.txt)

### Installation

1. *Clone the repository:*

    ```sh
    git clone [https://github.com/your-repo/product-recommender.git](https://github.com/Soumyadeep-Dey36/HackOn_Stakers)
    

2. *Install the dependencies:*

    ```sh
    pip install -r requirements.txt
    

### Running the Demo

To see a demo of this project, simply run the main.py file:

```
python main.py
```

Team - Stakers (Amazon Hack On)
Members -
Soumyadeep Dey,
Pritam Raj,
Shubham Bisht,
Sidhant Mishra
