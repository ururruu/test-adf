import os
import subprocess


def main(filename: str):
    # with open(f'app/files/{filename}', 'r') as file:
    #     print(file.read())
    with open(f'app/files/output_file.txt', 'w') as output_file:
        output_file.write('Test')


if __name__ == "__main__":
    print('Test')
    print('Test2')
    result = subprocess.run(['find', '.'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(result.stdout)
    filename = os.environ['input_file']
    main(filename)
