# Q2. How can a given string be reversed using recursion?  -- 
def reverse_string(str_a: str):
    if len(str_a) == 0:
        return str_a
    else:
        return reverse_string(str_a[1:]) + str_a[0]

str_a = "himanshu garg"
rever_a = reverse_string(str_a)
print(rever_a)


# Q3. Program to find sum of digits of an array of numbers using recursion.  --
def sum_of_digits_array(number):
    if number <= 9:
        return number
    else: 
        return number%10 + sum_of_digits_array(number//10) # 120 % 10 = 0 | 120 // 10 = 12

number = 12346
print(sum_of_digits_array(number))
