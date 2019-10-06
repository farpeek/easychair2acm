# easychair2acm
Python script to convert easy chair conference data to ACM processing metadata requirements

EasyChair is a conference management system  https://easychair.org with >21millon accesses per month
ACM Association for Computing Machinery https://www.acm.org is a 72 years old scientific organization with over 100,000 members and a major customer of easychair.

This python script is for conference program chairs who want to automatically converts author, sumbission data into the following ACM publishing process' metadata format,

content type - full paper, short paper, or abstract
title
author / affiliation list (see below)
email list (see below)
submission ID

Authors and affiliations are separated by semi-colons, with affiliations in parentheses:
  Alan Smithie (University of Lanark);Hamilton Armstrong (Woodpark University)
E-mail addresses are in the same order as authors and separated by semi-colons:
  a.smithie@gmail.com;h.armstrong@outlook.com

Without having to pour through all authors and submission data.

Steps:

1 - In chair role, click administration tab, then conference data download the xls data file
2 - In excel or other, export the Submissions sheet with accepted articles to accepted.csv
3 - In excel or other, export the Authors sheet to authors.csv
4 - Run easychair2acm.py > myconference.acm.metadata

Author name matching automates processing the combined author list sentence, into separated metadata per author, crosschecked with the author database.

Friends of easychair2acm

https://github.com/alexorso/easychairscripts
https://github.com/nblomqvist/easy2acl

MIT License

Copyright 2019 farpeek

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

