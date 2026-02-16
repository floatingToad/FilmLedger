# FilmLedger - Movie Commodity Database

## 1. Project Summary

We will design and implement a relational database system that treats movies as commodities by organizing them by genre, release year, and ratings. The system will support retrieval and update operations through a GUI, allowing users to add movies, assign genres, submit ratings, and filter movies by release year. The project will be implemented in a DBMS (MySQL/PostgreSQL) with a GUI that supports both retrieval and update operations.

## 2. Background and Motivation

We all agreed that movies are commodities—people consume them, evaluate them, compare them, and categorize them. We thought a movie database would be an effective project because it is realistic, intuitive, and naturally supports relational database concepts such as normalization, many-to-many relationships, and structured retrieval. This project allows us to demonstrate strong database design without requiring advanced programming skills, while still meeting all technical and academic requirements.

## 3. System Functions

### Retrieval
- Search movies by title
- Filter movies by genre
- Filter movies by release year
- View movie details, assigned genres, and ratings
- View average rating per movie

### Update
- Add and edit movies
- Add and manage genres
- Assign or remove genres from movies
- Add, update, or delete ratings

## 4. Database Design

### Table 1: Movies
- MovieID
- Title

### Table 2: ReleaseYears
- ReleaseYearID
- YearValue

### Table 3: Genres
- GenreID
- GenreName

### Table 4: Ratings
- RatingID
- MovieID
- Stars (1–5)
- RatedAt (Date/Time)

## 5. GUI Design

The GUI will include:
- Movie entry and edit forms
- Genre assignment interface
- Rating submission form
- Search and filter functionality by genre and release year
