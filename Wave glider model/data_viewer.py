import matplotlib.pyplot as plt
t_plot = []


def data_viewer(x1, y1, phid, phit, t,
                u1='', T='', rudder_angle='',
                Ffoil_x=''):
    t_plot.append(t)
    plt.figure(1)

    path = plt.subplot(3, 2, 1)
    path.plot(y1, x1, '-r')
    path.set_title('Path')
    path.set_ylabel('x(m)')
    path.set_xlabel('y(m)')

    heading = plt.subplot(3, 2, 2)
    heading.plot(t_plot, phid, '-r')
    heading.plot(t_plot, phit, '-b')
    heading.set_ylabel('Course(rad)')
    heading.set_xlabel('Time(s)')

    if T:
        T_plot = plt.subplot(3, 2, 3)
        T_plot.plot(t_plot, T, '-r')
        T_plot.set_title('Tether force')
        T_plot.set_ylabel('T(N)')
        T_plot.set_xlabel('Time(s)')

    if u1:
        speed_plot = plt.subplot(3, 2, 4)
        speed_plot.plot(t_plot, u1, '-r')
        speed_plot.set_title('Sailing speed')
        speed_plot.set_ylabel('Speed(m/s)')
        speed_plot.set_xlabel('Time(s)')

    if rudder_angle:
        rudder_angle_plot = plt.subplot(3, 2, 5)
        rudder_angle_plot.plot(t_plot, rudder_angle, '-r')
        rudder_angle_plot.set_title('Rudder angle')
        rudder_angle_plot.set_ylabel('Rudder angle(deg)')
        rudder_angle_plot.set_xlabel('Time(s)')

    if Ffoil_x:
        Ffoil_x_plot = plt.subplot(3, 2, 6)
        Ffoil_x_plot.plot(t_plot, Ffoil_x, '-r')
        Ffoil_x_plot.set_title('Foil force')
        Ffoil_x_plot.set_ylabel('Foil force(N)')
        Ffoil_x_plot.set_xlabel('Time(s)')


    plt.tight_layout()
    plt.pause(0.00000000000000001)


