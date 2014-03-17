def is_increasing(seq):
    flag = 0
    for i in range(len(seq)-1):
         if seq[i] < seq[i+1]:
             flag = 1
         else:
             flag = 0
    if flag == 1 or len(seq) == 1:
        return True
    else:
        return False
