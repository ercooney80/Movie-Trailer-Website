import fresh_tomatoes
import media

# Creating the Movie object instances using the Movie Class 
mean_girls = media.Movie("Mean Girls",
    "https://upload.wikimedia.org/wikipedia/en/a/ac/Mean_Girls_film_poster.png",  # NOQA
    "https://www.youtube.com/watch?v=KAOmTMCtGkI")

justice_league = media.Movie("Justice League",
    "https://upload.wikimedia.org/wikipedia/en/3/31/Justice_League_film_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=d2n-OZBwr6Q")

spiderman_homecoming = media.Movie("Spiderman: Homecoming",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=gDhTIY3LqSM")

the_emoji_movie = media.Movie("The Emoji Movie",
    "https://upload.wikimedia.org/wikipedia/en/6/63/The_Emoji_Movie_film_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=r8pJt4dK_s4")

war_for_the_planet_of_the_apes = media.Movie("War For The Planet Of The Apes",
    "https://upload.wikimedia.org/wikipedia/en/d/d7/War_for_the_Planet_of_the_Apes_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=qxjPjPzQ1iU")

rock_dog = media.Movie("Rock Dog",
    "https://upload.wikimedia.org/wikipedia/en/a/a1/Rock_Dog_2016_Teaser_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=UVwFM2PukSE")

logan = media.Movie("Logan",
    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=gbug3zTm3Ws")

get_out = media.Movie("Get out",
    "https://upload.wikimedia.org/wikipedia/en/e/eb/Teaser_poster_for_2017_film_Get_Out.png",  # NOQA
    "https://www.youtube.com/watch?v=sRfnevzM9kQ")

the_great_wall = media.Movie("The Great Wall",
    "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Great_Wall_%28film%29.png",  # NOQA
    "https://www.youtube.com/watch?v=6SKI9rgqFck")

# Creating the list of movies we will show on the page
movies = [mean_girls, justice_league, spiderman_homecoming,
          the_emoji_movie, war_for_the_planet_of_the_apes,
          rock_dog, logan, get_out, the_great_wall]

# Sending the movie list to build and display the page
fresh_tomatoes.open_movies_page(movies)
