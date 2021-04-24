from PIL import Image
import numpy


class Game:

    def __init__(self, rows, columns, image_name):
        self.rows = rows
        self.columns = columns
        self.image_name = image_name
        self.image_matrix = self.import_image_and_convert_to_matrix()
        self.hint_matrix = self.generate_matrix_with_hints()
        self.minimal_hint_matrix = self.create_minimal_hint_matrix()

    def import_image_and_convert_to_matrix(self):
        with Image.open(self.image_name, 'r') as image:
            image = image.resize((self.columns, self.rows))

            threshold = lambda x: 0 if x > 175 else 1
            image = image.convert('L').point(threshold, mode='1')

            pixels = list(image.getdata())

            image_matrix = numpy.reshape(pixels, (-1, self.columns))

            return image_matrix

    def generate_matrix_with_hints(self):
        hint_matrix = numpy.empty([self.rows, self.columns], int)

        for i in range(self.rows):
            for j in range(self.columns):
                hint_matrix[i][j] = self.calculate_number_of_neighbors(i, j)

        return hint_matrix

    def calculate_number_of_neighbors(self, x, y):
        number_of_neighbors = 0
        for i in range(max(0, x - 1), x + 2 if x + 2 < self.rows else self.rows):
            for j in range(max(0, y - 1), y + 2 if y + 2 < self.columns else self.columns):
                number_of_neighbors += self.image_matrix[i][j]
        return number_of_neighbors

    def create_minimal_hint_matrix(self):
        minimal_hint_matrix = numpy.empty([self.rows, self.columns], str)

        for i in range(self.rows):
            for j in range(self.columns):
                if self.hint_matrix[i][j] == 0:
                    minimal_hint_matrix[i][j] = ' '
                else:
                    minimal_hint_matrix[i][j] = self.hint_matrix[i][j]

        return minimal_hint_matrix

    def print_minimal_hint_matrix(self):
        for i in range(self.rows):
            new_map = map(str, self.minimal_hint_matrix[i])
            print(" ".join(new_map))

    def make_a_guess(self, row_index, column_index):
        if self.image_matrix[row_index][column_index] == 1:
            return True
        else:
            return False

    def delete_hints_around_9(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.minimal_hint_matrix[i][j] == '9':
                    for m in range(-1, 2):
                        for n in range(-1, 2):
                            if (i + m, j + n) != (i, j) and (0 <= i + m < self.rows and 0 <= j + n < self.columns):
                                self.minimal_hint_matrix[i + m][j + n] = ' '


if __name__ == '__main__':
    print("Fill-a-pix by Michał Dunat")
    rows = int(input("Input desired number of rows: "))
    columns = int(input("Input desired number of columns: "))
    image_name = input("Input file name: ")
    game = Game(rows, columns, image_name)
    # game = Game(40, 40, "tree_icon.png")
    print("Image matrix:")
    print(numpy.matrix(game.image_matrix))
    print("Matrix with all hints:")
    print(numpy.matrix(game.hint_matrix))
    print("Puzzle with all hints:")
    game.print_minimal_hint_matrix()
    print("Puzzle without all hints: ")
    game.delete_hints_around_9()
    game.print_minimal_hint_matrix()
    while True:
        print("Try to point a square that should be painted!")
        row_index = int(input("Row index: "))
        column_index = int(input("Column index: "))
        if game.make_a_guess(row_index, column_index):
            print("Good! This square should be painted!")
        else:
            print("Miss :( Try again!")
