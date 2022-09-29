from functools import wraps
import time
import matplotlib.pyplot as plt

valores = [1,10**1,10**2,10**3,10**4,10**5,10**6,10**7,10**8,10**9]
tiempos1 = []
tiempos2 = []


#decorador para calcular la funcion tiempo en suma1
# bibliografia https://dev.to/kcdchennai/python-decorator-to-measure-execution-time-54hk
def timeit1(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time  
        tiempos1.append(total_time)      
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.10f} seconds')
        return result
    return timeit_wrapper

#decorador para calcular la funcion tiempo en suma2
def timeit2(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time  
        tiempos2.append(total_time)      
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.10f} seconds')
        return result
    return timeit_wrapper


@timeit1
def sum1(n):                                                             #costo         veces
    total = 0  # declarar una variable cuesta una operacion              #1             1
    for i in range(1, n+1):  # una variable que se va a llamar N veces   #2             n
        total += i  #sumatoria de loa valores N veces                    #2             n
    return total # declaracion de otra variable de operacion             #1             1 
                                                                         #T(n) = 1 + 2n + 2n + 1
                                                                         #T(n) = 4n + 2             #funcion lineal
                                                                         
    #T1(n) = 2c + (c1 + c2)n
    #caso promedio es 10^5
    #T1(n) = 0 + (10^5 + 10^5)n
    # 0 + (10^5 + 10^5)n = 0.0052919000
    # T(n) = 2.64595e-8(n)
    # T(n) = 2.64595e-8(n) * 10^5
    # T(n) = 0.00264595 segundos


@timeit2
def sum2(n):                                                            #costo          #veces
    total = n*(n+1)//2  # declaracion de una variable = n * (n)/2       #4              #1 
    return total #declaracion de una variable                           #1              #1
                                                                        #T(n) = 4 + 1      #funcion constante
#T(n) = 5   es una constante                                                                        
#T(n) = K     



if __name__ == '__main__':
    for i in valores:
       
        sum1(i)
        
        sum2(i)
    print(len(tiempos1))
    print(len(tiempos2))   
    print(len(valores))  
    plt.plot(valores,tiempos1,'r',marker = '*')  #rojo sumatoria1
    plt.xlim([0, valores[-1]])
    plt.ylim([0, tiempos1[-1]])
    plt.plot(valores,tiempos2,'g',marker = '.')  #verde sumatoria2  
    plt.grid() 
    plt.show()


