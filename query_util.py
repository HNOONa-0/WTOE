
Q='lang:en';
def or_query(arr):
    q='(';
    q+=(arr[0] );
    for i in range(1,len(arr) ):
        q+=' '+'OR'+' '+arr[i];
        # cant save space here
        # q+='OR'+arr[i];
    q+=')';
    return q;
def main():
    print('hello');
if __name__ == "__main__":
    main()