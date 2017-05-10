from collections import defaultdict


def map_score(qids, labels, preds):
        qid2cand = defaultdict(list)
        for qid, label, pred in zip(qids, labels, preds):
                qid2cand[qid].append((pred, label))
        average_precs = []
        for qid, candidates in qid2cand.iteritems():
                average_prec = 0
                running_correct_count = 0
                for i, (score, label) in enumerate(sorted(candidates, reverse=True), 1):
                        if label > 0:
                                running_correct_count += 1
                                average_prec += float(running_correct_count) / i
                average_precs.append(average_prec / (running_correct_count + 1e-6))
        map_score = sum(average_precs) / len(average_precs)
        return map_score

def filter_all_same(qids, labels, preds):
        qid2cand = defaultdict(list)
        allpos = 0
        allneg = 0
        for qid, label, pred in zip(qids, labels, preds):
                qid2cand[qid].append((pred, label))
        for quid, candidate in qid2cand.iteritems():
                tot = sum(map(lambda x: x[1], candidate))
                if tot == 0:
                        pass
                elif tot==len(candidate):
                        for pred, label in candidate:
                                yield quid, label, float(pred)
                else:
                        for pred, label in candidate:
                                yield quid, label, float(pred)

def map_score_filtered(qids, labels, preds):
        qid2cand = defaultdict(list)
        for qid, label, pred in filter_all_same(qids, labels, preds):
                qid2cand[qid].append((pred, label))
        average_precs = []
        for qid, candidates in qid2cand.iteritems():
                average_prec = 0
                running_correct_count = 0
                for i, (score, label) in enumerate(sorted(candidates, reverse=True), 1):
                        if label > 0:
                                running_correct_count += 1
                                average_prec += float(running_correct_count) / i
                average_precs.append(average_prec / (running_correct_count + 1e-6))
        map_score = sum(average_precs) / len(average_precs)
        return map_score
