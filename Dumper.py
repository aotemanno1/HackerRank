import xlrd
import matplotlib.pyplot as plt


global_app_names = ["Hub", "Calendar", "Contacts", "Tasks", "Notes"]

directory = input("Enter Excel file location here if file isn't in same directory as this .py file, otherwise press enter: ")
if len(directory) > 0:
    directory += "\\"
filename = input("Copy Excel file name here: ")
if filename[-5:] != ".xlsx":
    filename += ".xlsx"

workbook = xlrd.open_workbook(directory + filename)
sheet = workbook.sheet_by_index(0)

ratings_congregate = []
for x in range(0, 5):
    ratings_congregate.append([0]*12)


class MyApp:
    def __init__(self):
        app_name = input("Which app's data would you like? ")
        self.name = app_name.capitalize()
        self.index = global_app_names.index(self.name)
        self.ratings = [0] * 12
        self.satisfaction_percent = -1
        self.total = -1
        self.comments = []
        self.satisfied = -1
        self.unsatisfied = -1
        self.no_response = -1

        self.get_ratings()
        self.get_total()
        # Will also fetch no_response
        self.get_satisfaction_percent()
        # Will also fetch number of satisfied and number of unsatisfied
        self.get_comments()

    def get_ratings(self):
        for row_num in range(1, sheet.nrows):
            try:
                self.ratings[int(sheet.cell(row_num, self.index * 2 + 3).value)] += 1
            except ValueError:
                self.ratings[11] += 1

    def get_total(self):
        self.no_response = self.ratings[11]
        self.total = sum(self.ratings) - self.ratings[11]

    def get_satisfaction_percent(self):
        self.satisfied = self.ratings[8]+self.ratings[9]+self.ratings[10]
        self.unsatisfied = self.total - self.satisfied - self.no_response
        self.satisfaction_percent = 100*float(self.satisfied)/self.total

    def get_comments(self):
        for row_num in range(1, sheet.nrows):
            try:
                if len(sheet.cell(row_num, self.index * 2 + 4).value) > 0:
                    self.comments.append((sheet.cell(row_num, 0).value, sheet.cell(row_num, self.index * 2 + 4).value))
            except ValueError:
                pass

    def generate_bar(self):
        left = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        height = self.ratings

        tick_label = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "NA"]

        plt.bar(left, height, tick_label=tick_label, width=0.75, color=(0.117647059, 0.564705882, 1))
        plt.xlabel('Score given by participants')
        plt.ylabel('Quantity of participants for each score')
        plt.title(self.name + " Responses Bar Graph")
        for v in range(0, 12):
            plt.text(v, height[v]+0.5, str(height[v]), color='black', ha='center', fontweight='bold')
        plt.show()

    def generate_pie(self):
        plt.pie([self.satisfied, self.unsatisfied, self.no_response],
                labels=[self.satisfied, self.unsatisfied, self.no_response],
                colors=[(1, 0.843137255, 0), (1, 0.270588235, 0), (0.541176471, 0.0274509804, 0.0274509804)],
                startangle=90, shadow=True, radius=1.1)
        plt.legend(["Satisfied", "Unsatisfied", "No response"])
        plt.show()


while True:
    myapp = MyApp()

    with open(directory + "CommentDump " + filename + " " + myapp.name + ".txt", "w") as file:
        for x in range(0, len(myapp.comments)):
            try:
                file.write(myapp.comments[x][1].strip("\n") + "\n")
            except AttributeError:
                file.write(myapp.comments[x][0] + "ATTRIBUTE ERROR" "\n")
            except UnicodeEncodeError:
                file.write(myapp.comments[x][0] + "UNICODE ERROR" "\n")

    print("Comments dumped at a textfile in the same directory as Excel File")

    myapp.generate_pie()
    myapp.generate_bar()

    if input("Break? y/n ").lower() == 'y':
        break
