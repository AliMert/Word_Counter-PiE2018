import argparse
import re

def count_lines(data=""):
    lines = data.split("\n")

    for real_lines in lines:
        if not real_lines: # if line is empty("\n"), remove that line
            lines.remove(real_lines)
    # print("The lines in the text are:")
    # print(lines)
    print("The number of lines is: " + str(len(lines)))
    return len(lines)



def count_words(data=""):

    words = re.sub("[^A-Za-z0-9\']+", " ", data)
    #words = re.sub('\W+', ' ', data)
    words = words.split(" ")

    if words[0] == " " or words[0] == "":
        words.pop(0)
    elif words[-1] == " " or words[-1] == "":
            words.pop()
    # print("The words in the text are:")
    # print(words)
    print("The number of words is:" + str(len(words)))
    return len(words)



def count_chars(data=""):
    # print("The characters in the text are:")
    # print(data)
    print("The number of total characters is: " + str(len(data)))
    return len(data)


"""
def get_words2(data=""):
    lines = data.replace("\n"," ")
    words = lines.split(" ")

    # can't use 'for loop' because python does not allow to decrement/increment/change loop variable
    '''
    for real_word in words:
        if "." in real_word:
            index = words.index(real_word)
            real_word = real_word.replace(".", "")
            words[index] = real_word

        if  real_word == " " or  real_word == "":
            index = words.index(real_word) - 1
            words.remove(real_word)
            real_word = words[index] # python does not allows this in for loop
    '''

    i = 0
    while i < len(words):
        if "." in words[i]:
            words[i] = words[i].replace(".", "")

        if words[i] == " " or words[i] == "":
            words.remove(words[i])
            i -= 1
        # print("hi")
        i += 1

    # print("The words in the text are:")
    # print(words)
    print("The number of words is: " + len(words))
    return len(words)
"""



def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-wc", "--wordCounter", help="counts words of a given text file", type=argparse.FileType('r'))
    parser.add_argument("-lc", "--lineCounter", help="counts lines of a given text file", type=argparse.FileType('r'))
    parser.add_argument("-cc", "--charCounter", help="counts characters of a given text file", type=argparse.FileType('r'))

    try:
        args = parser.parse_args()

        if args.wordCounter:
            with args.wordCounter as file:
                data = str(file.read())
                count_words(data)
        elif args.lineCounter:
            with args.lineCounter as file:
                data = str(file.read())
                count_lines(data)
        elif args.charCounter:
            with args.charCounter as file:
                data = str(file.read())
                count_chars(data)

        else:
            print("Please press try again or type '-h' to get help.")

    except SystemExit:
        print("Please press try again or type '-h' to get help.")



if __name__ == '__main__':
  main()
