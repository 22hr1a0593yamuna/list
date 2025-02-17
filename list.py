# list
Write a program to create a list and display it. 
Input format:
Input consist of n+1 integers
First integer corresponds to the size of the list
Next n inputs corresponds to the elements in the list 
Output format: 
Output is an integer list
Sample Input
4 
1
2
3
4
Output
[1, 2, 3, 4]
def create_and_display_list():
    size = int(input())
    number_list = []
    for _ in range(size):
        number = int(input())
        number_list.append(number)
    print(number_list)
create_and_display_list()
2)Write a program to create a list and display it. 
Input format:
Input consist of n+1 integers
First integer corresponds to the size of the list
Next n inputs corresponds to the elements in the list 
Output format: 
Output is an integer list
Sample Input
4 
1
2
3
4
Output
1 2 3 4
def create_and_display_list():
    size = int(input())
    number_list = []
    for _ in range(size):
        number = int(input())
        number_list.append(number)
    print(" ".join(map(str, number_list)))
create_and_display_list()
3)Write a Python Program to find the largest number in a list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the size of the list.
Output consists of the largest element.
Sample Input:
5
1
2
3
6
5
Sample Output:
6
def find_largest_number():
    size = int(input())
    number_list = []
    for _ in range(size):
        number = int(input())
        number_list.append(number)
    largest_number = max(number_list)
    print(largest_number)
find_largest_number()


4)Write a Python Program to put the even and odd elements in a list into two different lists.
Input format:
Input consists of one integer and one list.
First input consists of the size of the list.
Second input consists of the elements based on the size.
Output format:
Output consists of two lists.
First list consists of all the even numbers in the list.
Second list consists of all the odd numbers in the list.
Sample Input:
5
1
2
3
6
5
Sample Output:
The even list [2, 6]
The odd list [1, 3, 5]
def separate_even_odd():
    size = int(input())
    even_list = []
    odd_list = []
    for _ in range(size):
        number = int(input())
        if number % 2 == 0:
            even_list.append(number)  
        else:
            odd_list.append(number)
    print("The even list", even_list)
    print("The odd list", odd_list)
separate_even_odd()
5)Write a program to find the sum of the elements in the array. 
Input Format: 
Input consists of n+1 integers where n corresponds to the number of elements in the array.
The first integer corresponds to n and the next n integers correspond to the elements in the array.
Assume that the maximum number of elements in the array is 20. 
Output Format: 
Output consists of a double value which corresponds to the mean of the array.
Refer sample input and output for formatting specifications.
Sample Input: 
5
2
4
1
3
1
Sample Output:
11
def sum_of_elements():
    n = int(input())
    total_sum = 0
    for _ in range(n):
        number = int(input())
        total_sum += number
    print(total_sum)
sum_of_elements()
6)Write a Python Program to find the smallest number in a list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the size of the list.
Output consists of the largest element.
Sample Input:
5
1
2
3
6
5
Sample Output:
1
def find_smallest_number():
    size = int(input())
    number_list = []
    for _ in range(size):
        number = int(input())
        number_list.append(number)
    smallest_number = min(number_list)
    print(smallest_number)
find_smallest_number()

7)Write a Program to find the search element in the given list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the elements of list in single line separated by space.
Third input consists of the element which we need to search
Sample Input 1:
5
1 2 3 6 5
3
Sample Output 1:
3 is present in the given list
Sample Input 2:
5
1 2 3 6 5
4
Sample Output 2:
4 is not present in the given list

def search_in_list():
    size = int(input())
    number_list = list(map(int, input().split()))
    search_element = int(input())
    if search_element in number_list:
        print(f"{search_element} is present in the given list")
    else:
        print(f"{search_element} is not present in the given list")
search_in_list()

8)Write a program to count the number of times the given value is repeated.
Input Format:
First line of input consists of our list elements.
Second line of input consists of value to count.
Output Format:
Print thr number of times the given value is repeated in the list.
Sample Input:
10 20 10 40 10
10
Sample Output:
3

def count_occurrences():
    number_list = list(map(int, input().split()))
    value_to_count = int(input())
    count = number_list.count(value_to_count)
    print(count)
count_occurrences()

9)Write a program to print the given list in reverse order.
Sample Input:
10 20 30 40 50
Sample Output:
50 40 30 20 10 
10)Write a program to sort the given list and print it.
Sample Input:
30 20 10 50 40
Sample Output:
10 20 30 40 50 

def print_reverse():
    number_list = list(map(int, input().split()))
    print(" ".join(map(str, reversed(number_list))))
print_reverse()





