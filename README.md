# tzinfo
Actual code behind the blog post: http://www.pavelgurenko.com/2017/05/getting-posix-tz-strings-from-olson.html

Olson tzdata to JSON of POSIX TZ strings builder

build_tzinfo.py gets the latest tzdata from IANA, builds it, extracts the POSIX TZ strings and writes the resulting JSON to tzinfo file.
