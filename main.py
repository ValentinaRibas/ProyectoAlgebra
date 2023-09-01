import numpy as np
import pandas as pd

tweet1="Excelente en su área, su muerte es una enorme pérdida y debería ser luto nacional!!!"
tweet2="Vaya señora que bueno que se asesora por alguien inteligente luto."
tweet3="Se me ocurre y sin ir a clase me informéis por dónde empiezo. Entiendo que os tendría que decir quién soy y que quiero, vamos conocerme para asesorarme bien. Un saludo"
tweet4="Soy docente universitario, estoy intentando preparar mis clases en modo bien didáctico,(le llamo modo noticiero), descargue una plataforma gratuita de grabación y transmisión de vídeo, se llama Obs estudio! bueno la sigo remando con sus funciones pero sé que saldrá algo!"

positive_words = ["excelente",
                  "gran",
                  "positivo"]

neutro_words = ["pérdida"]

negative_words = ["muerte",
                  "luto"]

words = ["excelente",
        "gran",
        "positivo",
        "pérdida",
        "muerte",
        "luto"]


def count_words_in_tweet(tweet):
    words_count = np.array([0]*len(words))
    tweet_array = tweet.replace("!","").replace(",","").replace(".","").replace("(","").replace(")","").split()
    
    for tweet_word in tweet_array:
        i = 0
        while i < len(words):
            if tweet_word.lower() == words[i]:
                words_count[i] += 1
            i += 1
    return words_count

def count_group_of_words(tweet):
    group_of_words_count = np.array([0]*3)
    tweet_array = tweet.replace("!","").replace(",","").replace(".","").replace("(","").replace(")","").split()
    
    for tweet_word in tweet_array:
        for word in positive_words:
            if tweet_word.lower() == word:
                group_of_words_count[0] += 1
        for word in neutro_words:
            if tweet_word.lower() == word:
                group_of_words_count[1] +=1
        for word in negative_words:
            if tweet_word.lower() == word:
                group_of_words_count[2] += 1
    return group_of_words_count

def most_positive(tweets):
    most_positive_tweet = ""
    positive_words_counter = 0
    for tweet in tweets:
        group_of_words = count_group_of_words(tweet)
        if group_of_words[0] > positive_words_counter:
            positive_words_counter = group_of_words[0]
            most_positive_tweet = tweet

    return most_positive_tweet

def most_negative(tweets):
    most_negative_tweet = ""
    negative_words_counter = 0
    for tweet in tweets:
        group_of_words = count_group_of_words(tweet)
        if group_of_words[2] > negative_words_counter:
            negative_words_counter = group_of_words[2]
            most_negative_tweet = tweet

    return most_negative_tweet

def average_quality(tweet):
    tweet_array = tweet.replace("!","").replace(",","").replace(".","").replace("(","").replace(")","").split()
    quantity = len(tweet_array)
    return (1 / quantity) * (count_words_in_tweet(tweet))

def score(tweet):
    b = count_group_of_words(tweet)
    a = np.array([1,0,-1])
    return np.dot(a,b)


def main():
    tweets = np.array([tweet1, tweet2, tweet3, tweet4])
    
    most_positive_tweet = most_positive(tweets)
    print("Tweet mas positivo: ", most_positive_tweet)

    most_negative_tweet = most_negative(tweets)
    print("Tweet mas negativo: ", most_negative_tweet)

    for tw in tweets:
        avg = average_quality(tw)
        sc = score(tw)
        print("Tweet: ", tw)
        print("Promedio de calidad: ", avg)
        print("Score: ", sc)

if __name__ == "__main__":
    main()