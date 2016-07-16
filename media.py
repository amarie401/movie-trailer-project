import webbrowser
""" 

Class for representing a movie 
This class will be used in the entertainment_center.py file

"""

class Movie():
    def __init__(
        self, movie_title, movie_art, 
        movie_director, movie_actors, 
        movie_release_date, trailer_youtube):
        """ Inits a movie object
            Arguments:
                title = contains a string of the movie's title
                art = a string containing a URL to movie's poster image
                director = contains a string of the movie's director
                actors = a string of the featured actors
                release = an integer containing the movie's release date
                trailer = a string containing a URL to movie's trailer
         """
        self.title = movie_title
        self.art = movie_art
        self.director = movie_director
        self.actors = movie_actors
        self.release_date = movie_release_date
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)