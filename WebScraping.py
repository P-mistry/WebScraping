from bs4 import BeautifulSoup
from textblob import TextBlob

from termcolor import colored

html_file = open('index.html', 'r')
page = html_file.read()


soup = BeautifulSoup(page, 'html.parser')

reviews = soup.find_all('p')

print("Here the seller reviews...\n")

positiveCount, negativeCount = 0, 0

for p in reviews:
    text = p.get_text()
    sentiment = TextBlob(text).sentiment.polarity
    sentimentStr = " "

    if len(text) == 0:
        pass
    else:
        if sentiment >= 0.1:
            sentimentStr = colored("+", "green")
            positiveCount += 1

        else:
            sentimentStr = colored("-", "red")
            negativeCount += 1

        print(sentimentStr, p.get_text())


print("\nTotal positive reviews: ", colored(positiveCount, "green"))
print("Total negative reviews: ", colored(negativeCount, "red"))