from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, computed_field
from typing import Optional 

app = FastAPI() 

class Movies(BaseModel): 
  id: int = Field(gt=0)
  title: str = Field(min_length=1, max_length=200)
  director: str = Field(min_length=1, max_length=100)
  year: int = Field(ge=1900, le=2026)
  rating: float = Field(ge=1.0, le=10.0)

  @computed_field
  @property 
  def rating_category(self) -> str: 
    if self.rating >= 9.0:
      return "Excellent"
    elif self.rating >= 7.0:
      return "Good"
    elif self.rating >= 5.0:
      return "Average"
    else: return "Poor"
  
movies = [
  Movies(id = 1, title = "Space Jam", director = "Michael Jordan", year = 1984, rating = 6.6),
  Movies(id = 2, title = "Space Jam 2", director = "LeBron James", year = 2024, rating = 9.8),
  Movies(id = 3, title = "Weapons", director = "Julia Garner", year = 2026, rating = 8.2),
  Movies(id = 4, title = "Emoji Movie", director = "Chris Brown", year = 2018, rating = 4.4),
]

@app.get("/movies")
def get_movies(): return movies 

@app.get("/movies/search")
def search_movie(
  title: Optional[str] = None, 
  director: Optional[str] = None, 
  min_year: Optional[int] = None, 
  max_year: Optional[int] =  None, 
  min_rating: Optional[float] = None, 
  max_rating: Optional[float] = None 
):
  results = movies 

  if title: 
    results = [m for m in results if title.lower() in m.title.lower()]
  
  if director: 
    results = [m for m in results if director.lower() in m.director.lower()]

  if min_year: 
    results = [m for m in results if min_year <= m.year]

  if max_year: 
    results = [m for m in results if m.year <= max_year]

  if min_rating: 
    results = [m for m in results if min_rating <= m.rating]

  if max_rating: 
    results = [m for m in results if m.rating <= max_rating]
  
  return{
    "count": len(results),
    "movies": results
  }

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
  for movie in movies:
    if movie_id == movie.id: return movie 
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie ID not found")

@app.post("/movies", status_code=status.HTTP_201_CREATED)
def create_movie(new_movie: Movies):
  for movie in movies:
    if movie.id == new_movie.id:
      raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Movie ID {new_movie.id} has already been assigned.")
  
  movies.append(new_movie)
  return {"message": "Movie created", "movie": new_movie}

@app.put("/movies/{movie_id}")
def update_movie(movie_id: int, new_movie: Movies):
  if movie_id != new_movie.id:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"URL ID {movie_id} does not match Body ID {new_movie.id}")

  for i, movie in enumerate(movies):
    if movie.id == new_movie.id:
      movies[i] = new_movie 
      return {"message": "Movie updated", "movie": new_movie}
  
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie ID not found")

@app.delete("/movies/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_movie(movie_id: int):
  for i, movie in enumerate(movies):
    if movie.id == movie_id:
      movies.pop(i)
      return
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie ID not found")



  