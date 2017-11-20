class Movie():
    """The class Movie contains the attributes for a movie

    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """The __init__ method is used to instantiate movie objects

        Args:
            title (str): Movie title of movie object.
            poster_image_url (str): URL for poster image of movie object.
            trailer_youtube_url (str): URL for trailer of movie object.

        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
