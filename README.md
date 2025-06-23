## Instant JSON Server

<p>Meant for developers who need to quickly wind up a server for a json file.
It creates all basic CRUD endpoints for each resource of a JSON file of your choice.
</p>

## To Install

<pre>pip install instant-json-server</pre>

## To use
<pre>instant-json-server path_to_your_json</pre>

## Example JSON File that works:
<pre>
  {
    "blogs": [
        {
            "id": 1,
            "content": "first blog"
        },
        {
            "id": 2,
            "content": "second blog"
        }
    ],
    "users": [
        {
            "id": "usr1",
            "username": "username1"
        },
        {
            "id": "usr2",
            "username": "username2"
        },
        {
            "id": 1233,
            "username": "asdasdad"
        },
        {
            "id": 12234234242433,
            "username": "asdasdad"
        }
    ]
}
</pre>
