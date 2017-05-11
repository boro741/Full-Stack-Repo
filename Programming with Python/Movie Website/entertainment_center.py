import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg?1493823258244",
                        "https://youtu.be/KYz2wyBy3kc")

# print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an Alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://youtu.be/5PSNL1qE6VY")

bahubali2 = media.Movie("Bahubali 2",
                        "Bahubali: The conclusion",
                        "http://stat2.bollywoodhungama.in/wp-content/uploads/2017/01/Bahubali-2-The-Conclusion-4.jpg",
                        "https://youtu.be/G62HrubdD6o")

life = media.Movie("Life",
                   "Life found on space",
                   "http://horrornews.net/wp-content/uploads/2017/03/l1-1.jpg",
                    "https://youtu.be/dgOGqWHtjP0")

dangal = media.Movie("Dangal",
                    "Former wrestler Mahavir Singh Phogat (Aamir Khan) trains young daughters Geeta (Fatima Sana Shaikh) and Babita (Sanya Malhotra) to follow in his footsteps and become world-class grapplers.",
                    "https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg",
                    "https://youtu.be/x_7YlGv9u1g")

#print(avatar.storyline)

#avatar.show_trailer()

movies = [toy_story, avatar, bahubali2, life, dangal]

fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
#print(media.Movie.__name__)

#print(media.Movie.__module__)
