import re

class Parser():
    def __init__(self, input_path: str):
        self.input_path = input_path

    def parse(self):
        with open(self.input_path, 'r') as file:
            line = file.readline()
            print(line)


if __name__ == '__main__':
    parser = Parser('overview.built.css')
    parser.parse()