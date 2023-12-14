<!DOCTYPE html>
<html>
<head>
    <title>{{ project['title'] }} Details</title>
</head>
<body>
    <h1>{{ project['title'] }} Details</h1>
    <p>Title: {{ project['title'] }}</p>
    <p>Description: {{ project['description'] }}</p>
    <p>Lead Member: {{ project['member']['name'] }}</p>

    <h2>Ratings</h2>
    <ul>
        % for rating in ratings:
            <li>{{ rating[1] }}</li>
        % end
    </ul>

    <a href="/projects/{{ project['id'] }}/add_rating">Add a Rating</a>
    <a href="/projects/{{ project['id'] }}/update">Update Project</a>
    <a href="/projects/{{ project['id'] }}/delete">Delete Project</a>
    <a href="/projects">Back to Projects</a>
</body>
</html>
