import os


def main(filename: str, file_dir: str = 'files'):
    with open(f'{file_dir}/{filename}', 'r') as file:
        print(file.read())
    with open(f'{file_dir}/output_file.txt', 'w') as output_file:
        output_file.write('Test')


if __name__ == "__main__":
    filename = os.environ['input_file']
    file_dir = os.environ['file_dir']
    main(filename, file_dir)
