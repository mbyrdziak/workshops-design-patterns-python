class ImageRepository:
    def getImages(self):
        return [
            HighResolutionImage("image1.jpg"),
            HighResolutionImage("image2.jpg"),
            HighResolutionImage("image3.jpg"),
            HighResolutionImage("image4.jpg")
        ]


class Image:
    def showImage(self):
        raise NotImplementedError()


class HighResolutionImage(Image):
    def __init__(self, filename):
        self.filename = filename
        print("Loads {} image from disk into memory, heavy operation".format(
            self.filename))

    def showImage(self):
        print("Showing image: {}".format(self.filename))
