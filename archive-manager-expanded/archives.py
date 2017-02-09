class ArchiveReader(object):
    def __init__(self, location_path):
        self.location_path = location_path

    def read(self):
        raise NotImplementedError()


class ZipArchiveReader(ArchiveReader):

    def read(self):
        print("Reading files from zip archive")


class TarArchiveReader(ArchiveReader):

    def read(self):
        print("Reading files from tar archive")


class ArchiveWriter(object):
    def __init__(self, location_path):
        self.location_path = location_path

    def write(self, fileNames):
        raise NotImplementedError()

    def remove(self, fileName):
        raise NotImplementedError()


class ZipArchiveWriter(ArchiveWriter):

    def write(self, fileNames):
        print("Writing files to zip archive")

    def remove(self, fileName):
        print("Removing a file from zip archive")


class TarArchiveWriter(ArchiveWriter):

    def write(self, fileNames):
        print("Writing files to tar archive")

    def remove(self, fileName):
        print("Removing a file from tar archive")
