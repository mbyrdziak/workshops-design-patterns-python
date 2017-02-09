from images import *


def main():
    images = ImageRepository().getImages()

    # user just want to show only one particular image
    images[2].showImage()

if __name__ == "__main__":
    main()
