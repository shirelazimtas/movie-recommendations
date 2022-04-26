import wikipedia


def stringToList(string):
    listRes = list(string.split(" "))
    return listRes

# return information from  wikipedia for the movies

def wikipedia_data(jeans):
    try:
        data = wikipedia.summary(jeans, sentences=3)
        list_wiki = stringToList(data)
    except wikipedia.exceptions.DisambiguationError as exe:
        list_wiki = stringToList('add the word film to your search')
    except wikipedia.exceptions.PageError as ex:
        list_wiki = stringToList(
            'Page name ' + jeans + ' does not match any pages. Try another name!')
    except:
        list_wiki = stringToList("try again")
    return list_wiki
