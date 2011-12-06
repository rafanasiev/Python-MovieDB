"""
Class: Movie( title, release_year, stars, format)
Each movie object has a title, release year, list of stars and format
"""
# $Id: Movie.py,v 1.3 2011-11-13 21:44:24 ruslan Exp $

class Movie(object):
    def __init__(self, title, release_year, stars, format):
        """
        Movie takes four arguments to its constructor.
        All the arguments are required.
        NOTE: stars is a list of movie's star []
        """
        self.title = title
        self.release_year = release_year
        self.stars = stars
        self.format = format

    def set_title(self, title):
        """
        setTitle - simple accessor method
        """
        self.title = title

    def set_release_year(self, release_year):
        """
        setReleaseYear - simple accessor method
        """
        self.release_year = release_year

    def set_stars(self, stars):
        """
        setStars - simple accessor method
        """
        self.stars = stars

    def set_format(self, format):
        """
        setFormat - simple accessor method
        """
        self.format = format

        # Overload print operation, print a specific format for movie.
    def __str__(self):
        s  = "=======================================================\n"
        s += "* Title: " + self.title + "\n"
        s += "* Release Year: " + str(self.release_year) + "\n"
        s += "* Stars:\n"
        for star in self.stars:
            s += "\t- " + star + "\n"
        s += "* Format: " + self.format + "\n"
        s += "=======================================================\n"
        return s
