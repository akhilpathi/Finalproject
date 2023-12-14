<!DOCTYPE html>
<html>
<head>
    <title>Update Project</title>
</head>
<body>
    <h1>Update Project</h1>
    <form action="/projects/{{ project['id'] }}/update" method="post">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" value="{{ project['title'] }}" required><br>

        <label for="description">Description:</label>
        <textarea id="description" name="description" required>{{ project['description'] }}</textarea><br>

        <label for="member_id">Lead Member:</label>
        <select id="member_id" name="member_id" required>
            % for member in members:
                <option value="{{ member['id'] }}" {% if member['id'] == project['member_id'] %}selected{% end %}>{{ member['name'] }}</option>
            % end
        </select><br>

        <input type="submit" value="Update Project">
    </form>
    <a href="/projects/{{ project['id'] }}">Back to Project Details</a>
</body>
</html>
