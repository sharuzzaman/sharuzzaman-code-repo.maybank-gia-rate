#!/usr/bin/python

# Maybank Gold Investment Account price scraper
# Using BeautifulSoup package
# Developed and tested on Debian Testing (Jessie)
# Initial development 25 July 2012 

# Copyright (C) 2012,2013 Sharuzzaman Ahmat Raslan (sharuzzaman@gmail.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import urllib2
from BeautifulSoup import BeautifulSoup
import datetime

website=urllib2.urlopen('http://www.maybank2u.com.my/mbbfrx/gold_rate.htm')
data=website.read()

soup = BeautifulSoup(data)

date=soup('td')[31].string
selling=soup('td')[32].string
buying=soup('td')[33].string

print "%s,%s,%s" % (date,selling,buying)
