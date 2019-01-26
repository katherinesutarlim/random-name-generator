import random
import tkinter

# Loads files containing letters and letter combinations to be used to compose
# names. Each letter/combination are place on separate lines, and the first line
# of each file specifies the number of lines to be readself.
# Parameter: file_name - name of the files
# Returns: list - a list containing the letters or letter combinations from the
#                 file.
def load_file(file_name):
    list = []
    with open(file_name,"r") as f:
        num_lines = f.readline()
        for i in range(0,int(num_lines)):
            list.append(f.readline().strip())
    return list

# Appends a letter/combination from the vowel list to the list of selected
# letter/combination, then choose which list to append from next or stop appending
# Parameter: list - list containing selected letter/combination that will be
#                   appended to
# Returns: none
def add_vowel(list):
    rand_num = int(random.random()*len(vowel))
    list.append(vowel[rand_num])
    prob_end_cons = random.random()*0.7**len(list)
    prob_start_cons = random.random()*0.7**len(list)
    prob_end_set = random.random()*len(list)*len(list)/7
    prob_end = random.random()*((len(list)*len(list)/7)-1)
    if ((prob_end_cons>prob_start_cons)
        and (prob_end_cons>prob_end_set)
        and (prob_end_cons>prob_end)):
        add_end_cons(list)
    elif ((prob_start_cons>prob_end_cons)
        and (prob_start_cons>prob_end_set)
        and (prob_start_cons>prob_end)):
        add_start_cons(list)
    elif ((prob_end_set>prob_end_cons)
        and (prob_end_set>prob_start_cons)
        and (prob_end_set>prob_end)):
        add_end_set(list)

# Appends a letter/combination from the start_consonant list to the list of selected
# letter/combination, then continue with appending vowel.
# Parameter: list - list containing selected letter/combination that will be
#                   appended to
# Returns: none
def add_start_cons(list):
    rand_num = int(random.random()*len(start_consonant))
    list.append(start_consonant[rand_num])
    add_vowel(list);

# Appends a letter/combination from the end_consonant list to the list of selected
# letter/combination, then appends either another consonant or vowel or stops
# the "append chain".
# Parameter: list - list containing selected letter/combination that will be
#                   appended to
# Returns: none
def add_end_cons(list):
    rand_num = int(random.random()*len(end_consonant))
    list.append(end_consonant[rand_num])
    prob_vowel = random.random()*0.7**len(list)
    prob_start_cons = random.random()*0.7**len(list)
    prob_end = random.random()*len(list)*len(list)/7
    if (prob_vowel>prob_start_cons) and (prob_vowel>prob_end):
        add_vowel(list)
    elif (prob_start_cons>prob_end) and (prob_start_cons>prob_end):
        add_start_cons(list)

# Appends a letter/combination from the end_set list to the list of selected
# letter/combination.
# Parameter: list - list containing selected letter/combination that will be
#                   appended to
# Returns: none
def add_end_set(list):
    rand_num = int(random.random()*len(end_set))
    list.append(end_set[rand_num])

vowel = load_file("vowel")
start_consonant = load_file("start-consonant")
end_consonant = load_file("end-consonant")
end_set = load_file("end-set")

# Randomly generates name.
# Parameter: none
# Returns: the randomly generated name as a string
def generate_name():
    name_list = []

    prob_vowel = random.random()
    prob_start_cons = random.random()
    if (prob_vowel>prob_start_cons):
        add_vowel(name_list)
    else:
        add_start_cons(name_list)

    return "".join(name_list).capitalize()

# Setting up GUI
app = tkinter.Tk()
app.geometry("300x200")
app.title("Random Name Generator")

# Displaying the output
generated_name = tkinter.StringVar()
generated_name.set(generate_name())

label_name = tkinter.Label(app, textvariable = generated_name)
label_name.pack()
label_name.place(anchor = "center", x = 150, y = 80)

# When button is clicked, generate a new name and change the label.
# Parameter: none
# Returns: none
def button_clicked():
    generated_name.set(generate_name())
    label_name.pack()
    label_name.place(anchor = "center", x = 150, y = 80)

# Setting up button
button_generate = tkinter.Button(app, text = "Generate Name", command = button_clicked, cursor = "hand2")
button_generate.place(anchor = "center", x = 150, y= 120)

app.mainloop()
