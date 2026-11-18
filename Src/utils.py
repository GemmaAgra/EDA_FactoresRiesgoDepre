import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# import openpyxl



# A > estrés, > probabilidad de depresión   Correlación positiva (r > 0)  Espero una línea ascendente y una correlación positiva (r > 0)
# Representa los datos en un gráfico y muestra el coeficiente de correlación.
def hipotesis_H1(df):

    estres = df['estres']
    depre = df['depresion']
   
    r = estres.corr(depre)                               # Calcular correlación entre ambas vbles
    pendiente, constante = np.polyfit(estres, depre, 1)  # Calcular línea de tendencia

    plt.figure(figsize=(8, 5))
    plt.scatter(estres, depre, color='red', alpha=0.6, label='Datos')
    plt.plot( estres, pendiente * estres + constante, color='black', label='Tendencia')
    plt.xlabel('Nivel de estrés')
    plt.ylabel('Depresión')
    plt.title('H1: Relación entre estrés y depresión')
    plt.legend()
    plt.grid(alpha=0.3)
    plt.text(0.05, 0.90,  f'Correlación: r = {r:.3f}', transform=plt.gca().transAxes) 
    plt.tight_layout()
    plt.savefig('H1_estres_depresion.png', format='png', dpi=300, bbox_inches='tight')   # guardo gráfico en PNG en el directorio desde el q ejecutes el programa

    plt.show()


    # correlacion = df['estres'].corr(df['depresion'])
    # print("H1: Estrés y depresión, Correlación:", correlacion)    


'''   Depresion 0=no y 1=sí. Los gráficos permiten visualizar la relación entre cada vble y si hay depresión. 
      La línea es una tendencia lineal, no una regresión logística.'''    


# A > nº de horas de sueño, < probabilidad de depresión    Correlación negativa (r < 0) . Espero una línea descendente y una correlación negativa (r < 0)
def hipotesis_H2(df):

    x = df['horas_sueno']
    y = df['depresion']

    r = x.corr(y)                                 # Calcular correlación
    pendiente, constante = np.polyfit(x, y, 1)    # Calcular línea de tendencia

    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, color='green', alpha=0.6, label='Datos')
    plt.plot( x, pendiente * x + constante, color='black', label='Tendencia')
    plt.xlabel('Horas de sueño')
    plt.ylabel('Depresión')
    plt.title('H2: Relación entre sueño y depresión')
    plt.legend()
    plt.grid(alpha=0.3)
    plt.text( 0.05, 0.90, f'Correlación: r = {r:.3f}', transform=plt.gca().transAxes)
    plt.tight_layout()
    plt.savefig('H2_sueno_depresion.png', format='png', dpi=300, bbox_inches='tight')

    plt.show()

    #correlacion = df['horas_sueno'].corr(df['depresion'])
    #print("H2: Sueño y depresión, Correlación:", correlacion) 



def hipotesis_H3(df):    # A > nivel de estrés, < nº de horas de sueño.   Se espera una correlación negativa (r < 0).

    estres = df['estres']
    sueno = df['horas_sueno']

    r = estres.corr(sueno)    # Calcular correlación    
    pendiente, constante = np.polyfit(estres, sueno, 1)    # Calcular línea de tendencia

    # Crear gráfico
    plt.figure(figsize=(8, 5))
    plt.scatter(estres, sueno, color='blue', alpha=0.6, label='Datos')
    plt.plot( estres, pendiente * estres + constante,  color='black',  label='Tendencia')
    plt.xlabel('Nivel de estrés')
    plt.ylabel('Horas de sueño')
    plt.title('H3: Relación entre estrés y horas de sueño')
    plt.legend()
    plt.grid(alpha=0.3)
    plt.text( 0.05, 0.90, f'Correlación: r = {r:.3f}', transform=plt.gca().transAxes)
    plt.tight_layout()    
    plt.savefig( 'H3_estres_sueno.png',  format='png', dpi=300, bbox_inches='tight')  # Guardo gráfico en PNG

    plt.show()