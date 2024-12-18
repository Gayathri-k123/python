import csv

def read_csv_file(filename):
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)  # Each row is printed as a list of strings

# Example usage
csv_filename = "exam.csv"
read_csv_file(csv_filename)
