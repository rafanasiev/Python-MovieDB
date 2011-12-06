# $Id: unittests_movie.py,v 1.3 2011-11-20 21:16:46 ruslan Exp $

import unittest
import sys
sys.path.append('../')
from Movie import Movie


class testMovie(unittest.TestCase):
    """
    testMovie - a test class to test Movie module
    """
    title = 'Men in Black'
    year = 1997
    stars = ['Tommy Lee Jones', 'Will Smith']
    format = 'DVD'
    dbfile = 'movie.db'
    src_file = 'sample_movies.txt'

    def setUp(self):
        """
        setUp - set up data used for the test.
        """
        self.movie = Movie(title, year, stars, format)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(testMovie))
        return suite

if __name__ == '__main__':
    #testSuite = Movie('Men in Black', 1997, ['Tommy Lee Jones', 'Will Smith'], 'DVD')
    #suite = unittest.TestSuite()
    unittest.main()
