#!/usr/bin/python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------
# moviedb.py - TextUserInterface tool to manage your movies
#
# $Id: moviedb.py,v 1.14 2011-11-20 20:45:24 ruslan Exp $
# ----------------------------------------------------------

import argparse
import sys
sys.path.append('../lib')
sys.path.append('..')
from MovieDB import MovieDB
mdb = MovieDB()

def main():
    p = argparse.ArgumentParser(
        description="moviedb.py - TUI tool to manage the movies library",
    )
    p.add_argument("--import", "-i", action="store", dest="file",
            type=str, help="import data from a txt file")
    p.add_argument("--add", "-a", action="store", dest="add_rec",
            type=str, help="""add a record. The format of the record should as:
            'y=YYYY;t=The Movie;f=DVD;s=John Doe,Jack Lee'""")
    p.add_argument("--delete", "-d", action="store", dest="del_id",
            type=int, help="delete a record by id")
    p.add_argument("--property", "-p", action="store", dest="show_id",
            type=int, help="show properties of a record by id")
    p.add_argument("--title-list", "-t", action="store_true", dest="title_list",
            default=False, help="show records, alphabetically by title")
    p.add_argument("--year-list", "-y", action="store_true", dest="year_list",
            default=False, help="show records, chronologically by year")
    p.add_argument("--find-by-title", action="store", dest="title",
            type=str, help="find records by a title name")
    p.add_argument("--find-by-star", action="store", dest="star",
            type=str, help="find records by a star name")
    p.add_argument("--find-by-year", action="store", dest="year",
            type=int, help="find records by a year")
    p.add_argument("--menu", "-m", action="store_true", dest="menu",
            default=False, help="script will prompt interactive menu")
    p.add_argument("--version", "-v", action="version", version='%(prog)s 0.1a')

    arguments = p.parse_args()

    #print arguments
    #print 'dir arguments: ', dir(arguments)
    #print 'dict: ', arguments.__dict__

    if arguments.menu:
        mdb.dispatcher('menu', mdb)
    elif arguments.file:
        print 'Got file for import: ' + arguments.file
        mdb.dispatcher('import', arguments.file)
    elif arguments.del_id:
        mdb.dispatcher('del', arguments.del_id)
    elif arguments.add_rec:
        mdb.dispatcher('add', arguments.add_rec)
    elif arguments.year:
        print 'Looking for a movie by year: %d' % arguments.year
        mdb.dispatcher('find_by_year', arguments.year)
    elif arguments.show_id:
        print 'Got ID: ' + str(arguments.show_id)
        mdb.dispatcher('property', arguments.show_id)
    elif arguments.year_list:
        print 'Got list of the movies by release year:'
        mdb.dispatcher('year_list')
    elif arguments.title_list:
        print 'Got list of the movies by title:'
        mdb.dispatcher('title_list')
    elif arguments.title:
        print 'Looking for a movie by substring: %s' % arguments.title
        mdb.dispatcher('find_by_title', arguments.title)
    elif arguments.star:
        print 'Looking for a movie star by substring: %s' % arguments.star
        mdb.dispatcher('find_by_star', arguments.star)
    else:
        p.print_help()


if __name__ == '__main__':
    main()
