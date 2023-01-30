def function(string):
    new_string = ""
    length = len(string)
    for i in range (length):
        if i==0 or i==length-1:
            s = string[i].capitalize()
            new_string += s
        else :
            new_string += string[i]


    return(new_string)




input = "iqbal"
print("input =", input)
output = function(input)
print("output = ", output)