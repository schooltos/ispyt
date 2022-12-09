def word_count(text):
    wrd_cnt = 0
    line_count = 0
    for line in text:
        line_count += 1
        words_in_line = line.split(" ")
        wrd_cnt = len(words_in_line)
        print(f"There are {wrd_cnt} words in {line_count} paragraph")

def letter_count(text):
    lttr_cnt = 0
    line_count = 0
    for line in text:
        line_count += 1
        lttr_cnt = len(line)
        print(f"There are {lttr_cnt} letters in {line_count} paragraph")

with open("file.txt", "r") as fl:
    file_txt = fl.readlines()

word_count(file_txt)
letter_count(file_txt)


