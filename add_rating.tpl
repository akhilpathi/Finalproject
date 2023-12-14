<!DOCTYPE html>
<html>
<head>
    <title>Add Rating</title>
</head>
<body>
    <h1>Add Rating</h1>
    <form action="/projects/{{ project_id }}/add_rating" method="post">
        <label for="rating">Rating:</label>
        <input type="number" id="rating" name="rating" min="1" max="5" required><br>

        <input type="submit" value="Add Rating">
    </form>
    <a href="/projects/{{ project_id }}">Back to Project Details</a>
</body>
</html>
