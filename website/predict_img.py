import os
from ultralytics import YOLO
import cv2, json, sys

def predict():
    # Define paths
    # IMAGE_DIR = 'C:/Users/User/Downloads/HackOn/website/images'
    IMAGE_DIR = os.path.join('.', 'static/images')
    DICTIONARY_DIR = os.path.join('.', 'static')
    image_path = os.path.join(IMAGE_DIR, 'snap.jpg')
    image_path_out = os.path.join(IMAGE_DIR, 'snap_out.jpg')
    cropped_dir = os.path.join(IMAGE_DIR, 'yolo_out')
    json_path = os.path.join(DICTIONARY_DIR, 'detected_obj.json')
    model_path = os.path.join('.', 'yolo_model.pt')
    
    def delete_files_in_folder(folder_path):
        try:
            # Iterate over all files in the folder
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                
                # Check if the path is a file and not a directory
                if os.path.isfile(file_path):
                    os.remove(file_path)  # Delete the file
                    print(f"Deleted: {file_path}")
            
            print(f"All files deleted from {folder_path}")
        except Exception as e:
            print(f"Error deleting files: {e}")

    # Example usage:
    delete_files_in_folder(cropped_dir)

    # Create directory for cropped images if it doesn't exist
    os.makedirs(cropped_dir, exist_ok=True)

    # Load a model
    model = YOLO(model_path)  # load a custom model

    # Read the image
    image = cv2.imread(image_path)
    H, W,_  = image.shape

    # Define threshold for filtering detections
    threshold = 0.5

    # Perform inference
    results = model(image)[0]

    # Initialize counter for detected objects
    detected_object_count = 0
    
    # Initialize dictionary to store labels and filenames
    detections_dict = {}

    # Process and annotate results
    cropped_count = 0
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            # Increment the detected object counter
            detected_object_count += 1

            # Get the label
            label = results.names[int(class_id)].upper()

            # Crop the detected region
            crop_img = image[int(y1):int(y2), int(x1):int(x2)]

            # Save the cropped image with class label in the filename
            crop_img_filename = f'{label}crop{cropped_count}.jpg'
            crop_img_path = os.path.join(cropped_dir, crop_img_filename)
            cv2.imwrite(crop_img_path, crop_img)
            cropped_count += 1

            # Append the cropped image path to the detections dictionary
            if label not in detections_dict:
                detections_dict[label] = []
            detections_dict[label].append({label: crop_img_filename})

    # Create a final dictionary with serial numbers
    final_dict = {str(i): detections for i, (label, detections) in enumerate(detections_dict.items())}

    # Save detections to JSON file
    with open(json_path, 'w') as json_file:
        json.dump(final_dict, json_file, indent=4)

    # Print the dictionary
    print(final_dict)

    # Print the number of objects detected
    print(f'Number of objects detected: {detected_object_count}')
    
# predict()
