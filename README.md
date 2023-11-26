# Blog API
Homework assignment for the [SPŠE Ječná](https://www.spsejecna.cz/) school.
The goal of this assignment is to create a simple REST API for a blog application.


## Table of Contents

  - [API Documentation](#api-documentation)
    - [1. GET All Blog Posts](#1-get-all-blog-posts)
    - [2. GET Specific Blog Post](#2-get-specific-blog-post)
    - [3. Create Blog Post](#3-create-blog-post)
    - [4. Update Blog Post](#4-update-blog-post)
    - [5. Delete Blog Post](#5-delete-blog-post)


## API Documentation

---

### 1. **GET All Blog Posts**

#### Endpoint:
```markdown
GET /api/blog
```

#### Description:
Retrieve a list of all blog posts.

#### Response:
- **Status Code:** 200 OK
- **Body:**
  ```json
  [
    {
      "id": 1,
      "content": "Lorem ipsum...",
      "creation_date": "2023-01-01",
      "author_id": 1
    },
    {
      "id": 2,
      "content": "Dolor sit amet...",
      "creation_date": "2023-01-02",
      "author_id": 2
    },
    ...
  ]
  ```

---

### 2. **GET Specific Blog Post**

#### Endpoint:
```markdown
GET /api/blog/<int:blog_id>
```

#### Description:
Retrieve a specific blog post by its ID.

#### Parameters:
- `blog_id` (integer): The ID of the blog post.

#### Response:
- **Status Code:**
  - 200 OK: Blog post found.
  - 404 Not Found: Blog post not found.
- **Body:**
  ```json
  {
    "id": 1,
    "content": "Lorem ipsum...",
    "creation_date": "2023-01-01",
    "author_id": 1
  }
  ```

---

### 3. **Create Blog Post**

#### Endpoint:
```markdown
POST /api/blog
```

#### Description:
Create a new blog post.

#### Request Body:
- **Content Type:** application/json
- **Body:**
  ```json
  {
    "content": "Lorem ipsum...",
    "creation_date": "2023-01-01",
    "author_id": 1
  }
  ```

#### Response:
- **Status Code:** 
  - 201 Created: Blog post created successfully.
  - 400 Bad Request: Invalid JSON format or missing required fields.
  - 500 Internal Server Error: Error creating the blog post.

---

### 4. **Update Blog Post**

#### Endpoint:
```markdown
PATCH /api/blog/<int:blog_id>
```

#### Description:
Partially update a blog post by its ID.

#### Parameters:
- `blog_id` (integer): The ID of the blog post.

#### Request Body:
- **Content Type:** application/json
- **Body:**
  ```json
  {
    "content": "Updated content...",
    "creation_date": "2023-01-02"
  }
  ```

#### Response:
- **Status Code:**
  - 200 OK: Blog post updated successfully.
  - 400 Bad Request: Invalid JSON format.
  - 404 Not Found: Blog post not found.
  - 500 Internal Server Error: Error updating the blog post.

---

### 5. **Delete Blog Post**

#### Endpoint:
```markdown
DELETE /api/blog/<int:blog_id>
```

#### Description:
Delete a blog post by its ID.

#### Parameters:
- `blog_id` (integer): The ID of the blog post.

#### Response:
- **Status Code:**
  - 200 OK: Blog post deleted successfully.
  - 404 Not Found: Blog post not found.
  - 500 Internal Server Error: Error deleting the blog post.

---