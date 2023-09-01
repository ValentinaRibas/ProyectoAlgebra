import numpy as np
import pandas as pd

tweet1="Fernando Alonso se dirige a los 'Tifosi': Es un placer estar aquí siempre, aunque no esté en Ferrari. Espero que tengamos por fin una carrera en seco y hacer un buen espectáculo para todos vosotros. También deseo que a Ferrari le vaya bien"
tweet2="El ridículo es que es enorme la diferencia entre Ferrari y Red Bull, muy malo el trabajo de los pits de Ferrari, son el peor del campeonato"
tweet3="El Domingo veremos el mejor podio de 2023, La pasión y el amor de los fans de Ferrari hace que las victorias de otros equipos en Monza sean uno de los momentos más memorables de la temporada"
tweet4="Llego el Patrón al ItalianGP buongiorno Checo! Por un buen fin de semana! Vamos Checo a ganar"
tweet5="Ya no puedo con Ferrari, siempre estan con quejas, llorando por su coche que no es rápido, hasta cuando van a seguir sin ganar, ya es un desastre esto, nefasto el rendimiento"

positive_words = ["excelente",
                  "gran",
                  "positivo",
                  "placer",
                  "buen",
                  "deseo",
                  "bien",
                  "mejor",
                  "pasión",
                  "amor",
                  "victorias",
                  "buen",
                  "ganar"]

neutro_words = ["pérdida",
                "enorme",
                "diferencia"]

negative_words = ["muerte",
                  "luto",
                  "ridículo",
                  "malo",
                  "peor",
                  "malos",
                  "quejas",
                  "llorando",
                  "desastre",
                  "nefasto"]

words = ["excelente",
                  "gran",
                  "positivo",
                  "placer",
                  "buen",
                  "deseo",
                  "bien",
                  "mejor",
                  "pasión",
                  "amor",
                  "victorias",
                  "buen",
                  "ganar",
                  "pérdida",
                  "enorme",
                  "diferencia",
                  "muerte",
                  "luto",
                  "ridículo",
                  "malo",
                  "peor",
                  "malos",
                  "quejas",
                  "llorando",
                  "desastre",
                  "nefasto"]


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
    tweets = np.array([tweet1, tweet2, tweet3, tweet4, tweet5])
    
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