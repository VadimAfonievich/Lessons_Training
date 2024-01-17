import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)


def main():

    @app.route('/')
    def hello():
        return 'Hello, FilmLOVER!'

    def connect_db(query):
        with sqlite3.connect("netflix.db") as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()

            return result

    @app.route("/movie/<title>/")
    def search_film_for_title(title):
        query = f"""
            SELECT title, country, release_year, listed_in, description
            FROM netflix
            WHERE title = '{title}'
            LIMIT 1
        """

        film = connect_db(query)

        searched_film = {
            "title": film[0][0],
            "country": film[0][1],
            "release_year": film[0][2],
            "genre": film[0][3],
            "description": film[0][4]
        }

        for attribute, value in searched_film.items():
            print(f"{attribute}: {value}")

        return jsonify(searched_film)

    @app.route("/movie/<start_year>/to/<end_year>")
    def search_film_by_year(start_year, end_year):
        query = f"""
            SELECT title, release_year
            FROM netflix
            WHERE release_year BETWEEN {start_year} AND {end_year}
            ORDER BY release_year ASC
            LIMIT 100
        """

        films = connect_db(query)

        searched_films = []

        for film in films:
            searched_films.append({
                "title": film[0],
                "release_year": film[1]
            })

        return jsonify(searched_films)

    @app.route("/movie/rating/<group>")
    def search_film_for_rating(group):
        levels = {
            "children": ["G"],
            "family": ['G', 'PG', 'PG-13'],
            "adult": ["R", "NC-17"]
        }

        if group in levels:
            level = "\',\'".join(levels[group])
            level = f"\'{level}\'"
        else:
            return jsonify([])

        query = f"""
                SELECT title, rating, description
                FROM netflix
                WHERE rating IN ({level})
                ORDER BY release_year ASC
                LIMIT 10
                """

        films = connect_db(query)
        # print(films)

        searched_films = []

        for film in films:
            searched_films.append({
                "title": film[0],
                "rating": film[1],
                "description": film[2].strip()
            })

        return jsonify(searched_films)

    @app.route("/genre/<genre>")
    def search_film_by_genre(genre):
        query = f"""
            SELECT title, description, listed_in, release_year
            FROM netflix
            WHERE listed_in LIKE '%{genre}%'
            ORDER BY release_year DESC
            LIMIT 10
        """

        films = connect_db(query)

        searched_films = []

        for film in films:
            searched_films.append({
                "title": film[0],
                "description": film[1],
                "listed_in": film[2],
                "release_year": film[3]
            })

        return jsonify(searched_films)

    @app.route("/actors/<first_actor>/and/<second_actor>")
    def search_film_by_actors(first_actor, second_actor):
        query_actors = f"""
                    SELECT "cast"
                    FROM netflix 
                    WHERE "cast" LIKE '%{first_actor}%'
                    AND "cast" LIKE '%{second_actor}%'
                """
        # Получаем всех актеров, которые играли с первым актером
        actors = connect_db(query_actors)
        common_coactors = set(actor for row in actors for actor in row[0].split(', '))

        # Создаем словарь для подсчета встречаемости каждого актера
        coactor_count = {}

        # Подсчитываем встречаемость каждого актера в колонке "cast" для пары актеров
        for coactor in common_coactors:
            films = connect_db(f"""SELECT COUNT(*) FROM netflix WHERE "cast" LIKE '%{coactor}%'""")
            coactor_count[coactor] = films[0][0] if films else 0

        # Фильтруем актеров, игравших с обоими актерами более 2 раз
        result = [coactor for coactor, count in coactor_count.items() if count > 2]

        # Выводим результат в формате JSON
        return jsonify({"coactors": result})

    @app.route("/type/<film_type>/<release_year>/<genre>")
    def search_film_by_type(film_type, release_year, genre):
        query = f"""
                    SELECT type, title, release_year, listed_in, description
                    FROM netflix 
                    WHERE type LIKE '%{film_type}%'
                    AND release_year > '{release_year}'
                    AND listed_in LIKE '%{genre}%'
                    LIMIT 100
        """
        # Получаем всех актеров, которые играли с первым актером
        films = connect_db(query)

        searched_films = []

        for film in films:
            searched_films.append({
                "type": film[0],
                "title": film[1],
                "release_year": film[2],
                "genre": film[3],
                "description": film[4]
            })

        # Выводим результат в формате JSON
        return jsonify({"searched films by type": searched_films})


