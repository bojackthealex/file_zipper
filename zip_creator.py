import zipfile
import pathlib
def make_zip(filepath, dest_dir, zip_name):
    dest_dir = pathlib.Path(dest_dir, zip_name)
    with zipfile.ZipFile(dest_dir, "w") as zip_it:

        for file in filepath:
            file = pathlib.Path(file)
            zip_it.write(file, arcname=file.name)

