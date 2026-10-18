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
    """Печатает названия фильмов, которые НЕ относятся к жанру 'comedy'."""
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


def normalize_title(title):
    """Приводит строку к Title Case без использования str.title()."""
    words = title.split()
    normalized_words = []
    for word in words:
        if word:
            normalized_words.append(word[0].upper() + word[1:].lower())
    return " ".join(normalized_words)


def make_slug(title):
    """Превращает название в slug: 'Silent Hours' -> 'silent-hours'."""
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    """Одна строка отчета о фильме."""
    title = movie["title"]
    year = movie["year"]
    rating = movie["rating"]
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    return f"'{title}' ({year}) — {rating}/10, {duration}, жанры: {genres}"


def titles_sorted_by_rating(movies):
    """Список названий фильмов, отсортированных по убыванию рейтинга."""
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(movies, n=3):
    """Топ-n фильмов по рейтингу: список кортежей (title, rating)."""
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]


def count_by_genre(movies):
    """Возвращает словарь {жанр: количество фильмов}."""
    genre_counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            # Если жанра нет в словаре, get вернёт 0, и мы прибавим 1.
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
    return genre_counts


def actor_filmography(movies):
    """Возвращает словарь {актер: [список фильмов]}."""
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []
            filmography[actor].append(movie["title"])
    return filmography


def above_average_ratings(movies):
    """Возвращает {title: rating} только для фильмов с рейтингом выше среднего."""
    avg = average_rating(movies)
    return {
        movie["title"]: movie["rating"]
        for movie in movies
        if movie["rating"] > avg
    }

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

    print("\n--- Этап 4: строки ---")
    print(normalize_title("silent hours"))
    print(normalize_title("midnight in oslo"))
    print(make_slug("Silent Hours"))
    print(make_slug("The Quiet Algorithm"))
    print(format_report_line(movies[7]))

    print("\n--- Отчет по всем фильмам ---")
    for movie in movies:
        print(format_report_line(movie))

    
    print("\n--- Этап 5: списки ---")
    print("Названия по убыванию рейтинга:")
    for title in titles_sorted_by_rating(movies):
        print(" ", title)

    print("\nТоп-3 по рейтингу:")
    for title, rating in top_n_by_rating(movies, 3):
        print(f"  {title} — {rating}")

    print("\nТоп-5 по рейтингу:")
    for title, rating in top_n_by_rating(movies, 5):
        print(f"  {title} — {rating}")

    print("\nПроверка: movies не отсортирован —")
    print("  первый фильм в movies:", movies[0]["title"])


    print("\n--- Этап 6: словари ---")
    print("Количество по жанрам:")
    genres = count_by_genre(movies)
    for genre, count in sorted(genres.items()):
        print(f"  {genre}: {count}")

    print("\nФильмография (некоторые актеры):")
    filmography = actor_filmography(movies)
    for actor in sorted(filmography.keys()):
        print(f"  {actor}: {filmography[actor]}")

    print("\nФильмы с рейтингом выше среднего (7.2):")
    above_avg = above_average_ratings(movies)
    for title, rating in above_avg.items():
        print(f"  {title}: {rating}")