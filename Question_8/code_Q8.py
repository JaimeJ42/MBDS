#!/usr/bin/python
# -*- coding:utf-8 -*-

#Q8.2

k1 = 100
k2 = 600
k3 = 150
E_free = E0 = 1
S_total = S0 = 10
ES_total = ES0 = 0
P_total = P0 = 0

def ES(t,c, S):
    return k1*(E0-c)*(S-k3*c) - (k2+k3)*c

def runge_kutta(t0, c0, dt, N):
    global E0, S0, ES0, P0
    global E_free, S_total, ES_total, P_total
    while N:
        t1 = t0 + dt
        S = S0
        K1 = ES(t0, c0, S)
        K2 = ES(t0+dt/2, c0+dt*K1/2, S)
        K3 = ES(t0+dt/2, c0+dt*K2/2, S)
        K4 = ES(t1, c0+dt*K3, S)
        ES1 = c0 + dt*(K1+K2*2+K3*2+K4)/6
        E1 = -k1*(E0-ES1)*(S-k3*ES1) + (k2+k3)*ES1
        S1 = -k1*(E0-ES1)*(S-k3*ES1) + k2*ES1
        P1 = k3*ES1

        S0 -= P1*dt
        E_free += E1*dt
        S_total += S1*dt
        ES_total += ES1*dt
        P_total += P1*dt

        if S_total > 0 and E_free > 0:
            #print('%.6f, %.6f, %.6f, %.6f, %.6f' % (t1, E1, S1, ES1, P1))
            print('%.6f, %.6f, %.6f, %.6f, %.6f' % (t1, E_free, S_total, ES_total, P_total))

        if S_total > 0 and E_free < 0:
            E_free -= E1*dt
            ES_total -= ES1*dt
            #print('%.6f, %.6f, %.6f, %.6f, %.6f' % (t1, E1, S1, ES1, P1))
            print('%.6f, %.6f, %.6f, %.6f, %.6f' % (t1, E_free, S_total, ES_total, P_total))

        N -= 1
        t0 = t1
        c0 += ES1*dt
runge_kutta(0, ES0, 0.00002, 1500)

#Q8.3
import matplotlib.pyplot as plt
import numpy as np

S = np.linspace(0, 10, 50)
Velocity = (k3*E0*S)/((k1/(k2+k3))+S)
plt.figure()
plt.plot(S, Velocity)
plt.show()


'''
#Q8.2
k1 = 100
k2 = 600
k3 = 150
E0 = 1
S0 = 10
ES0 = 0
P0 = 0

def ES(t, c, S):
    return k1*(E0-c)*(S-k3*c) - (k2+k3)*c
def E(t, c, S, ES):
    return -k1*(E0-ES)*(S-k3*ES) + (k2+k3)*ES
def S(t, c, S, ES):
    return -k1*(E0-ES)*(S-k3*ES) + k2*ES
def P(t, c, ES):
    return k3*ES

def runge_kutta(t0, ES_c0, E_c0, S_c0, P_c0, dt, N):
    global E0, S0, ES0, P0, count
    while N:
        t1 = t0 + dt
        S_next = S0
        ES_K1 = ES(t0, ES_c0, S_next)
        ES_K2 = ES(t0+dt/2, ES_c0+dt*ES_K1/2, S_next)
        ES_K3 = ES(t0+dt/2, ES_c0+dt*ES_K2/2, S_next)
        ES_K4 = ES(t1, ES_c0+dt*ES_K3, S_next)
        ES1 = ES_c0 + dt*(ES_K1+ES_K2*2+ES_K3*2+ES_K4)/6

        E_K1 = E(t0, E_c0, S_next, ES1)
        E_K2 = E(t0+dt/2, E_c0+dt*E_K1/2, S_next, ES1)
        E_K3 = E(t0+dt/2, E_c0+dt*E_K2/2, S_next, ES1)
        E_K4 = E(t1, E_c0+dt*E_K3, S_next, ES1)
        E1 = E_c0 + dt*(E_K1+E_K2*2+E_K3*2+E_K4)/6

        S_K1 = S(t0, S_c0, S_next, ES1)
        S_K2 = S(t0+dt/2, S_c0+dt*S_K1/2, S_next, ES1)
        S_K3 = S(t0+dt/2, S_c0+dt*S_K2/2, S_next, ES1)
        S_K4 = S(t1, S_c0+dt*S_K3, S_next, ES1)
        S1 = S_c0 + dt*(S_K1+S_K2*2+S_K3*2+S_K4)/6

        P_K1 = P(t0, P_c0, ES1)
        P_K2 = P(t0+dt/2, P_c0+dt*P_K1/2, ES1)
        P_K3 = P(t0+dt/2, P_c0+dt*P_K2/2, ES1)
        P_K4 = P(t1, P_c0+dt*P_K3, ES1)
        P1 = P_c0 + dt*(P_K1+P_K2*2+P_K3*2+P_K4)/6

        S0 -= P1

        if S1 > 0 and E1 > 0:
            print('%.6f, %.6f, %.6f, %.6f, %.6f' % (t1, E1, S1, ES1, P1))

        N -= 1
        t0 = t1
        ES_c0 = ES1
        E_c0 = E1
        S_c0 = S1
        P_c0 = P1
runge_kutta(0, ES0, E0, S0, P0, 0.0002, 100)
'''