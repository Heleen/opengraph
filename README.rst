OpenGraph is a module of python for parsing the Open Graph Protocol, you can read more about the specification at http://ogp.me/

.. note:: Added functionality: parsing of Twitter metatags (e.g. ``<meta value="https://www.youtube.com/embed/IZdR2bK7jOw" name="twitter:player">``). This was added for video embedding support. Works with Youtube and Vimeo videos and possibly others.

Installation
=============

pip install ogp

Features
=============

* Use it as a python dict
* Input and parsing from a specific url
* Input and parsing from html previous extracted
* HTML output

Usage
==============

**From an URL**

>>> import ogp
>>> video = ogp.OpenGraph(url="http://www.youtube.com/watch?v=q3ixBmDzylQ")
>>> video.is_valid()
True
>>> for x,y in video.items.items():
...     print "%-15s => %s" % (x, y)
... 
site_name       => YouTube
description     => Eric Clapton and Paul McCartney perform George Harrison's "While My Guitar Gently Weeps" at the...
title           => While My Guitar Gently Weeps
url             => http://www.youtube.com/watch?v=q3ixBmDzylQ
image           => http://i2.ytimg.com/vi/q3ixBmDzylQ/default.jpg
video:type      => application/x-shockwave-flash
site            => @youtube
video:height    => 360
player=> https://www.youtube.com/embed/q3ixBmDzylQ
video           => http://www.youtube.com/v/q3ixBmDzylQ?version=3&autohide=1
video:width     => 640 
type            => video
card            => player

site, player and card are from the new Twitter metatag parsing.

**From HTML**

>>> HTML = """
... <html xmlns:og="http://ogp.me/ns#">
... <head>
... <title>The Rock (1996)</title>
... <meta property="og:title" content="The Rock" />
... <meta property="og:type" content="movie" />
... <meta property="og:url" content="http://www.imdb.com/title/tt0117500/" />
... <meta property="og:image" content="http://ia.media-imdb.com/images/rock.jpg" />
... </head>
... </html>
... """
>>> movie = ogp.OpenGraph() # or you can instantiate as follows: opengraph.OpenGraph(html=HTML)
>>> movie.parser(HTML)
>>> video.is_valid()
True
