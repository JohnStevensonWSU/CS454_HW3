from assignment3 import Ranking

def main():
    judgementFilePath = "relevance_judgements-v1.txt"
    queryFilePath = "sample.txt"

    ranking = Ranking(judgementFilePath)
    queryFile = open(queryFilePath, "r")
    queries = queryFile.readlines()

    line = int(input("line: "))
    thresh = int(input("thresh: "))
    
    print("rel: " + str(ranking.prec(queries[line], thresh)))
    print("recall: " + str(ranking.recall(queries[line], thresh)))
    print("rr: " + str(ranking.rr(queries[line], thresh)))
    

if __name__ == "__main__":
    main()
