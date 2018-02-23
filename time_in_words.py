#!/bin/python3

import sys

numtowords = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 
    16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty'
}

quarters = ["%s o' clock", "quarter past %s", "half past %s", "quarter to %s"]
formats = ['%s %s past %s', '%s %s to %s']


def timeInWords(h, m):
    past_or_to = m>30  # greater than 30 is 'to', less is 'to'
    h += past_or_to    # if greater than 30, plus one hour to current value
    
    if m%15==0:  # only quarters, half past and o'clock
        return quarters[m//15] % numtowords[h]
    else:
        mf30 = min(m, 60-m)  # converting to time format 16->16, 32->28, 58->2
        minute_f = 'minute'+'s'*(mf30>1) # adds 's' to 'minute' when minute_count more than one
        if mf30<=20:
            return formats[past_or_to] % (numtowords[mf30], minute_f, numtowords[h])
        else:
            total_min = 'twenty ' + numtowords[mf30%10]
            return formats[past_or_to] % (total_min, minute_f, numtowords[h])
    return res
    

if __name__ == "__main__":
    h = int(input().strip())
    m = int(input().strip())
    result = timeInWords(h, m)
    print(result)
