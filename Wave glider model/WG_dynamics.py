import numpy as np
from math import sin
from Model.J import J
from Model.Vc import Vc
from Model.Foil import Foil
from Model.WG import WG
from Model.Tether import Tether
from Model.Rudder import Rudder


class WG_dynamics():
    def __init__(self, H, omega, c_dir, c_speed):
        self.state_0 = np.array([[0], [0], [0], [0],  # eta1
                  [0], [0], [0], [0],  # V1
                  [0], [0], [6.2], [0],  # eta2
                  [0], [0], [0], [0]], float)  # V2
        self.c_dir = c_dir
        self.c_speed = c_speed
        self.H = H
        self.omega = omega

    def f(self, state, phid, t):
        eta1 = state[0:4]
        eta1[2] = self.H / 2 * sin(self.omega * t)
        V1 = state[4:8]
        eta2 = state[8:12]
        V2 = state[12:16]

        V1_r = V1 - Vc(self.c_dir, self.c_speed, eta1)
        V2_r = V2 - Vc(self.c_dir, self.c_speed, eta2)

        wg = WG(eta1, eta2, V1, V2, self.c_dir, self.c_speed)
        tether = Tether(eta1, eta2)
        foil = Foil(eta2, V2, self.c_dir, self.c_speed)
        rudder = Rudder(eta2, V2, phid, self.c_dir, self.c_speed)

        eta1_dot = np.dot(J(eta1), V1)
        eta2_dot = np.dot(J(eta2), V2)

        Minv_1 = np.linalg.inv(wg.MRB_1() + wg.MA_1())
        Minv_2 = np.linalg.inv(wg.MRB_2() + wg.MA_2())
        MV1_dot = - np.dot(wg.CRB_1(), V1) - np.dot(wg.CA_1(), V1_r) - np.dot(wg.D_1(), V1_r) + wg.d_1() - np.dot(wg.G_1(), eta1) + tether.Ftether_1()
        V1_dot = np.dot(Minv_1, MV1_dot)
        MV2_dot = - np.dot(wg.CRB_2(), V2) - np.dot(wg.CA_2(), V2_r) - wg.d_2() - wg.g_2() + tether.Ftether_2() + rudder.force() + foil.foilforce()
        V2_dot = np.dot(Minv_2, MV2_dot)

        return np.vstack((eta1_dot, V1_dot, eta2_dot, V2_dot))
