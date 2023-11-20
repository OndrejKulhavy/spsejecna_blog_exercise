from flask import Flask, request, jsonify, abort, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_DB'] = 'blog'
app.config['MYSQL_HOST'] = 'localhost'

mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT blog_posts.title, blog_posts.content, blog_posts.creation_date, users.username FROM blog_posts JOIN users ON blog_posts.author_id = users.id")
    blog_posts = cursor.fetchall()
    cursor.close()
    print(blog_posts)
    return render_template('index.html', blog_posts=blog_posts)

@app.route('/api/blog', methods=['POST'])
def create_blog_post():
    data = request.get_json()

    if 'content' not in data or 'creation_date' not in data or 'author_name' not in data:
        abort(400, 'Invalid JSON format. Content, creation_date, and author_name are required.')

    cursor = mysql.connection.cursor()

    try:
        cursor.execute("INSERT INTO blog_posts (content, creation_date, author_id) VALUES (%s, %s, %s)",
                       (data['content'], data['creation_date'], data['author_id']))
        mysql.connection.commit()
        blog_post_id = cursor.lastrowid
        return jsonify({'id': blog_post_id}), 201
    except Exception as e:
        abort(500, f"Error creating blog post: {str(e)}")
    finally:
        cursor.close()

# Metoda pro zobrazení všech blog postů


@app.route('/api/blog', methods=['GET'])
def get_all_blog_posts():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM blog_posts")
    blog_posts = cursor.fetchall()
    cursor.close()
    return jsonify(blog_posts)

# Metoda pro zobrazení konkrétního blog postu podle id


@app.route('/api/blog/<int:blog_id>', methods=['GET'])
def get_blog_post(blog_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM blog_posts WHERE id = %s", (blog_id,))
    blog_post = cursor.fetchone()
    cursor.close()

    if blog_post is None:
        abort(404, 'Blog post not found.')

    return jsonify(blog_post)

# Metoda pro smazání konkrétního blog postu podle id


@app.route('/api/blog/<int:blog_id>', methods=['DELETE'])
def delete_blog_post(blog_id):
    cursor = mysql.connection.cursor()

    try:
        cursor.execute("DELETE FROM blog_posts WHERE id = %s", (blog_id,))
        mysql.connection.commit()
        return jsonify({'message': 'Blog post deleted successfully.'})
    except Exception as e:
        abort(500, f"Error deleting blog post: {str(e)}")
    finally:
        cursor.close()

# Metoda pro částečný update konkrétního blog postu podle id


@app.route('/api/blog/<int:blog_id>', methods=['PATCH'])
def update_blog_post(blog_id):
    cursor = mysql.connection.cursor()

    try:
        data = request.get_json()
        update_query = "UPDATE blog_posts SET "
        update_params = []

        if 'content' in data:
            update_query += "content = %s, "
            update_params.append(data['content'])

        if 'creation_date' in data:
            update_query += "creation_date = %s, "
            update_params.append(data['creation_date'])

        if 'author_id' in data:
            update_query += "author_id = %s, "
            update_params.append(data['author_id'])

        # Remove trailing comma and space
        update_query = update_query.rstrip(', ')

        update_query += f" WHERE id = %s"
        update_params.append(blog_id)

        cursor.execute(update_query, tuple(update_params))
        mysql.connection.commit()
        return jsonify({'message': 'Blog post updated successfully.'})
    except Exception as e:
        abort(500, f"Error updating blog post: {str(e)}")
    finally:
        cursor.close()


if __name__ == '__main__':
    app.run()
