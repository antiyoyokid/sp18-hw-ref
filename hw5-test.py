from hw5 import *

def test_all():
    test_stack_push_with_size()
    test_stack_pop_and_peek()
    test_empty_stack_pop()
    test_queue_push_with_size()
    test_queue_pop_and_peek()
    test_empty_queue_pop()

# Begin testing stack
def test_stack_push_with_size():
    s = Stack()
    s.push(5)
    assert(s.size() == 1)
    s.push(7)
    s.push(9)
    assert(s.size() == 3)

def test_stack_pop_and_peek():
    s = Stack()
    s.push(11)
    peek = s.peek()
    data = s.pop()
    assert(peek == 11)
    assert(data == 11)
    s.push(13)
    s.push(15)
    data = s.pop()
    assert(data == 15)

def test_empty_stack_pop():
    s = Stack()
    assert(s.is_empty())
    assert(s.size() == 0)
    data = s.pop()
    assert(s.pop() == None)

# Begin testing queue
def test_queue_push_with_size():
    q = Queue()
    q.push(5)
    assert(q.size() == 1)
    q.push(7)
    q.push(9)
    assert(q.size() == 3)

def test_queue_pop_and_peek():
    q = Queue()
    q.push(11)
    peek = q.peek()
    data = q.pop()
    assert(data == 11)
    assert(peek == 11)
    q.push(13)
    q.push(15)
    data = q.pop()
    assert(data == 13)

def test_empty_queue_pop():
    q = Queue()
    assert(q.is_empty())
    assert(q.size() == 0)
    data = q.pop()
    assert(q.pop() == None)

test_all()