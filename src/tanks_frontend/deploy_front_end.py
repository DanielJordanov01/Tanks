import subprocess
import shutil
import os

if __name__ == '__main__':

    subprocess.run(["ng", "build", "--extractCss=true"])

    source_dir = 'dist/tanks/'
    source = os.listdir(source_dir)

    for file in source:

        if file.endswith(".css"):
            shutil.copy(os.path.join(source_dir, file), '../../static/css')

        if file.endswith(".js"):
            shutil.copy(os.path.join(source_dir, file), '../../static/js')

        if file.endswith(".ico"):
            shutil.copy(os.path.join(source_dir, file), '../../static/img')

    print('Done')
