import zipfile


def extract_archive(archivepath, destdir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(destdir)



if __name__ == '__main__':
    extract_archive("src/compressed.zip", "dest")