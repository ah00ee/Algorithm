import os

def count_files():
    cnt = []
    for folder in os.listdir("./"):
        if os.path.isdir(folder) and folder[-4:].isdigit():
            cnt.append((folder, len(os.listdir(folder))))
    return cnt
    
def update_readme():
    results = count_files()
    with open("./README.md", "w+") as f:
        for folder, cnt in results:
            f.write(f"{folder}\t{cnt}\n")

if __name__ == "__main__":
    update_readme()