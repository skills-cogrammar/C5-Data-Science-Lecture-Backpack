# Hi! Really struggling with the logic of creating different star patterns on python. 
# Any way we could go through some different, maybe even some complex ones (such as hollow ones) 
# together and get it explained like to a 3 year old please? :)

"""
    **
   ****
  ******
 ***  ***
***    ***
 ***  ***
  ******
   ****
    **

"""

pattern = ""
count_up = 4
hole = ""

for num in range(9):
    
    if num <= 4:
        spaces = " " * (count_up - num)

        if num < 3:
            pattern += "*"
        
        else:
            hole += "  "
    
    else:
        spaces = " " * (num - count_up)

        if num == 5:
            hole = "  "
        
        else:
            hole = ""

        if num >= 7:
            pattern = "*" * ( 9 - num )

    print(f"{spaces}{pattern}{hole}{pattern}")


# I am struggling with making a for loop that goes up in number and then reverses after it reaches a certain number. 
# Please can you give some examples of how to do this?

count_up = 5

for num in range(1, 10):

    if num > count_up:
        print((count_up * 2) - num)

    else:
        print(num)


#I figured out how to capitalise alternate characters but I'm struggling with alternating capital words with lowercase words. 
# Would you be able to help with some examples? My logic at the end is flawed!
        
test_sent = "Quick brown fox never jumped"

new_sent = ""

for num in range(len(test_sent)):

    if(num % 2 == 0):
        new_sent += test_sent[num].lower() + " "

    else:
        new_sent += test_sent[num].upper() + " "


print(new_sent)