# Friendly-Recruitment-Task

## How to run

After cloning the project open command prompt, navigate to project's root directory (Friendly-Recruitment-Task) and execute:

```bash
# Navigate to 'mysite' directory ("/../Friendly-Recruitment-Task/friendlyTask/mysite"):
$ cd friendlyTask/mysite

# Install dependencies:
$ pip install -r requirements.txt

# To run an app: (or 'python' if you use an earlier version)
$ python3 manage.py runserver 

```

## Endpoints

### POST:

#### http://127.0.0.1:8000/add - connects with external API

body example in JSON format:
```
{
    "albumId": 3,
    "title": "quidem ut quos non qui debitis exercitationem"
}
```

You can also use this route via CLI:

```bash

$ curl -i -H "Content-Type: application/json" -X POST -d "{\"albumId\": 3, \"title\": \"reiciendis et velit laborum recusandae\"}" http://127.0.0.1:8000/add

```

#### http://127.0.0.1:8000/file/add - Uses local JSON file

To use the route above you first need to import JSON file from external API via CLI:

```bash
# make sure that you are in "/../Friendly-Recruitment-Task/friendlyTask/mysite" directory
$ curl -o friendlyTask/static/json/photos.json --create-dirs https://jsonplaceholder.typicode.com/photos

```

### GET:

#### http://127.0.0.1:8000/photos - Returns all photos as a list of JSON objects

### PUT:

#### http://127.0.0.1:8000/update/{photoId} - Updates photo attributes of an ID specified in URL with values specified in body

JSON body is the same as in POST request:

```
{
    "albumId": 3,
    "title": "quidem ut quos non qui debitis exercitationem"
}
```

### DELETE:

#### http://127.0.0.1:8000/delete/{photoId} - Deletes photo of an ID specified in URL






