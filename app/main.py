import os
import subprocess


def main(files_folder: str, filename: str):
    with open(f'{files_folder}/{filename}', 'r') as file:
        print(file.read())
    with open(f'{files_folder}/output_file.txt', 'w') as output_file:
        output_file.write('Test')


if __name__ == "__main__":
    print('Test')
    result = subprocess.run(['find', '.'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(result.stdout)
    filename = os.environ['input_file']
    files_folder = os.environ['files_folder']
    main(files_folder, filename)
