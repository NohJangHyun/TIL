from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("WorstMoviesDF").getOrCreate()

    df_rating = spark.read.load("ml-latest-small/ratings.csv", format="csv", sep = ",", inferSchema="true", header="true")
    df_movie = spark.read.load("ml-latest-small/movies.csv", format="csv", sep=",", inferSchema="true", header="true")

    df_rating.createOrReplaceTempView("ratings")
    df_movie.createOrReplaceTempView("movies")

    result = spark.sql("""
        SELECT title, rating, cnt
        FROM movies JOIN(
            SELECT movieId, avg(rating) as rating, count(rating) as cnt
            FROM ratings GROUP BY movieId
        ) r ON movies.movieId = r.movieId
        WHERE rating < 2.0 AND cnt > 30
        ORDER BY cnt
        """)

    for row in result.collect():
        print(row.title, round(row.rating,2), row.cnt, sep="    ")
