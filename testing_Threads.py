from threading import Thread


def do_this():
    answer = (2**10 -(6*40) *-90)
    print(answer)

def do_that():
    answer = (2**10 -(6*40) *-80)
    print(answer)



t1 = Thread(target=do_this)

t2 = Thread(target=do_that)

t1.start()
t2.start()
