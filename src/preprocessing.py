import cv2


def resize_image(image, width=None, height=None):
    """
    Resizes an image to specified width/height while preserving aspect ratio if only one dimension is given.

    Args:
        image (numpy.ndarray): The input image.
        width (int, optional): Desired width.
        height (int, optional): Desired height.

    Returns:
        numpy.ndarray: The resized image.
    """
    if width is None and height is None:
        return image

    h, w = image.shape[:2]

    if width is None:
        aspect_ratio = height / float(h)
        dimensions = (int(w * aspect_ratio), height)
    elif height is None:
        aspect_ratio = width / float(w)
        dimensions = (width, int(h * aspect_ratio))
    else:
        dimensions = (width, height)

    resized = cv2.resize(image, dimensions, interpolation=cv2.INTER_AREA)
    return resized


def convert_to_grayscale(image):
    """
    Converts a BGR image to grayscale.

    Args:
        image (numpy.ndarray): The input BGR image.

    Returns:
        numpy.ndarray: Grayscale image.
    """
    if len(image.shape) == 2:
        # Image is already grayscale
        return image
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def apply_gaussian_blur(image, kernel_size=(5, 5), sigma_x=0):
    """
    Applies Gaussian Blur to smooth out noise in the image.

    Args:
        image (numpy.ndarray): The input image (grayscale or BGR).
        kernel_size (tuple): Gaussian kernel size (width, height). Must be odd numbers.
        sigma_x (float): Gaussian kernel standard deviation in X direction.

    Returns:
        numpy.ndarray: Blurred image.
    """
    return cv2.GaussianBlur(image, kernel_size, sigma_x)


def preprocess_pipeline(image, target_width=None, kernel_size=(5, 5)):
    """
    Executes the full preprocessing pipeline:
    Resize -> Convert to Grayscale -> Apply Gaussian Blur

    Args:
        image (numpy.ndarray): Original BGR image.
        target_width (int, optional): Width to resize image to.
        kernel_size (tuple): Blur kernel size.

    Returns:
        numpy.ndarray: Preprocessed image.
    """
    # 1. Resize image (if target_width is specified)
    resized_img = resize_image(image, width=target_width)

    # 2. Convert to Grayscale
    gray_img = convert_to_grayscale(resized_img)

    # 3. Apply Gaussian Blur
    blurred_img = apply_gaussian_blur(gray_img, kernel_size=kernel_size)

    return blurred_img
