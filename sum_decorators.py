def decor_func(result_students):
    def distinction(marks):
        for m in marks:
            if m >=75:
                print("distinction")
        result_students(marks)
    return distinction   
    
@decor_func
def result(marks):
    for m in marks:
        if m>33:
            pass
        else:
            print("Fail")
            break        
    else:
        print("pass")
result([45,67,89,75,43])        
            
def smart_div(div):
    def inner(a,b):
        if a<b:
            a,b = b,a
            print("hello python")
        div(2,4)
    return inner            
        
@smart_div           
def div (a,b):
    result = a/b   
    return result
print (div(2,4))                
