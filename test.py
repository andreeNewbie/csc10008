def getName(selected_file_path):
    index = 0
    cnt = len(selected_file_path) - 1
    file_name = ""
    while cnt >= 0:
        if selected_file_path[cnt] == "/":
            index = cnt + 1
            break
        cnt -= 1

    while index < len(selected_file_path):
        file_name += selected_file_path[index]
        index += 1
    return file_name


if __name__ == "__main__":
    print(getName("C:/Users/DELL/Desktop/note_MMT/temp3/requirements.txt"))
