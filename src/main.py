import os
import sys
import cv2

# Import modular project components
from input_handler import select_and_load_image
from preprocessing import (
    resize_image,
    convert_to_grayscale,
    apply_gaussian_blur,
)
from parking_space_detector import (
    get_parking_spaces,
    extract_parking_space_crops,
    draw_parking_spaces,
)
from occupancy_detector import (
    detect_occupancy,
    DEFAULT_PIXEL_THRESHOLD,
)
from analytics import calculate_occupancy_metrics
from visualization import generate_final_visualization


def main():
    # Parse CLI choice if provided (e.g. 'python src/main.py 1' or 'python src/main.py 2')
    user_choice = sys.argv[1] if len(sys.argv) > 1 else None

    # 1. Step 1: Input Handler - Select and Load Image
    print("--- [Step 1: Input Handler] ---")
    image, prefix, image_path = select_and_load_image(choice=user_choice)

    if image is None:
        print("[Main] Execution stopped due to image loading failure.")
        return

    # Setup separate output filenames based on image prefix (e.g. 'parking1' or 'parking2')
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(base_dir, "output")
    os.makedirs(output_dir, exist_ok=True)

    preprocessed_path = os.path.join(output_dir, f"{prefix}_preprocessed.jpg")
    spaces_visualized_path = os.path.join(output_dir, f"{prefix}_spaces_visualized.jpg")
    occupancy_detected_path = os.path.join(output_dir, f"{prefix}_occupancy_detected.jpg")
    final_result_path = os.path.join(output_dir, f"{prefix}_final_result.jpg")

    pixel_threshold = DEFAULT_PIXEL_THRESHOLD

    # 2. Step 2: Preprocessing Pipeline
    print(f"\n--- [Step 2: Preprocessing Pipeline ({prefix})] ---")
    resized_image = resize_image(image, width=800)
    gray_image = convert_to_grayscale(resized_image)
    blurred_image = apply_gaussian_blur(gray_image, kernel_size=(5, 5))

    cv2.imwrite(preprocessed_path, blurred_image)
    print(f"Saved preprocessed image to: '{preprocessed_path}'")

    # 3. Step 3: Parking Space Identification
    print(f"\n--- [Step 3: Parking Space Identification ({prefix})] ---")
    parking_spaces = get_parking_spaces(image_key=prefix)
    print(f"Loaded {len(parking_spaces)} defined parking space coordinates for '{prefix}'.")

    extracted_regions = extract_parking_space_crops(resized_image, parking_spaces)
    print(f"Extracted {len(extracted_regions)} space regions.")

    # Draw and save spaces visualization
    spaces_visualized_img = draw_parking_spaces(resized_image, parking_spaces)
    cv2.imwrite(spaces_visualized_path, spaces_visualized_img)
    print(f"Saved spaces visualization to: '{spaces_visualized_path}'")

    # 4. Step 4: Occupancy Detection
    print(f"\n--- [Step 4: Occupancy Detection ({prefix})] ---")
    print(f"Using Pixel Count Threshold: {pixel_threshold}")
    occupancy_results = detect_occupancy(extracted_regions, threshold=pixel_threshold)

    print("\n" + "=" * 45)
    print(f"{'Space ID':<12} | {'Status':<10} | {'Pixel Count':<12}")
    print("=" * 45)
    for res in occupancy_results:
        print(f"{res['id']:<12} | {res['status']:<10} | {res['pixel_count']:<12}")
    print("=" * 45)

    # Draw and save occupancy detected image
    occupancy_img = draw_parking_spaces(resized_image, parking_spaces, occupancy_results)
    cv2.imwrite(occupancy_detected_path, occupancy_img)
    print(f"Saved occupancy detection image to: '{occupancy_detected_path}'")

    # 5. Step 5: Analytics
    print(f"\n--- [Step 5: Analytics ({prefix})] ---")
    metrics = calculate_occupancy_metrics(occupancy_results)
    print(f"Total Spaces      : {metrics['total_spaces']}")
    print(f"Occupied Spaces   : {metrics['occupied_count']}")
    print(f"Available Spaces  : {metrics['available_count']}")
    print(f"Occupancy Rate    : {metrics['occupancy_percentage']}%")

    # 6. Step 6: Visualization
    print(f"\n--- [Step 6: Visualization ({prefix})] ---")
    final_image = generate_final_visualization(
        resized_image,
        parking_spaces=parking_spaces,
        occupancy_results=occupancy_results,
        metrics=metrics
    )

    # Save final output image
    cv2.imwrite(final_result_path, final_image)
    print(f"Saved final annotated result to: '{final_result_path}'")

    # Display GUI window
    print(f"\nDisplaying results for '{prefix}'. Press any key on the image window to exit...")
    cv2.imshow(f"Smart Parking Detection - {prefix}", final_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
