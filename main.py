
# Natural Language Toolkit
import nltk

# use of a Data Set from UCI --> SMS Spam Collection Data Set
# Data set with messages label as Spam of Ham (good ones)

def main():
    print('Hello World')

    #open the file of the Messages
    f = open('SMSSpamCollection')
    # we get the messages into a variable
    messages = [line.rstrip() for line in f]
    print(len(messages))



if __name__ == "__main__":
    main()