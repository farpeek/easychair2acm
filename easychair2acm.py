import pandas

def splitAuthors(authorString):
    subauthors = authorString.replace(' and ',', ')
    subauthors = subauthors.split(', ')
    return [x for x in subauthors if "and" not in x]

def findAuthor(name, authors):
    for row in authors.iterrows():
        fname = row[1][1]
        sname = row[1][2]
        if name.startswith(fname) & name.endswith(sname):
            return row

authors = pandas.read_csv('authors.csv')
accepted = pandas.read_csv('accepted.csv')
accepted = accepted.applymap(lambda x: x.strip() if type(x)==str else x)
accepted['decision'] = accepted['decision'].apply(lambda x: x.replace('accept as ', '') if type(x)==str else x)
accepted['decision'] = accepted['decision'].apply(lambda x: x.replace('poster', 'abstract') if type(x)==str else x)
accepted = accepted[accepted['decision']!='reject']
accepted = accepted.sort_values('decision', ascending=False)
#print(accepted[['id','authors','decision']])
for submission in accepted.iterrows():
    subauthors=submission[1][2]
    authorlist = splitAuthors(subauthors)
    decision = submission[1][7]
    title = submission[1][1]
    sid = submission[1][0]
    print(decision,title,sid, sep=',')
    authorList = []
    for author in authorlist:
        authorRecord = findAuthor(author, authors)
        authorList.append(author + ' (' + str(authorRecord[1][5]) + ')')
    print(*authorList, sep=';')
    authorList = []
    for author in authorlist:
        authorRecord = findAuthor(author, authors)
        authorList.append(authorRecord[1][3])
    print(*authorList, sep=';')
    print()

        

