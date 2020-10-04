start_value=0
second_value=1
def fibonacci(end_value,start_value,second_value):
    print(start_value)
    print(second_value)
    for x in range(end_value):
        value=start_value+second_value
        start_value=second_value
        second_value=value
        print(value)

end_value=int(input("Enter the end value:"))
last_value=fibonacci(end_value,start_value,second_value)

