#!/usr/bin/env python

from __future__ import division
#import os
import numpy as np
#from scipy.io import loadmat, savemat
#import scipy.signal as sig
#import scipy.constants as const

# two mirror FP cavity transmission
def t_FP(T1, T2, k, L):
    t1 = np.sqrt(T1)
    t2 = np.sqrt(T2)
    r1 = np.sqrt(1-t1**2)
    r2 = np.sqrt(1-t2**2)
    t = t1*t2 / (1 - r1*r2*np.exp(-1j*2*k*L))
    return t

# two mirror FP cavity reflection
def r_FP(T1, T2, k, L):
    t1 = np.sqrt(T1)
    t2 = np.sqrt(T2)
    r1 = np.sqrt(1-t1**2)
    r2 = np.sqrt(1-t2**2)
    r = r1 - (t1**2 * r2 * np.exp(-1j*2*k*L)) / (1 - r1*r2*np.exp(-1j*2*k*L))
    return r

# Take as input:
# the input field (carrier + SBs)
# cavity fixed parameters
# cavity length (macroscopic length + detuning)


# compute the transmitted and reflected fields at each frequency for the given length

# compute the DC powers, the 1-omega PDH signals, the 2-omega PDH signals
def P_trans(Ein, T1, T2, k, L):
    return np.sum(np.abs(Ein * t_FP(T1, T2, k, L))**2)

def P_refl(Ein, T1, T2, k, L):
    return np.sum(np.abs(Ein * r_FP(T1, T2, k, L))**2)

def REFL_IQ(Ein, T1, T2, k, L):
    refl = Ein * r_FP(T1, T2, k, L)
    x    = np.outer(np.conj(refl), refl)
    beat = np.sum(x[0,1] + x[1,2])
    return beat.real, beat.imag
