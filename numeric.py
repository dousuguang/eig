import numpy
import scipy.linalg
import scipy.sparse.linalg
import time
import matplotlib.pyplot as plt
 
m = numpy.loadtxt('Rosser.txt')
print m
 
funcdic = {0:('numpy.linalg.eig',numpy.linalg.eig,{}),
           1:('numpy.linalg.eigh',numpy.linalg.eigh,{}),
           2:('scipy.linalg.eig',scipy.linalg.eig,{}),
           3:('scipy.linalg.eigh',scipy.linalg.eigh,{}),
           4:('scipy.sparse.linalg.eigs',scipy.sparse.linalg.eigs,{}),
           5:('scipy.sparse.linalg.eigsh',scipy.sparse.linalg.eigsh,{}),
           6:('scipy.sparse.linalg.eigs, sigma=0',scipy.sparse.linalg.eigs,{'sigma':0}),
           7:('scipy.sparse.linalg.eigsh, sigma=0',scipy.sparse.linalg.eigsh,{'sigma':0})}
 
def timing_val(func):
    def wrapper(*arg, **kw):
        t1 = time.time()
        for i in range(0,1000):
            res = func(*arg, **kw)
        t2 = time.time()
        print '%40s  %.3e sec' % (funcdic[arg[0]][0], t2-t1)
        return [res,t2-t1]
    return wrapper
 
@timing_val
def test_func(i):
    name,func,args = funcdic[i]
    eigval,eigvec = func(m,**args)
    return numpy.real(numpy.sort(eigval))
 
def compare():
    Resultslist = []
    for i in range(0,8):
        try:
            Resultslist.append(test_func(i))
        except Exception as e:
            print type(e)
            print e
        continue
    return Resultslist
 
if __name__ == '__main__':
    Resultslist = compare()
 
    exact = [-1020.049018,0,0.098049,1000,1000,1019.901951,1020.000000,1020.049018]
 
    for i in range(0,8):
        name,func,args = funcdic[i]
        print '='*20
        print name
        for j in range(0,8):
            if j<len(Resultslist[i][0]):
                print '%20f,%20f'%(exact[j],Resultslist[i][0][j])
            else:
                print '%20f,'%(exact[j],)
        print '='*20
        print '\n\n'
 
    info = 'method index - details\n'
    for i in range(0,8):
        info = info + '%d - %s\n'%(i,funcdic[i][0])
 
    plt.figure()
    tt = [Resultslist[i][1] for i in range(0,8)]
    plt.bar(numpy.arange(0,8)-0.4, tt, width=0.8,alpha=0.6)
    plt.xticks(range(0,8),[str(i) for i in range(0,8)])
    plt.xlabel('method index',fontsize = 16)
    plt.ylabel('time (s)',fontsize = 16)
    plt.text(0,0.6,info,fontsize = 14)
    plt.show()
