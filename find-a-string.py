def count_substring(string, sub_string):
    l1 = len(sub_string)
    l2 = len(string)
    out_counter = 0
    for k in range(l2):
        i=k
        l = i+l1
        if (k == l2-l1+1):
            break
        elif (string[i:l] == sub_string):
            out_counter+=1
        else:
            continue
    return out_counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
