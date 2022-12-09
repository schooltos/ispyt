with open("file.txt", "r") as fl:
    file_txt = fl.readlines()

def word_count():
    wrd_cnt = 0
    line_count = 0
    for line in file_txt:
        line_count += 1
        f = line.split(" ")
        wrd_cnt = wrd_cnt + len(f)
        print(f"There is {wrd_cnt} words in {line_count} paragraph")

def letter_count():
    lttr_cnt = 0
    line_count = 0
    for line in file_txt:
        line_count += 1
        lttr_cnt = len(line)
        print(f"There is {lttr_cnt} letters in {line_count} paragraph")

word_count()
letter_count()
