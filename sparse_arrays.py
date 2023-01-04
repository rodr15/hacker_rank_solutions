def matchingStrings(strings, queries):
    results = []

    for index_query,query in enumerate(queries):
        results.append(0)
        for string in strings:
            if( query == string ):
                results[index_query] += 1
                
    return results

if __name__ == '__main__':
    strings = ['aba','baba','aba','xzxb']
    queries = ['aba','xzxb','ab']

    print(matchingStrings(strings,queries))