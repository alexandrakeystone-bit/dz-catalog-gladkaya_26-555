import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


def average_rating(movies):
    """Средняя оценка по каталогу, округленная до 1 знака."""
    total = 0.0
    for movie in movies:
        total += movie["rating"]
    return round(total / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    """(возраст самого старого, возраст самого нового, средний возраст)."""
    oldest_age = current_year - min(movie["year"] for movie in movies)
    newest_age = current_year - max(movie["year"] for movie in movies)

    total_age = 0
    for movie in movies:
        total_age += current_year - movie["year"]
    average_age = math.ceil(total_age / len(movies))

    return (oldest_age, newest_age, average_age)


def duration_in_hours(minutes):
    """Минуты -> строка вида '2ч 35м'."""
    hours = minutes // 60
    remainder = minutes % 60
    return f"{hours}ч {remainder}м"


def rating_tier(rating):
    """Категория фильма по рейтингу."""
    if rating >= 9:
        label = "шедевр"
    elif rating >= 7:
        label = "хорошо"
    elif rating >= 5:
        label = "средне"
    else:
        label = "слабо"
    return label if rating <= 10 else "некорректный рейтинг"


def decade_label(year):
    """Метка поколения фильма по году выпуска."""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


def print_non_comedy(movies):
    """Печатает названия фильмов, которые не относятся к жанру 'comedy'."""
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def find_first_masterpiece(movies):
    """Печатает первый фильм с рейтингом > 9.0. Если нет — сообщение."""
    index = 0
    while index < len(movies):
        movie = movies[index]
        if movie["rating"] > 9.0:
            print("Первый шедевр:", movie["title"])
            break
        index += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    """Считает фильмы длиннее 120 минут (строго больше)."""
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


if __name__ == "__main__":
    print("Средняя оценка:", average_rating(movies))
    print("Возрасты:", catalog_age_stats(movies))
    print("Длительность 155 мин:", duration_in_hours(155))

    for r in (9.2, 8.9, 7.0, 5.0, 4.8):
        print(f"rating={r} -> {rating_tier(r)}")

    for y in (2011, 2014, 2015, 2020, 2021, 2024):
        print(f"year={y} -> {decade_label(y)}")

    print("\n--- Фильмы не-comedy ---")
    print_non_comedy(movies)

    print("\n--- Первый шедевр ---")
    find_first_masterpiece(movies)

    print("\n--- Шедевры не найдены (проверка else) ---")
    movies_without_masterpiece = [
        m for m in movies if m["title"] != "The Quiet Algorithm"
    ]
    find_first_masterpiece(movies_without_masterpiece)

    print("\n--- Фильмы длиннее 120 минут ---")
    print("Количество:", count_long_movies(movies))
    print("Длиннее 130:", count_long_movies(movies, threshold=130))
