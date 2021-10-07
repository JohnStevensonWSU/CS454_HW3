import math

class Ranking(object):
    """docstring for Ranking"""

    def __init__(self, judgement_file):
        judgementFile = open(judgement_file, "r")
        lines = judgementFile.readlines()
        self.judgements = {}
        self.queryResults = {}
        query = ""
        results = []
        for line in lines:
            judgement = line.split()
            if judgement[0] != query:
                self.queryResults[query] = results
                results = []
                query = judgement[0]
            self.judgements[judgement[0],judgement[1]] = judgement[2]
            results.append(judgement[1])
        judgementFile.close()

    def prec(self, query_line, thresh):
        line = query_line.split()
        query = line[0]
        cookie = line[1]
        timestamp = line[2]
        urls = line[3 : 13]
        rel = 0
        for url in urls:
            if self.judgement(query, url, thresh):
                rel += 1
        return rel / 10

    def recall(self, query_line, thresh):
        line = query_line.split()
        query = line[0]
        cookie = line[1]
        timestamp = line[2]
        urls = line[3 : 13]
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
            
    def rr(self, query_line, thresh):
        line = query_line.split()
        query = line[0]
        cookie = line[1]
        timestamp = line[2]
        urls = line[3 : 13]
        result = 0
        for url in urls:
            result += 1
            if self.judgement(query, url, thresh):
                return 1 / result
        return 0

    def f1_score(self, query_line, thresh):
        pass

    def ndcg(self, query_line):
        pass

    def judgement(self, query, url, thresh):
        try:
            if int(self.judgements[query,url]) >= thresh:
                return True
        except:
            return False
