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
        
word_count()