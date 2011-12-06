"""
Class: Storage()
This class can do:
    - caching the data (not implemented yet)
    - inseting the data into the local DB file
    - getting the data from the local DB file.
"""
# $Id: Storage.py,v 1.11 2011-11-20 20:45:31 ruslan Exp $

#import shelve
import pickle
import re
from operator import itemgetter, attrgetter
from Movie import Movie
from Utils import new_id

DBFILE = 'movie.db'

class Storage(object):
    def __init__(self):
        """
        Simple constructor
        """
        self.dbfile = DBFILE

    def store(self, movie):
        """
        store - method to convert each record into the Movie object
                and store it into a pickle file
        """
        try:
            #s_data = shelve.open(self.dbfile, writeback=True)
            p_file = open(self.dbfile, 'w')
            tmp_dict = {}
            for k in movie.keys():
                m_obj = Movie(movie[k]['title'], movie[k]['release_year'],
                        movie[k]['stars'], movie[k]['format'])
                tmp_dict[k] = m_obj
            pickle.dump(tmp_dict, p_file)
            p_file.close()
            print 'File has been imported sucessfully into: %s' % (self.dbfile)
        except IOError, err:
            print err

    def save(self, data):
        """
        save - method to save the data to the pickle file
        """
        try:
            p_file = open(self.dbfile, 'w')
            pickle.dump(data, p_file)
            p_file.close()
        except IOError, err:
            print err


    def retrieve(self):
        """
        retrieve - method to get data from the pickle file
        """
        try:
            #s_data = shelve.open(self.dbfile)
            p_file = open(self.dbfile, 'r')
            s_data = pickle.load(p_file)
            p_file.close()
            return s_data
        except IOError, err:
            print err

    def del_record(self, m_id):
        """
        del_record - method to delete a record by id
        """
        m_db = self.retrieve()
        del(m_db[m_id])
        self.save(m_db)
        print "Deleted record ID: %d" % m_id


    def add_record(self, record):
        """
        add_record - method to add a new record to movie library
        """
        data = {}
        tmp_list = record.split(';')

        for i in tmp_list:
            r_key, r_val = i.split('=')

            key, val = {
                'y': lambda x : ('release_year', int(x)),
                's': lambda x : ('stars', [ n.strip() for n in x.split(',') ]),
                't': lambda x : ('title', x),
                'f': lambda x : ('format', x),
            }[r_key](r_val)

            data[key] = val

        n_id = new_id(self.retrieve())
        movie = Movie(data['title'], data['release_year'], data['stars'], data['format'])
        m_db = self.retrieve()
        m_db[n_id] = movie
        self.save(m_db)

        print "New record has been saved under ID: %d" % n_id
        print movie


    def get_movie_by_id(self, m_id):
        """
        get_movie_by_id - method to get a movie by id
        """
        m_db = self.retrieve()
        try:
            print m_db[m_id]
        except KeyError:
            print "It looks like ID %d has been deleted or it does not exist" % m_id


    def get_list_by(self, key):
        """
        get_list_by - generic method to get list of movies by key
        """
        m_db = self.retrieve()
        m_list = []

        for k in m_db.keys():
            m_list.append([ k, m_db[k].__getattribute__(key) ])

        m_list = sorted(m_list, key=itemgetter(1))

        for i in m_list:
            key = key.replace('_', ' ').capitalize()
            print '-' * 70
            print "ID: %d\n%s: %s" % (i[0], key, str(i[1]))
            if key == 'Release year':
                print "Title: %s" % m_db[i[0]].title


    def find_by(self, substr, key):
        """
        find_by - generic method to find movie/movies by key
                  using a substring
        """
        m_db = self.retrieve()
        s_list = []

        for k in m_db.keys():
            if isinstance(m_db[k].__getattribute__(key), list):
                for i in m_db[k].__getattribute__(key):
                    if re.search(substr, i, re.IGNORECASE):
                        s_list.append([ i, m_db[k].title ])
            elif isinstance(m_db[k].__getattribute__(key), str):
                if re.search(substr, m_db[k].__getattribute__(key), re.IGNORECASE):
                    s_list.append([ m_db[k].__getattribute__(key), 'ID:' + str(k) ])
            elif isinstance(m_db[k].__getattribute__(key), int):
                if substr == m_db[k].__getattribute__(key):
                    s_list.append([ m_db[k].__getattribute__(key), m_db[k].title ])

        if len(s_list):
            print "Found movie(s) by '%s' attribute:" % key.replace('_',' ').capitalize()
            for i in s_list:
                print "\t- %s [%s]" % (i[0], i[1])
        else:
            print 'Nothing was found.'


    def import_file(self, fname):
        """
        import_file - method to get the data from the source file
        """
        data = {}
        index = 0
        tmp_list = []

        try:
            for line in open(fname, 'r').readlines():
                line = line.strip()
                if len(line):
                    tmp_list.append(line)

            while tmp_list:
                data[index] = {}

                title = tmp_list.pop(0).split(':')
                r_year = tmp_list.pop(0).split(':')
                m_format = tmp_list.pop(0).split(':')
                stars = tmp_list.pop(0).split(':')

                if len(title) == 2:
                    data[index][title[0].lower()] = title[1].strip()
                else:
                    data[index][title[0].lower()] = ":".join(title[1:])

                data[index][r_year[0].replace(' ', '_').lower()] = int(r_year[1])
                data[index][m_format[0].lower()] = m_format[1].strip()
                data[index][stars[0].lower()] = [ x.lstrip() for x in stars[1].split(',') ]

                index += 1

            self.store(data)

        except IOError, err:
            print err
