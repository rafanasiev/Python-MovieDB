"""
Class: Prompt()
This class provides an ability to build
interactive text based menu for an user.
"""

# $Id: Prompt.py,v 1.3 2011-11-20 20:45:31 ruslan Exp $

import sys

ACTIONS = ('a','d','p','n','t','s','y','q')

class Prompt(object):
    def __init__(self):
        pass

    def do_menu(self, mdb):
        """
        do_menu - method to build menu and run an appropriate user's action
        """

        while True:
            action = raw_input(self.show_interface())

            if action not in ACTIONS:
                print 'ERROR: invalid menu option!'
                action = raw_input("Please, input again: ?\b")

            if action == 'q' or action == 'Q':
                sys.exit(0)
            elif action == 'p' or action == 'P':
                m_id = input("Please, enter movie ID: ?\b")
                mdb.get_movie_by_id(m_id)
            elif action == 'd' or action == 'D':
                m_id = input("Please, enter movie ID: ?\b")
                mdb.del_record(m_id)
            elif action == 'a' or action == 'A':
                print "To add new record, use this format:"
                print 'y=YYYY;t=The Movie;f=DVD;s=John Doe,Jack Lee'
                record = raw_input("Please, enter new record: ?\b")
                mdb.add_record(record)
            elif action == 't' or action == 'T':
                mdb.get_list_by('title')
            elif action == 'y' or action == 'Y':
                mdb.get_list_by('release_year')
            elif action == 'n' or action == 'N':
                substr = raw_input("Please, enter substring to find movie by title: ?\b")
                mdb.find_by(substr, 'title')
            elif action == 's' or action == 'S':
                substr = raw_input("Please, enter substring to find movie star: ?\b")
                mdb.find_by(substr, 'stars')


    def show_interface(self):
        """
        show_interface - text based user menu
        """
        return """
=================================
 *** Movie DB user interface ***
=================================
Select one of:
a - Add new movie's record
d - Delete movie's record
p - Show movie properties
t - List movies by title
y - List movies by year
n - Find movie by title's name
s - Find movie by star
q - Exit
=================================
Your choice: ?\b"""

