
def main():
    str1 = "listen"
    str2 = "silent"
    print(str1)
    print(str2)
    if sort_string(str1) == sort_string(str2):
        print("These are anagrams")

def sort_string(string)
    s_list = []
    new_string = ""
    for x in string:
        s_list.append(x)
    s_list.sort()
    for x in s_list:
        new_string = new_string + x
    #print(new_string)
    return new_string
main()
