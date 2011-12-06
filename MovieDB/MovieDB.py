"""
Class: MovieDB()
A generic class to coordinate the actions
to manage movie library
"""
# $Id: MovieDB.py,v 1.11 2011-11-20 20:45:20 ruslan Exp $

import sys
sys.path.append('lib')

from Storage import Storage
from Prompt import Prompt

class MovieDB(Storage, Prompt):
    def __init__(self):
        super(MovieDB, self).__init__()
        #self.storage = Storage()

    def dispatcher(self, action, arg=None):
        """
        dispatcher - a generic method to handle user interface events
        """
        # a 'jump-table' to operate the actions
        actions = {
                'add': lambda x: self.add_record(x),
                'del': lambda x: self.del_record(x),
                'import': lambda x: self.import_file(x),
                'property': lambda x: self.get_movie_by_id(x),
                'year_list': lambda : self.get_list_by('release_year'),
                'title_list': lambda : self.get_list_by('title'),
                'find_by_title': lambda x: self.find_by(x, 'title'),
                'find_by_star': lambda x: self.find_by(x, 'stars'),
                'find_by_year': lambda x: self.find_by(x, 'release_year'),
                'menu': lambda x: self.do_menu(x),
        }

        if actions.has_key(action):
            if arg:
                return actions[action](arg)
            else:
                return actions[action]()
        else:
            return 'Unknown action'
