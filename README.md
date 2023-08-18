# Image Search, Similarity Analysis, and Image Processing

This repository contains a Python script that demonstrates the following functionalities:
- Retrieving images from a search query using the Google Custom Search API.
- Calculating text-image similarity scores using the BERT model.
- Performing various image processing operations using OpenCV.

## Getting Started

To run the script, follow the steps below:

1. **Prerequisites:** Ensure you have Python installed on your system.

2. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-repository.git

## Install Dependecies
- pip install requests transformers opencv-python-headless numpy

## Configure Google custom Search API
- Obtain an API key from the Google Cloud Console.
- Create a Custom Search Engine and note down its ID.

## Run the Script
- Open the main.py file in a text editor.
- Replace 'Your-API-Key' and 'Your-Custom-Search-Engine-ID' in the params dictionary with your actual API key and engine ID.
- Modify the search query q to the desired search term.
- Save the changes.

## Explanation
- The script sends a GET request to the Google Custom Search API to retrieve images based on the search query.
- BERT (Bidirectional Encoder Representations from Transformers) is used to calculate text-image similarity scores.
- OpenCV is used for various image processing operations, including grayscale conversion, blurring, edge detection, brightness adjustment, contrast adjustment, and 
  more.

## Output
- The best-matching image is saved as "best_matching_image.jpg".
- The processed images are displayed interactively to the user.

