from assignment3 import Ranking

def main():
    judgementFilePath = "relevance_judgements-v1.txt"
    queryFilePath = "sample.txt"

    ranking = Ranking(judgementFilePath)
    queryFile = open(queryFilePath, "r")
    queries = queryFile.readlines()

    line = int(input("line: ")) - 1
    thresh = int(input("thresh: "))
    
    print("rel: " + str(ranking.prec(queries[line], thresh)))
    print("recall: " + str(ranking.recall(queries[line], thresh)))
    print("f1: " + str(ranking.f1_score(queries[line], thresh)))
    print("rr: " + str(ranking.rr(queries[line], thresh)))
    print("ndcg: " + str(ranking.ndcg(queries[line])))
    

if __name__ == "__main__":
    main()
