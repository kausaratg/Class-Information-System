from django.shortcuts import render
import string

# Create your views here.

def class_group(request):
    if request.method == "POST":
        name = request.POST['name']
        split_name = name.split()
        last_name = split_name[0].lower()
        splited_letters = []
        for x in last_name:
            splited_letters.append(x)
        first_letter = splited_letters[0]
        second_letter = splited_letters[1]
        result = ""
        alpha1 = "a"
        test_list = []
        for i in range(0, 26):
            test_list.append(alpha1)
            alpha1 = chr(ord(alpha1) + 1)
        if first_letter in test_list[:1]:
            result = "You are in group A"
        elif first_letter in test_list[2:11]:
            result = "You are in group C"
        elif first_letter in test_list[11:14]:
            result = "You are in group B"
        elif first_letter in test_list[14]:
            if second_letter in test_list[0:11]:
                result = "You are in group C"
            if second_letter in test_list[11:26]:
                result = "You are in group D"
        elif first_letter in test_list[15:26]:
            result = "You are in group D"
        return render(request, "group/group.html", {"result": result})
    return render(request, "group/group.html")
