import cv2
import numpy as np

# Define a function to display a specific image output
def show_selected_output(output_dict, output_name):
    if output_name in output_dict:
        cv2.imshow(output_name, output_dict[output_name])
    else:
        print("Output not found!")

# Load the image
image = cv2.imread('best_matching_image.jpg')

# Perform image processing operations

# Convert the image to grayscale
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the grayscale image
blurred_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)

# Apply Canny edge detection to the blurred image
edged_image = cv2.Canny(blurred_image, 100, 200)

# Adjust image brightness using linear addition
brightness = 1.5
adjusted_image_brightness = cv2.addWeighted(image, 1, np.ones_like(image) * brightness, 0, 0, dtype=cv2.CV_8U)

# Adjust image contrast using element-wise multiplication
contrast = 1.5
adjusted_image_contrast = cv2.multiply(image, np.array([contrast]))

# Apply sharpening filter to the image
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
sharpened_image = cv2.filter2D(image, -1, kernel)

# Apply Gaussian blur for noise reduction
noise_reduction = 2
smoothened_image = cv2.GaussianBlur(image, (3, 3), noise_reduction)

# Apply Laplacian edge detection
edge_detection = cv2.Laplacian(image, -1)

# Apply embossing filter
embossing = cv2.filter2D(image, -1, np.array([[0, 1, 0], [0, 0, 0], [0, -1, 0]]))

# Apply thresholding to the image
threshold = 120
_, thresholded_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)

# Create a mask and perform inpainting to segment the image
mask = np.zeros(image.shape[:2], dtype=np.uint8)
segmented_image = cv2.inpaint(image, mask, 25, cv2.INPAINT_TELEA)

# Apply histogram equalization to the grayscale image
histogram_equalized_image = cv2.equalizeHist(grayscale_image)

# Create a dictionary to store the processed images
output_dict = {
    'Original Image': image,
    'Grayscale Image': grayscale_image,
    'Blurred Image':blurred_image,
    'Edged Image': edged_image,
    'Brigtness Image': adjusted_image_brightness,
    'Contrast Image': adjusted_image_contrast,
    'Sharpening': sharpened_image,
    'Noise Reduction': smoothened_image,
    'Laplacian Edge Image': edge_detection,
    'Embossing Filter': embossing,
    'Thresholding': thresholded_image,
    'Segmented Image':segmented_image,
    'Histogram Equalized Gray Scale Image' : histogram_equalized_image
}

# Display the processed images to the user
while True:
    print("Available outputs:")
    for output_name in output_dict.keys():
        print(f" - {output_name}")
    user_input = input("Enter the output name you want to see (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    show_selected_output(output_dict, user_input)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
