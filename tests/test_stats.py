# coding: utf-8

import  os
from tests.shared import  getEmptyDeck

def test_stats():
    d = getEmptyDeck()
    f = d.newNote()
    f['Front'] = "foo"
    d.addNote(f)
    c = f.cards()[0]
    # card stats
    assert d.cardStats(c)
    d.reset()
    c = d.sched.getCard()
    d.sched.answerCard(c, 3)
    d.sched.answerCard(c, 2)
    assert d.cardStats(c)

def test_graphs_empty():
    d = getEmptyDeck()
    assert d.stats().report()

def test_graphs():
    from anki import Collection as aopen
    d = aopen(os.path.expanduser("~/test.anki2"))
    g = d.stats()
    rep = g.report()
    open(os.path.expanduser("~/test.html"), "w").write(rep)
    return