if __name__ == "__main__":
    main()
    app.run(port=5000, debug=True)



# #############################################################################
# """
# группировка данных
# - GROUP BY
#
# Агрегирующие функции:
# - COUNT()
# - MAX  (SELECT MIN(release_year), MAX(release_year)
#         FROM netflix)
# - MIN
# - AVG
# - SUM
# - HAVING
# """
#
# import sqlite3
#
# with sqlite3.connect("netflix.db") as connection:
#     cursor = connection.cursor()
#     # query = """
#     #     SELECT release_year, type, country, title
#     #     FROM netflix
#     #     WHERE country != ''
#     #     GROUP BY release_year, type, country, title
#     # """
#
#     # query_count = """
#     #     SELECT MIN(release_year), MAX(release_year)
#     #     FROM netflix
#     # """
#
#     query_sum_duration = """
#         SELECT country, SUM(duration) as total_duration
#         FROM netflix
#         WHERE type = 'TV Show' AND country != ''
#         GROUP BY country
#         HAVING total_duration > 100
#         ORDER BY total_duration DESC
#         LIMIT 15
#     """
#
#
#     # cursor.execute(query)
#     # cursor.execute(query_count)
#     cursor.execute(query_sum_duration)
#
#     for row in cursor.fetchall():
#         print(row)




# #############################################################################
# """
# Сортировка данных (обычная и множественная)
# - ORDER_BY - ключевое слово для сортировки данных по конкретному столбцу.
# - ASC - сортировка от меньшего к большему.
# - DESC - сортировка от большего к меньшему.
# """
# import sqlite3
#
# with sqlite3.connect("netflix.db") as connection:
#     cursor = connection.cursor()
#
#     query = """
#         SELECT title, release_year, duration
#         FROM netflix
#         ORDER BY release_year DESC, duration ASC
#         LIMIT 10
#     """
#
# cursor.execute(query)
#
# for row in cursor.fetchall():
#     print(row)



# ##############################################################################
# """
# Подключение с SQLite
# Фильтрация данных
# Условия - совпадение, диапазоны, вхождения, пустые значения
# Комбинации - логические операторы
# """
# import sqlite3
#
# with sqlite3.connect("netflix.db") as connection:
#     cursor = connection.cursor()
#     query_type = """
#         SELECT *
#         FROM netflix
#         WHERE title LIKE 'American%'
#         AND type = 'Movie'
#         AND director != '' AND director IS NOT NULL
#     """
#
#     cursor.execute(query_type)
#
#     for row in cursor.fetchall():
#         print(row)
#
#     # получить описание столбцов
#     columns = [column[0] for column in cursor.description]
#
#     print()
#     print(columns)
#     print()
#
#     query_columns = """
#         SELECT director, title
#         FROM netflix
#         LIMIT 10
#         OFFSET 200
#     """
#
#     cursor.execute(query_columns)
#
#     for row in cursor.fetchall():
#         if row[0] == "":
#             continue
#         print(f"director - {row[0]}, title: '{row[1]}'")


# ##############################################################################
# """
# Подключение с SQLite
# """
#
# import sqlite3
#
# with sqlite3.connect("netflix.db") as connection:
#     cursor = connection.cursor()
#     query = """
#         SELECT *
#         FROM netflix
#         LIMIT 15
#         OFFSET 15
#     """
#
#     cursor.execute(query)
#
#     for row in cursor.fetchall():
#         print(row)
