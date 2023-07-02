import matplotlib.pyplot as plt

xlabel = [
        "linear",
        "polinomial",
        "interpolation"
    ]

def plot(clin, cpoly, cinterpol, vel, steps, laps, ltl, T, utl, cp, cpk):
    vel_str = ''
    for data in vel[::laps]:
        vel_str+=data
    vel_str += f'{laps}laps'
    vel_str = vel_str.replace(',', '-')

    fig, axs = plt.subplots(steps + 1, 3, num=vel_str, figsize=(9, 7), sharex=True, sharey=True)

    for i in range(0, steps+1):
        axs[i, 0].hist(clin[laps*i:(laps*i)+laps], orientation='horizontal',bins=20, color='green')
        axs[i, 0].set_xlabel(f'cp {cp.pop(0)}  cpk {cpk.pop(0)}')
        axs[i, 1].hist(cpoly[laps*i:(laps*i)+laps], orientation='horizontal', bins=20, color='red')
        axs[i, 1].set_xlabel(f'cp {cp.pop(0)}  cpk {cpk.pop(0)}')
        axs[i, 2].hist(cinterpol[laps*i:(laps*i)+laps], orientation='horizontal', bins=20, color='blue')
        axs[i, 2].set_xlabel(f'cp {cp.pop(0)}  cpk {cpk.pop(0)}')
        axs[i, 0].set_ylabel(vel[i*laps].replace(',', ''), rotation=0, ha='right')

    for i in range(0, 3):
        axs[0, i].set_title(xlabel[i])

    ydelimeters = [ltl, T, utl]
    plt.yticks(ydelimeters, [str(d) for d in ydelimeters])
    plt.suptitle(f'SPC results {laps} laps')
    fig.tight_layout()
    plt.draw()
    plt.pause(0.0001)
    input("Press [enter] to continue.")
    plt.close()