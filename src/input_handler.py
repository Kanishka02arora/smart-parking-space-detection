import os
import cv2

# Mapping of available image choices to filenames and output prefixes
AVAILABLE_IMAGES = {
    "1": {"filename": "parking.jpg", "prefix": "parking1", "name": "parking.jpg (Image 1)"},
    "2": {"filename": "parking2.jpg", "prefix": "parking2", "name": "parking2.jpg (Image 2)"},
}


def load_image(image_path):
    """
    Loads an image from the specified path using OpenCV.

    Args:
        image_path (str): Path to image file.

    Returns:
        numpy.ndarray or None: Loaded image array or None if loading fails.
    """
    if not os.path.exists(image_path):
        print(f"[Error] File not found: '{image_path}'")
        return None

    image = cv2.imread(image_path)
    if image is None:
        print(f"[Error] Failed to load image from '{image_path}'.")
        return None

    print(f"[Input Handler] Image loaded successfully from: '{image_path}' (Shape: {image.shape})")
    return image


def select_and_load_image(choice=None, data_dir=None):
    """
    Allows user to select which input image to load ('parking.jpg' or 'parking2.jpg').

    Args:
        choice (str, optional): '1' or '2' or filename. If None, prompts user in CLI.
        data_dir (str, optional): Directory path where images reside.

    Returns:
        tuple: (image_array, image_prefix, image_path) or (None, None, None) on error.
    """
    if data_dir is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_dir = os.path.join(base_dir, "data")

    # If no choice provided, prompt user interactively
    if choice is None:
        print("\nSelect Parking Image to Process:")
        print("  1. parking.jpg  (Image 1)")
        print("  2. parking2.jpg (Image 2)")
        user_input = input("Enter choice (1 or 2) [default: 1]: ").strip()
        choice = user_input if user_input in AVAILABLE_IMAGES else "1"

    choice_str = str(choice).strip()

    # Normalize choice key
    if choice_str in AVAILABLE_IMAGES:
        selected_info = AVAILABLE_IMAGES[choice_str]
    elif choice_str in ["parking.jpg", "parking1"]:
        selected_info = AVAILABLE_IMAGES["1"]
    elif choice_str in ["parking2.jpg", "parking2"]:
        selected_info = AVAILABLE_IMAGES["2"]
    else:
        print(f"[Input Handler] Invalid choice '{choice_str}'. Defaulting to parking.jpg (Image 1).")
        selected_info = AVAILABLE_IMAGES["1"]

    filename = selected_info["filename"]
    prefix = selected_info["prefix"]
    image_path = os.path.join(data_dir, filename)

    print(f"\n[Input Handler] Selected: {selected_info['name']}")
    image = load_image(image_path)

    return image, prefix, image_path
