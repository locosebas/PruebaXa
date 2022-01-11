#python

from typing  import Optional

#FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import Body, Query

import dataManagement as dbm
from models import Generes, SongBase




app = FastAPI()



@app.get(
    path="/search",
    status_code=status.HTTP_200_OK
    )
def search(

    top: Optional[int] = Query(
        None,
        title= "song id",
        description="song id",
        example=3
    ),

    id: Optional[str] = Query(
        None,
        title= "song id",
        description="song id",
        example='1603748478'
        ),
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=100,
        title="song Name",
        description="This is the song name. ",
        example="poochie gown"

    #     ),
    # artistName: Optional[str] = Query(
    #     None,
    #     min_length=1,
    #     max_length=50,
    #     title="artist Name",
    #     description="This is the artist name. ",
    #     example="Gunna"

        )
    
    ):
    if id:
        return dbm.getById(id)
    elif name:
        return dbm.getByname(name)
    elif top:
        return dbm.getByTop(top)

@app.get(
    path="/top50",
    status_code=status.HTTP_200_OK
    )
def top50():
    return dbm.top50()

@app.post(
     path="/deleteItem",
     status_code=status.HTTP_200_OK
     )
def deleteItem(
    top: Optional[int] = Query(
        None,
        title= "song id",
        description="song id",
        example=99
    )
    ):
    if dbm.deleteByTop(top):
        a = "succesfully delleted"
    else:
        a = "the item do not exist"
    return {'answer': a}

@app.post(
    path="/addSong"
    )
def addSong(
    song: SongBase= Body(...)
    ):
    songD = dict(song)
    songD["genres"]=dict(songD["genres"])
    return dbm.addItem(songD)
    #return songD
    
@app.post(
    path="/update"
)
def update():
    return dbm.update()
