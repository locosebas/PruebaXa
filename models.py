#Pydantic
from pydantic import BaseModel, Field 

class Generes(BaseModel):
    genreId: str = Field(..., examlpe="18")
    name:  str = Field(..., examlpe="Hip-Hop/Rap")
    url:  str = Field(..., examlpe="https://itunes.apple.com/us/genre/id18")


class SongBase(BaseModel):
    artistName : str = Field(..., examlpe= "Drake")
    id: str = Field(..., examlpe="1584281784")
    name: str = Field(..., examlpe= "No Friends In The Industry")
    releaseDate:str = Field(..., examlpe= "2021-09-03")
    kind:str = Field(..., examlpe= "songs")
    artistId: str = Field(..., examlpe= "271256")
    artistUrl: str = Field(..., examlpe="https://music.apple.com/us/artist/drake/271256")
    contentAdvisoryRating:str = Field(..., examlpe= "Explict")
    artworkUrl100:str = Field(..., examlpe= "https://is4-ssl.mzstatic.com/image/thumb/Music115/v4/11/36/38/1136384a-eebc-697a-c005-d890e41c0854/21UM1IM07518.rgb.jpg/100x100bb.jpg")
    genres: Generes = Field(...)
    url:str = Field(..., examlpe= "https://music.apple.com/us/album/no-friends-in-the-industry/1584281467?i=1584281784")




    