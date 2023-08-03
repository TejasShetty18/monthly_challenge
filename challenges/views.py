from django.shortcuts import render
from django.http import Http404 , HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
# def january(request):
#     return HttpResponse("do not eat meat for a month")

# def february(request):
#     return HttpResponse("do not play game for a month")

# def march(request):
#     return HttpResponse("do not eat meat for a month")

# def april(request):
#     return HttpResponse("do not eat meat for a month")

# def may(request):
#     return HttpResponse("do not eat meat for a month")

# def june(request):
#     return HttpResponse("do not eat meat for a month")

# def july(request):
#     return HttpResponse("do not eat meat for a month")

# def august(request):
#     return HttpResponse("do not eat meat for a month")

# def september(request):
#     return HttpResponse("do not eat meat for a month")

# def october(request):
#     return HttpResponse("do not eat meat for a month")

# def november(request):
#     return HttpResponse("do not eat meat for a month")

# def december(request):
#     return HttpResponse("do not eat meat for a month")

monthly_challenge_text = {
    "January": """ * Write a program that prints the numbers from 1 to 100.
                        * For multiples of 3, print "Fizz" instead of the number.
                        * For multiples of 5, print "Buzz" instead of the number.
                        * For numbers that are multiples of both 3 and 5, print 'FizzBuzz' """,
    "February": """ * Write a program that checks if a given string is a palindrome (reads the same backward as forward).
                                       * Ignore spaces, punctuation, and capitalization while checking.""",
    "March": """ * Write a function to generate the Fibonacci sequence up to a given number 'n'.
                                    * Implement the function using both iterative and recursive approaches. """,
    "April": """ * Create a program that generates prime numbers up to a specified limit 'n'.
                                        * Implement the Sieve of Eratosthenes algorithm for efficiency. """,
    "May" : """ * Write a program that takes a text file as input and counts the frequency of each word.
                                       * Ignore punctuation and capitalization while counting words """,
    "June":""" * Implement the binary search algorithm to find a target element in a sorted array.
                             * Compare its efficiency with linear search for large datasets. """,
    "July": """ * Implement three sorting algorithms: Bubble Sort, Merge Sort, and Quick Sort.
                                   * Compare their time complexities and performance with different input sizes. """,
    "August": """ * Create a basic singly linked list and implement common operations: insertion, deletion, and traversal. """,
    "September": """ * Implement a stack and a queue using arrays or linked lists.
                                      * Demonstrate their usage with some real-world examples. """,
    "October": """ * Implement a binary tree data structure and its traversal methods (Inorder, Preorder, Postorder). """,
    "November": """ * Implement Depth-First Search (DFS) and Breadth-First Search (BFS) algorithms on a graph. """,
    "December": """ * Solve a classic dynamic programming problem, like finding the longest common subsequence or the minimum edit distance between two strings"""
}

def index(request):
    #list_item = ""
    months = list(monthly_challenge_text.keys())

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenges", args = [month])
    #     list_item += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    #     # "<li><a href="....">january</a></li>""<li><a href="....">februry</a></li>"

    # response_data = f"<ul>{list_item}</ul>"
    # return HttpResponse(response_data)  OR

    return render(request,"challenges/index.html",{
        "months" : months
    })



def monthly_challenges_by_number(request,month):
    months = list(monthly_challenge_text.keys())

    if month > len(months):
        #return HttpResponseNotFound("invalid month")or
        response_data =render_to_string("404.html")
        return HttpResponseNotFound(response_data)
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenges",args=[redirect_month])  #/challenges/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenges(request , month):
    try:
        challenge_text = monthly_challenge_text[month]
        month_name = month
        #response_data = f"<h1>{challenge_text}</h1>"  or
       # response_data = render_to_string("challenges/challenge.html")
        #return HttpResponse(response_data) or
        return render(request,"challenges/challenge.html", { "name": month_name,
            "text":challenge_text
        })
        
    except:
        # response_data =render_to_string("404.html")
        # return HttpResponseNotFound(response_data) or
        raise Http404()
   