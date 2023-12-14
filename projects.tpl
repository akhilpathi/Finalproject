
<!DOCTYPE html>
<html>
<head>
    <title>Projects</title>
</head>
<body>
    <h1>Projects</h1>
    <ul>
        % for project in projects:
            <li>
                <a href="/projects/{{ project['id'] }}">{{ project['title'] }}</a>
            </li>
        % end
    </ul>
    <a href="/projects/add">Add a Project</a>
</body>
</html>

