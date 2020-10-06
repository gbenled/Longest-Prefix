"""
created by Damilola Gbenle
"""

def match(prefixes, numbers):
    # Write your code here
    #create another list of phone numbers to be replaced with the prefix if they match 
    new_phone = []
    new_phone = new_phone + numbers
    #sort the prefix number in descending order so it always pic the longest
    prefixes1 = sorted(prefixes, key=len)
    for number in range(len(new_phone)):
        for prefix in range(len(prefixes)):
            #check if the prefix is in the number
            if prefixes1[prefix] == numbers[number][:len(prefixes1[prefix])]:
                #once they match i replace the number with the prefix in my new phone list
                new_phone[number] = prefixes1[prefix]
    #to replace phone number with no prefix that match with an empty space
        #if the number in both lists match it means no prefix was found
        for index1, number1 in enumerate(new_phone):
            for index2, number2 in enumerate(numbers):
                if number1==number2:
            #replace with empty space
                    new_phone[index1] = " "
    return new_phone
