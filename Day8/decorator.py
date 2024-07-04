# def div(a,b):
#     return print(a/b)
#
#
# def smart_div(func):
#     def innner(a,b):
#         if a<b:
#             a,b = b,a
#         return func(a,b)
#     return innner
#
# div = smart_div(div)
#
# div(2,4)

# another way

def smart_div(func):
    def innner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return innner

@smart_div
def div(a,b):
    return print(a/b)


div(2,10)