from abc import ABC, abstractmethod

class FileHandler(ABC):

    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

    def __add__(self, other):
        try:
            data1 = self.read()
            data2 = other.read()

            combined_name = "combined_" + self.filename
            new_file = TextFile(combined_name)

            new_file.write(data1 + "\n" + data2)
            print(f"\nFiles combined into: {combined_name}")
            return new_file

        except Exception as e:
            print("Error while combining files:", e)

class TextFile(FileHandler):

    def read(self):
        try:
            with open(self.filename, "r") as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"{self.filename} does not exist.")

    def write(self, data):
        try:
            with open(self.filename, "w") as f:
                f.write(data)
            print(f"Data written to {self.filename}")
        except Exception as e:
            print("Write error:", e)

class CSVFile(FileHandler):

    def read(self):
        try:
            with open(self.filename, "r") as f:
                lines = f.readlines()
                return "".join(lines)
        except FileNotFoundError:
            raise FileNotFoundError(f"{self.filename} does not exist.")

    def write(self, data):
        try:
            with open(self.filename, "w") as f:
                f.write(data)
            print(f"CSV data written to {self.filename}")
        except Exception as e:
            print("CSV Write error:", e)


try:
    file1 = TextFile("file1.txt")
    file2 = TextFile("file2.txt")

    file1.write("Hello, this is File 1.")
    file2.write("Welcome! This is File 2.")


    print("\nReading File 1:")
    print(file1.read())

    print("\nReading File 2:")
    print(file2.read())

    combined = file1 + file2

    print("\nReading Combined File:")
    print(combined.read())

except Exception as e:
    print("System Error:", e)
