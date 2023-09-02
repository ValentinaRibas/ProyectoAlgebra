import numpy as np
import pandas as pd

tweet1="Alonso: Es un placer estar aquí siempre, siento amor por la Tifosi. Espero hacer un buen espectáculo para todos. Deseo que a Ferrari le vaya bien"
tweet2="El ridículo es que es enorme la diferencia entre Ferrari y Red Bull, muy malo el trabajo de los pits de Ferrari, son el peor del campeonato"
tweet3="El fin de semana veremos el mejor podio de 2023, siempre es enorme la pasión y el amor de los fans de Ferrari, hace que las victorias de otros equipos en Monza sean un espectáculo y uno de los momentos más memorables de la temporada"
tweet4="Llego el Patrón al ItalianGP buongiorno Checo! Por un buen fin de semana! Vamos Checo a ganar, te deseo muchas victorias! Arriba Mexico, si estamos unidos la pasion nos hara ganar, Go Red Bull a ganar a Ferrari"
tweet5="No puedo con Ferrari, siempre estan con quejas, llorando por su coche que no es rápido, hasta cuando van a seguir sin ganar, ya es un desastre esto, nefasto el rendimiento"

positive_words = ["placer",
                  "deseo",
                  "bien",
                  "mejor",
                  "pasión",
                  "amor",
                  "victorias",
                  "buen",
                  "ganar"]

neutro_words = ["enorme",
                "diferencia",
                "siempre",
                "si",
                "no",
                "Espero",
                "espectáculo",
                "muy",
                "trabajo",
                "hace",
                "memorables",
                "momentos",
                "buongiorno",
                "fin",
                "semana",
                "vamos",
                "puedo",
                "cuando",
                "Ferrari",
                "Red",
                "Bull"]

negative_words = ["ridículo",
                  "malo",
                  "peor",
                  "malos",
                  "quejas",
                  "llorando",
                  "desastre",
                  "nefasto"]

words = ["placer",
        "deseo",
        "bien",
        "mejor",
        "pasión",
        "amor",
        "victorias",
        "buen",
        "ganar"
        "enorme",
        "diferencia",
        "siempre",
        "si",
        "no",
        "Espero",
        "espectáculo",
        "muy",
        "trabajo",
        "hace",
        "memorables",
        "momentos",
        "buongiorno",
        "fin",
        "semana",
        "vamos",
        "puedo",
        "cuando",
        "Ferrari",
        "Red",
        "Bull",
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
            if tweet_word.lower() == words[i].lower():
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
    n = len(words)
    w = sum(count_words_in_tweet(tweet))
    avg_quality = np.dot(1/n,w)
    return avg_quality

def score(tweet):
    b = count_group_of_words(tweet)
    a = np.array([1,0,-1])
    return np.dot(a,b)

def total_average(tweets):
    added_average = 0
    for tw in tweets:
        avg = average_quality(tw)
        added_average += avg
    total_average = added_average / 5
    return total_average

def average_score(tweets):
    added_score = 0
    for tw in tweets:
        indiv_score = score(tw)
        added_score += indiv_score
    avg_score = added_score / 5
    return avg_score

def main():
    print("----------------------------------------------------------")
    print("Inicio del programa")
    tweets = np.array([tweet1, tweet2, tweet3, tweet4, tweet5])
    
    most_positive_tweet = most_positive(tweets)
    print("Tweet mas positivo: ", most_positive_tweet)

    most_negative_tweet = most_negative(tweets)
    print("Tweet mas negativo: ", most_negative_tweet)

    for tw in tweets:
        avg = average_quality(tw)
        sc = score(tw)
        w = sum(count_words_in_tweet(tw))
        print("Tweet: ", tw)
        print("Cantidad de palabras detectadas: ", w)
        print("Promedio de calidad: ", avg)
        print("Score: ", sc)
    print("\nFin de procesamiento principal")
    print("----------------------------------------------------------")
    print("Inicio de procesamiento para preguntas de informe")
    total_avg = total_average(tweets)
    avg_score = average_score(tweets)
    print("El promedio total de calidad de los tweets es", total_avg)
    print("El promedio total de puntaje de los tweets es", avg_score)
    print("\nFin de procesamiento para preguntas")
    print("----------------------------------------------------------")
    
    
if __name__ == "__main__":
    main()