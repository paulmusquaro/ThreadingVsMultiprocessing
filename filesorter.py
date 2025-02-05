import sys
from pathlib import Path
from shutil import copyfile
from threading import Thread
import logging


source_folder = None
output_folder = "dist"

for i in range(len(sys.argv)):
    if sys.argv[i] == "--source" or sys.argv[i] == "-s":
        source_folder = sys.argv[i + 1]
    elif sys.argv[i] == "--output" or sys.argv[i] == "-o":
        output_folder = sys.argv[i + 1]

if source_folder is None:
    print("You need to specify the path to the directory --source")
    sys.exit(1)

source = Path(source_folder)
output = Path(output_folder)
folders = []

def grabs_folder(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            grabs_folder(el)

def copy_file(path: Path) -> None:
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix[1:]
            ext_folder = output / ext
            try:
                ext_folder.mkdir(exist_ok=True, parents=True)
                copyfile(el, ext_folder / el.name)
            except OSError as err:
                logging.error(err)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(threadName)s %(message)s")

    folders.append(source)
    grabs_folder(source)
    print(folders)

    threads = []
    for folder in folders:
        th = Thread(target=copy_file, args=(folder,))
        th.start()
        threads.append(th)

    [th.join() for th in threads]
    print(f"Can be deleted {source}")