# coding=utf-8
from time import time
import matplotlib
#this will prevent the figure from popping up
matplotlib.use('Agg')

from matplotlib import pyplot as plt
import numpy as np

#max_iters = cantidad de iteraciones que la funcion  Zn = Zn-1 ^2  + c iterara.
#width = la cantidad de numeros que queremos que haya en el plano real
#real_low = lower bound del plano real (x)
#real_high = upper bound del plano real(x)
#height = la cantidad de numeros que habran en el plano complejo.
#imag_high= upper bound de plano complejo(y)
#imag_low = lower bound de plano complejo(y)
def simple_mandelbrot(width, height, real_low, real_high, imag_low, imag_high, max_iters):
    #ACA EMPIEZA TAREA 0:
    #Necesitamos:       
    #            Load Arreglo real_vals
    #            Load array image vals
    #            Load mandelbrot_graph   
    #creamos el arreglo de valores de ambos planos, plano real es de tamano width y plano imaginario es de height
    real_vals = np.linspace(real_low, real_high, width)
    imag_vals = np.linspace(imag_low, imag_high, height)
        
    # we will represent members as 1, non-members as 0.
    # Creamos una matriz de 2d tamaño heightXwidth las filas siendo height, columnas siendo width y de tipo float32 
    mandelbrot_graph = np.ones((height,width), dtype=np.float32)
    
    #ACA EMPIEZA LA TAREA 3:
    #Necesitamos:  
    #            Arreglo real vals, image_val, max iters, width
    #Iniciamos un ciclo del tamano de la cantidad de columnas que hay en nuestra matriz.
    for x in range(width):
      #ACA EMPIEZA LA TAREA 2:
      #Necesitamos:
        #                            El arreglo de valores reales, 
        #                            El arreglo de valores imaginarios
        #                            numero max de iteraciones
        #                            valor de width          
        #Iniciamos otro ciclo con el tamano de la cantidad de filas que hay en nuestra matriz. 
        for y in range(height):
          #ACA EMPIEZA LA TAREA 1. 
          #Para la tarea 1 necesitamos:
          #                            El arreglo de valores reales, 
          #                            El arreglo de valores imaginarios 
          #                            numero de max iteraciones,
            #creamos el numero complejo C en base a los valores de real_vals e imag_vals
            c = np.complex64( real_vals[x] + imag_vals[y] * 1j  )
            #creamos un valor z que represante z0 en la funcion que Zn = Zn-1 ^2  + c        
            z = np.complex64(0)
            #En el siguiente ciclo vamos a empezar a iterar para determinar si el valor c pertenece al set de mandelbrot
            for i in range(max_iters):
                
                z = z**2 + c
                #sacamos el valor absoluto de Z, si es mayor que 2, no converge y en la matriz de mandelbrot colocamos un 0 en esa posicion de (y,x) 
                if(np.abs(z) > 2):
                    mandelbrot_graph[y,x] = 0
                    break
   #Tarea final NECSITAMOS: 
   #                        mandelbrot_graph.             
    return mandelbrot_graph


if __name__ == '__main__':
    
    t1 = time()
    mandel = simple_mandelbrot(512,512,-2,2,-2,2,256)
    t2 = time()
    mandel_time = t2 - t1
    
    t1 = time()
    fig = plt.figure(1)
    plt.imshow(mandel, extent=(-2, 2, -2, 2))
    plt.savefig('mandelbrot.png', dpi=fig.dpi)
    t2 = time()
    
    dump_time = t2 - t1
    
    print 'It took {} seconds to calculate the Mandelbrot graph.'.format(mandel_time)
    print 'It took {} seconds to dump the image.'.format(dump_time)