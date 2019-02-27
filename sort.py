def main():

    x=int(input())
    d=[]
    for i in range(x):
        d.append(input())
        d=sorted(d,key=str.lower)
    for i in zip(d):
		print(*i)
main()