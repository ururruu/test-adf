import os


def main(filename: str):
    with open(f'files/{filename}', 'r') as file:
        print(file.read())
    with open(f'files/output_file.txt', 'w') as output_file:
        output_file.write('Test')


if __name__ == "__main__":
    filename = os.environ['input_file']
    main(filename)
