import psycopg2
from psycopg2.extras import DictCursor

conn = psycopg2.connect('postgresql://postgres:@localhost:5432/test_db')


# BEGIN (write your solution here)
def create_post(conn, post):
    with conn.cursor() as cursor:
        query = """
        INSERT INTO posts (title, content, author_id) 
        VALUES (%s, %s, %s) 
        RETURNING id
        """
        cursor.execute(query, (post['title'], post['content'], post['author_id']))
        post_id = cursor.fetchone()[0]
        conn.commit()
        return post_id


def add_comment(conn, comment):
    with conn.cursor() as cursor:
        query = """
        INSERT INTO comments (post_id, author_id, content) 
        VALUES (%s, %s, %s) 
        RETURNING id
        """
        cursor.execute(query, (comment['post_id'], comment['author_id'], comment['content']))
        comment_id = cursor.fetchone()[0]
        conn.commit()
        return comment_id


def get_latest_posts(conn, n):
    with conn.cursor(cursor_factory=DictCursor) as cursor:
        query_posts = """
        SELECT * 
        FROM posts 
        ORDER BY created_at DESC 
        LIMIT %s
        """
        cursor.execute(query_posts, (n,))
        posts = cursor.fetchall()

        result = []
        for post in posts:
            query_comments = """
            SELECT * 
            FROM comments 
            WHERE post_id = %s 
            ORDER BY created_at ASC
            """
            cursor.execute(query_comments, (post['id'],))
            comments = cursor.fetchall()

            comments_list = [
                {
                    'id': comment['id'],
                    'author_id': comment['author_id'],
                    'content': comment['content'],
                    'created_at': comment['created_at']
                } for comment in comments
            ]

            result.append({
                'id': post['id'],
                'title': post['title'],
                'content': post['content'],
                'author_id': post['author_id'],
                'created_at': post['created_at'],
                'comments': comments_list
            })
        return result
# END
