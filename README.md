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
# example:
$ curl -i -H "Content-Type: application/json" -X POST -d "{\"albumId\": 3, \"title\": \"reiciendis et velit laborum recusandae\"}" http://127.0.0.1:8000/add

```

#### IMPORTANT: Because placeholder.com uses CloudFlare, access to photos can be denied. To work around this, changing settings of 'cloudscraper' in helpers.py on line 18 can be helpful. Below are possible values to cloudscraper's parameters:

![image](https://user-images.githubusercontent.com/78605465/198174928-07605555-a674-4244-bea6-6a1f01796a06.png)

#### http://127.0.0.1:8000/file/add - Uses local JSON file

```bash

# importing via CLI
$ curl -i -H "Content-Type: application/json" -X POST -d "{\"albumId\": 4, \"title\": \"eum laborum in sunt ea\"}" http://127.0.0.1:8000/file/add

```
JSON body stays the same

### GET:

#### http://127.0.0.1:8000/photos - Returns all photos as a list of JSON objects

#### http://127.0.0.1:8000/photos/{photoId} - Returns photo of an ID specified in URL


### PUT:

#### http://127.0.0.1:8000/update/{photoId} - Updates photo of an ID specified in URL with values specified in body

JSON body is the same as in POST request:

```
{
    "albumId": 3,
    "title": "quidem ut quos non qui debitis exercitationem"
}
```


### DELETE:

#### http://127.0.0.1:8000/delete/{photoId} - Deletes photo of an ID specified in URL






