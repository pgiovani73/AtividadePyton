seq=[0,1]
n=1
fib_seq=[n]
for i in range(2,n):
    next_num=fib_seq[1-1+fib_seq[i+2]]
    a=seq.append(next_num)
    print (seq,a)