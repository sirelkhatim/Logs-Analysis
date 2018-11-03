import psycopg2

DBNAME = 'news'

query1 = """
            SELECT title, count(log.id) AS num from articles,log
            WHERE log.path = Concat('/article/',articles.slug)
            GROUP BY articles.title order by num desc limit 3
        """
query2 = """
            SELECT authors.name, COUNT(*) AS num from authors,articles,log
             WHERE log.status = '200 OK' and authors.id = articles.author AND articles.slug = substr(log.path,10)
            GROUP BY authors.name ORDER BY num DESC
        """
query3 = """
            WITH requests AS
            ( SELECT time::date AS day, count(*) FROM log GROUP BY time::date ORDER BY time::date),
            errors AS
            (SELECT time::date AS day, count(*) FROM log WHERE status!= '200 OK' GROUP BY time::date
            ORDER BY time::date),
            error_rate AS
            (SELECT requests.day, errors.count::float / requests.count::float * 100
            AS error_percentage FROM requests, errors WHERE requests.day = errors.day)
            SELECT * FROM error_rate WHERE error_percentage > 1;
        """


def get_posts(query):
    """
    Function that connects to a database executes a query and outputs the result after closing the connection
    :param
    query: SQL query that you want to execute
    :return
    articles: result from executing the query
    """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    articles = c.fetchall()
    db.close()
    return articles


def get_most_popular_articles():
    """
    Function that formats the output of query 1 to display it in a user friendly way
    """
    results = get_posts(query1)
    print("Top three most popular articles:\n")
    for result in results:
        print(
            '{title} - {count} views'.format(title=result[0], count=result[1]))
    print("\n")
    return


def get_most_popular_authors():
    """
    Function that formats the output of query2 to display it in a user friendly way
    """
    results = get_posts(query2)
    print("Most popular authors:\n")
    for result in results:
        print(
            '{author} - {count} views'.format(author=result[0], count=result[1]))
    print("\n")
    return


def get_errors():
    """
    Function that formats the output of query3 to display it in a user friendly way
    """
    results = get_posts(query3)
    print("Days with greater than 1% errors:\n")
    for result in results:
        print('{date:%B %d, %Y} - {error_rate:.1f}% errors'.format(
            date=result[0],
            error_rate=result[1]
        ))
    print("\n")
    return


if __name__ == '__main__':
    get_most_popular_articles()
    get_most_popular_authors()
    get_errors()
