import zipfile
import pathlib


def make_archive(filepaths, destdir):
    destpath = pathlib.Path(destdir, "compressed.zip")
    with zipfile.ZipFile(destpath, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


if __name__ == '__main__':
    make_archive(filepaths=["bonus12.py", "bonus14.py"], destdir="dest")
