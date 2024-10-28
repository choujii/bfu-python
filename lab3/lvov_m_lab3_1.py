import sys
from pathlib import Path
import numpy as np
from skimage import io, util, transform

def apply_transformation(image_groups, transformation_func):
    for folder, images in image_groups:
        next_index = len(images)
        for image in images:
            image = (image * 255).astype(np.uint8)
            transformed_image = transformation_func(image)
            transformed_image = (transformed_image * 255).astype(np.uint8)
            io.imsave(f'{folder}/{str(next_index).zfill(4)}.jpg', transformed_image)
            next_index += 1

def get_transformation(option):
    def scale_down(image):
        return transform.rescale(image, 0.7, anti_aliasing=True, multichannel=True)

    def rotate_45(image):
        return transform.rotate(image, 45, resize=True)

    def flip_horizontally(image):
        return np.fliplr(image)

    def add_noise(image):
        return util.random_noise(image)

    def shift_image(image):
        tform = transform.SimilarityTransform(translation=(15, 26))
        return transform.warp(image, tform)

    def complex_change(image):
        image = scale_down(image)
        image = rotate_45(image)
        image = flip_horizontally(image)
        image = add_noise(image)
        image = shift_image(image)
        return image

    transformation_mapping = {
        1: scale_down,
        2: rotate_45,
        3: flip_horizontally,
        4: add_noise,
        5: shift_image,
        6: complex_change
    }
    return transformation_mapping.get(option)

def main():
    if len(sys.argv) != 2:
        print('Please provide the correct path as an argument.')
        return

    path = Path(sys.argv[1])
    images_by_folder = []

    for folder in path.iterdir():
        images_by_folder.append([str(folder), io.imread_collection(f'{folder}/*.jpg')])

    print("Choose a transformation:\n"
          "1. Scale down\n"
          "2. Rotate by 45 degrees\n"
          "3. Flip horizontally\n"
          "4. Add noise\n"
          "5. Shift\n"
          "6. Complex transformation\n")

    images_by_folder = [group for group in images_by_folder if len(group[1])]

    while True:
        try:
            choice = int(input("Enter the transformation number: "))
            if 1 <= choice <= 6:
                break
            else:
                print("Invalid choice, try again.")
        except ValueError:
            print("Please enter a valid number.")

    try:
        transformation_func = get_transformation(choice)
        apply_transformation(images_by_folder, transformation_func)
        print("Transformation applied successfully!")
    except Exception as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()
