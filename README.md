# PruebaXa
This is just the mandatory part of the sent test, I have decided to do it in FastAPI.
- so first you go to the terminal and you have to create an environment - then you install the requirements file using  "pip install -r requirements.txt" command.
- finally, you turn on the server using "uvicorn main:app --reload" command
I have created 5 endpoints and I recommend, first of all, go to the endpoint "localhost:8000/update" because this download from the given link the .Json file to work.

there are another 4 endpoints:
- "localhost:8000/search" -> An endpoint that provides a search lookup within the tracks, you can do the search by position in the top, by track name, and also by track apple id.
It works through a path query so you will use this kind of endpoint:
*"http://127.0.0.1:8000/search?top=3"
*"http://127.0.0.1:8000/search?id=1603748478"
*"http://127.0.0.1:8000/search?name=poochie%20gown"
-"http://127.0.0.1:8000/top50" -> An endpoint that allows getting the top 50 popularity tracks.
-"http://127.0.0.1:8000/deleteItem" -> An endpoint that removes a track, using the top position and it works also through a path query so the endpoint could look like: "http://127.0.0.1:8000/deleteItem?top=99" 
-"http://127.0.0.1:8000/addSong" ->An endpoint that adds a new track through a Body query that has to have the next structure:
{
  "artistName": "string",
  "id": "string",
  "name": "string",
  "releaseDate": "string",
  "kind": "string",
  "artistId": "string",
  "artistUrl": "string",
  "contentAdvisoryRating": "string",
  "artworkUrl100": "string",
  "genres": {
    "genreId": "string",
    "name": "string",
    "url": "string"
  },
  "url": "string"
}
Inside the folder, you will find 3 .py files:
-dataManagement.py -> where are the functions that interact whit the .json file.
-models.py -> It is a file that provides models for the add function.
-main.py -> where are the functions wiht his decorators that create the endpoints. 
