import os
DOWNLOADS_PATH = os.getcwd()

def run ():
    os.chdir(DOWNLOADS_PATH)
    cur_path = os.getcwd()

    for file in os.listdir():
        file_path = os.path.join(cur_path, file)

        if os.path.isdir(file_path):
            continue

        ext = file.split('.').pop(-1)

        dir_path = os.path.join(cur_path, ext)

        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        os.replace(file_path, os.path.join(dir_path, file))

if __name__ == "__main__":
    run()
