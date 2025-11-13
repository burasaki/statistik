import pandas as pd
import os
from dotenv import load_dotenv
from collections import defaultdict



load_dotenv()
maths531_URL = os.getenv("MATHS531_URL")
algem531_URL = os.getenv("ALGEM531_URL")
inf531_URL = os.getenv("INF531_URL")
prog531_URL = os.getenv("PROG531_URL")

maths532_URL = os.getenv("MATHS532_URL")
algem532_URL = os.getenv("ALGEM532_URL")
inf532_URL = os.getenv("INF532_URL")
prog532_URL = os.getenv("PROG532_URL")
#Список предметов по которым собираются данные
grops_predmets_info = {
            "ИКС-531":{
                'Математика': [maths531_URL,'A', 100],
                'АиГ': [algem531_URL,'A', 100],
                'Информатика': [inf531_URL,'A', 10],
                'Программирование': [prog531_URL,"B", 10]
            },
            "ИКС-532":{
                'Математика': [maths532_URL,'A', 100],
                'АиГ': [algem532_URL,'A', 100],
                'Информатика': [inf532_URL,'A', 10],
                'Программирование': [prog532_URL,"B", 10]
            }

        }

def get_rating_a_subject(url:str, index_of_name:str, divider:int) -> dict[str, float]:
    """returns the ranking of all students by subject"""
    df = pd.read_html(url, encoding='utf-8')[0]
    name_of_ratings_row = ['текущий рейтинг', 'Рейтинг', 'Итог <= 100', "ПРОЦЕНТ"]
    rating_column = [x for x, value in df.iloc[0].to_dict().items() if value in name_of_ratings_row]

    ratings = df.set_index(index_of_name)[rating_column][::].to_dict()[''.join(rating_column)]
    ratings = {key.split(' ')[0].capitalize():int(value)/divider for key, value in ratings.items() if type(value) == str and value.isdigit() and type(key) == str}
    
    return ratings


def get_ratings_all_students(grop:str) -> dict[str, dict[str, int]]:
    """returns the ranking of all students in all subjects"""
    predmets = grops_predmets_info[grop]
    
    ratings_all_students = defaultdict(dict)
    for predmet, info in predmets.items():
        predmet_url, predmet_index_of_name, predmet_divider = info

        rating_a_subject = get_rating_a_subject(predmet_url, predmet_index_of_name, predmet_divider)

        for student, rating in rating_a_subject.items():
            ratings_all_students[student][predmet] = rating

    names_to_dell = []
    for i in ratings_all_students:
        if len(ratings_all_students[i]) < 4:
            names_to_dell.append(i)
    for name in names_to_dell:
        del ratings_all_students[name]
    return dict(ratings_all_students)

if __name__ == '__main__':
    print(get_ratings_all_students("ИКС-531"))