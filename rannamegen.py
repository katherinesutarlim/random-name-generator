import random

def load_file(file_name):
    list = []
    with open(file_name,"r") as f:
        num_lines = f.readline()
        for i in range(0,int(num_lines)):
            list.append(f.readline().strip())
    return list

def add_vowel(list):
    rand_num = int(random.random()*len(vowel))
    list.append(vowel[rand_num])
    prob_end_cons = random.random()*0.7**len(list)
    prob_start_cons = random.random()*0.7**len(list)
    prob_end_set = random.random()*len(list)*len(list)/7
    prob_end = random.random()*((len(list)*len(list)/7)-1)
    if (prob_end_cons>prob_start_cons) and (prob_end_cons>prob_end_set):
        add_end_cons(list)
    elif (prob_start_cons>prob_end_cons) and (prob_start_cons>prob_end_set):
        add_start_cons(list)
    else:
        add_end_set(list)

def add_start_cons(list):
    rand_num = int(random.random()*len(start_consonant))
    list.append(start_consonant[rand_num])
    add_vowel(list);

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

def add_end_set(list):
    rand_num = int(random.random()*len(end_set))
    list.append(end_set[rand_num])


vowel = load_file("vowel")
start_consonant = load_file("start-consonant")
end_consonant = load_file("end-consonant")
end_set = load_file("end-set")

name_list = []

prob_vowel = random.random()
prob_start_cons = random.random()
if (prob_vowel>prob_start_cons):
    add_vowel(name_list)
else:
    add_start_cons(name_list)

print("".join(name_list).capitalize())
