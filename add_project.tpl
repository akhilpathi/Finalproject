<!DOCTYPE html>
<html>
<head>
    <title>Add Project</title>
</head>
<body>
    <h1>Add Project</h1>
    <form action="/projects/add" method="post">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required><br>

        <label for="description">Description:</label>
        <textarea id="description" name="description" required></textarea><br>

        <label for="member_id">Lead Member:</label>
        <select id="member_id" name="member_id" required>
            % for member in members:
                <option value="{{ member['id'] }}">{{ member['name'] }}</option>
            % end
        </select><br>

        <input type="submit" value="Add Project">
    </form>
    <a href="/projects">Back to Projects</a>
</body>
</html>
