import re

#takes in a string and does the same thing as the strip() string method
def regexStrip(x, str):
    if x == '':
        leftRegex = re.compile(r'^\s+')
        rightRegex = re.compile(r'\s+$')
        front = leftRegex.sub('', str)  #removes space from front of string
        back = rightRegex.sub('', front)  #removes space from back of new string
        print(back) #prints string with spaces removed from front and back
    else:
        leftRegex = re.compile(r'^[' + x + ']+', re.DOTALL)
        rightRegex = re.compile(r'[' + x + ']+$', re.DOTALL)
        front = leftRegex.sub('', str)  #removes x from front of string
        back = rightRegex.sub('', front)  #removes x from back of new string
        print(back) #prints string with x removed from front and back

regexStrip('', '   Hello World!     ')
regexStrip('abc', 'abcabcHelloabcWorldabcabc')
regexStrip('cab', 'abcabcHelloabcWorldabcabc')
