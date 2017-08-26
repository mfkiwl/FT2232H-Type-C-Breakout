
from zipfile import ZipFile
import os

PROJECT_NAME = "FT2232H Type-C"

FILES = [
    ('-F.Cu.gbr', '.GTL'),
    ('-F.Mask.gbr', '.GTM'),
    ('-F.SilkS.gbr', '.GTO'),

    ('-B.Cu.gbr', '.GBL'),
    ('-B.Mask.gbr', '.GBM'),
    ('-B.SilkS.gbr', '.GBO'),

    ('-Edge.Cuts.gbr', '.GML'),

    ('.drl', '.TXT'),
]

if __name__ == "__main__":

    zip_path = os.path.join('build', PROJECT_NAME + '.fusion.zip')
    # We rename the file to match
    with ZipFile(zip_path, 'w') as fzip:
        for file_name, zip_file_name in FILES:
            src = os.path.join('build', PROJECT_NAME + file_name)
            dst = os.path.join('build', PROJECT_NAME + zip_file_name)
            fzip.write(src, dst)
