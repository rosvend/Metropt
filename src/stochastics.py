import numpy as np 
from grid import Grid
from scipy.stats import poisson
import matplotlib.pyplot as plt

#TODO: Implement CA (Cellular Automata) for population growth and movement instead of using a simple Poisson distribution. 
# This will allow for more realistic modeling of population dynamics and interactions between neighboring cells.

def pr(i,j,t,n): #Distribución de probabilidad de personas
  rate=np.sin(2*np.pi*i/20)*np.sin(2*np.pi*j/15)*2+2 #Tasa de crecimiento de población por año
  media=rate*t
  #poisson distribution
  prob = poisson.pmf(n, mu=media)
  return prob

def gen(i,j,t): #Distribución de probabilidad de personas
  rate=np.sin(2*np.pi*i/20)*np.sin(2*np.pi*j/15)*2+2 #Tasa de crecimiento de población por año
  media=rate*t
  #poisson distribution
  n = np.random.poisson(lam=media)
  return n

def expected_population(x, y, t, grid_size=20):
    rate = np.sin(2 * np.pi * x / grid_size) * np.sin(2 * np.pi * y / grid_size) * 2 + 2
    return rate * t