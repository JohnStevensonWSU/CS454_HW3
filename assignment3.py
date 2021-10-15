import math


# Ranking performs various ranking methods for query optimization.
# Must be given a judgement file which contains columns of values
# separated by a single space. Most functions require a query_line
# from 'sample.txt' file containing anonymized Yahoo query data and
# a score threshold to judge the relevancy of a url.
# prec - returns the precision
# recall - returns the recall
# rr - returns the reciprocal rank
# f1_score - returns the f1 score
# ndcg - returns ndcg
class Ranking(object):
    """docstring for Ranking"""

    def __init__(self, judgement_file):
        judgementFile = open(judgement_file, "r")
        lines = judgementFile.readlines()
        self.judgements = {}
        self.queryResults = {}
        query = ""
        results = []
        # parse judgement file for query, url judgement scores
        for line in lines:
            judgement = line.split()
            if judgement[0] != query:
                self.queryResults[query] = results
                results = []
                query = judgement[0]
                self.judgements[query] = {}
            self.judgements[judgement[0]][judgement[1]] = judgement[2]
            results.append(judgement[1])
        judgementFile.close()

    # Returns the precision of a query
    def prec(self, query_line, thresh):
        line = query_line.split()
        query = line[0]
        cookie = line[1]
        timestamp = line[2]
        urls = line[3: 13]
        rel = 0
        for url in urls:
            if self.judgement(query, url, thresh):
                rel += 1
        return rel / 10

    # Returns the recall of a query
    def recall(self, query_line, thresh):
        line = query_line.split()
        query = line[0]
        cookie = line[1]
        timestamp = line[2]
        urls = line[3: 13]
        rel = 0
        total = 0
        for url in urls:
            if self.judgement(query, url, thresh):
                rel += 1
        urls = self.queryResults[query]
        for url in urls:
            if self.judgement(query, url, thresh):
                total += 1
        try:
            return rel / total
        except:
            return 0

    # Returns the reciprocal rank of a query
    def rr(self, query_line, thresh):
        line = query_line.split()
        query = line[0]
        cookie = line[1]
        timestamp = line[2]
        urls = line[3: 13]
        result = 0
        for url in urls:
            result += 1
            if self.judgement(query, url, thresh):
                return 1 / result
        return 0

    # Returns the f1 score of a query
    def f1_score(self, query_line, thresh):
        alpha = 0.5
        prec = self.prec(query_line, thresh)
        recall = self.recall(query_line, thresh)

        try:
            return 1 / ((alpha * (1 / prec)) + ((1 - alpha) * (1 / recall)))
        except:
            return 0

    # Returns the ndcg of a query
    def ndcg(self, query_line):
        line = query_line.split()
        query = line[0]
        urls = line[3: 13]

        try:
            return self.dcg(query, urls) / self.idcg(query, urls)
        except:
            return 0

    # Returns true if the query, url judgement score is above the threshold
    def judgement(self, query, url, thresh):
        try:
            if int(self.judgements[query][url]) >= thresh:
                return True
        except:
            return False
        return False

    # Returns the dcg of a query
    def dcg(self, query, urls):
        count = 1
        score = 0

        for url in urls:
            try:
                score += int(self.judgements[query][url]) / math.log(1 + count, 2)
            except:
                pass
            count += 1
        return score

    # Returns the idcg of a query
    def idcg(self, query, urls):
        count = 1
        score = 0
        judgements = []

        optimal = self.judgements[query]
        for judgement in optimal.values():
            judgements.append(int(judgement))
        judgements.sort(reverse=True)

        for judgement in judgements:
            score += (judgement / math.log(1 + count, 2))
            count += 1
            if count > len(urls):
                break
        return score

# Main function to test Ranking class
def main():
    judgementFilePath = "relevance_judgements-v1.txt"
    queryFilePath = "sample.txt"

    ranking = Ranking(judgementFilePath)
    queryFile = open(queryFilePath, "r")
    queries = queryFile.readlines()

    while True:
        line = int(input("line: ")) - 1
        thresh = int(input("thresh: "))

        print("rel: " + str(ranking.prec(queries[line], thresh)))
        print("recall: " + str(ranking.recall(queries[line], thresh)))
        print("f1: " + str(ranking.f1_score(queries[line], thresh)))
        print("rr: " + str(ranking.rr(queries[line], thresh)))
        print("ndcg: " + str(ranking.ndcg(queries[line])))

if __name__ == "__main__":
    main()