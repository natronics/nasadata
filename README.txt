=========
NASA Data
=========

The nasadata package provides tools for scraping publicly availible
spaceflight data from NASA into python objects for scripting. Might
work like this::

    #!/usr/bin/env python

    from nasadata import isstle

    tle = isstle.get_current_tle()
    print "ISS orbit Eccentricity:", tle.e
