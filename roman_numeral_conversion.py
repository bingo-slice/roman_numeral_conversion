def roman_numerals(arg):
    """a function which will turn a string of roman numerals, to integer and v.v."""
    
    roman_to_int = {'M': 1000, 'CM': 900, 'D': 500, 'C': 100, 'XC': 90, 'L': 50,
              'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    int_to_roman = dict(map(reversed, roman_to_int.items()))
    

    #roman -> int conversion function:
    if type(arg) == str:
        result = 0
        for key, letter in enumerate(arg):
            if key != len(arg)-1 \
               and roman_to_int[letter] < roman_to_int[arg[key+1]]:
                # if the letter to the right is higher value, then this letter
                # is subtracted (e.g. IV = 5 - 1 = 4). Otherwise it is added
                result -= roman_to_int[letter]
            else:
                result += roman_to_int[letter]
        return result
    else:
        #int -> roman conversion
        result = ''
        while arg > 0:
            #Look in the dictionary for the highest valued symbol which is
            #not greater than the required sum, and add it to the string.
            #Then reduce the target sum by that amount and repeat until
            #the target sum is zero.
            next_subtract = max([i for i in int_to_roman.keys() if i <= arg])
            result += int_to_roman[next_subtract]
            arg -= next_subtract
        return result
            
    
    
