import matplotlib.pyplot as plt
n = [1000,2000,4000,8000,16000,32000,64000]
t = [0.0,0.02,0.2,0.6,2.6,10.4,41.6]

plt.plot(n,t)

plt.show()


#si crece rapido la funcion al inicio y luego se estabiliza, lo mas probable es que sea una funcion logaritmica  