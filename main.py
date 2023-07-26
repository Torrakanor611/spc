import re
import argparse
from spc.spc import *
from plot import plot

def main():
    parser = argparse.ArgumentParser(description='Log file parser')
    parser.add_argument('-f', dest='file', type=str, required=True, help='log file path')
    parser.add_argument('-sl', dest='sl', type=float, help='specification limit', default=45)
    parser.add_argument('-n', dest='n', type=int, choices=range(1,13), help='sample size', default=6)
    args = parser.parse_args()

    lines = []
    with open(args.file, "r") as file:
        lines = file.readlines()

    # remove timestamp
    lines = [line[26:] for line in lines]

    # get steps, laps, ini vel and final vel from first line
    _, _, _, steps, _, laps, _, _, vel_ini, _, _, vel_final, *_ = [data for data in re.split('\s+', lines[0])]
    steps = int(steps)
    laps = int(laps)
    vel_ini = int(vel_ini)
    vel_final = int(vel_final)

    # remove 1st and last lines
    lines = lines[1:(len(lines)-1)]

    # get setup lap data
    _, _, _, x, *_ = [data for data in lines[0].split(' ') if data != '']

    # set Target, upper and lower specification limit
    T = float(x)
    ltl = T - (args.sl / 2)
    utl = T + (args.sl / 2)

    # get test data
    x, vel, X_correction = [], [], []
    lin, poly, interpol = [], [], []
    [
        [vel.append(data[1]), x.append(data[4]), X_correction.append(data[10]),     
        lin.append(data[13]), poly.append(data[15]), interpol.append(data[17])]
        for data in [re.split('\s+', line) for line in lines[1:]]
    ]

    # sum x and X_correction and calibration
    clin, cpoly, cinterpol = [], [], []
    for i in range(0, len(x)):
        clin.append(float(x[i]) + float(X_correction[i]) + float(lin[i]))
        cpoly.append(float(x[i]) + float(X_correction[i]) + float(poly[i]))
        cinterpol.append(float(x[i]) + float(X_correction[i]) + float(interpol[i]))

    # calculate capability and capability index
    cp = []
    cpk = []

    for j in range(0, steps+1):
        s1 = spc(clin[laps*j:(laps*j)+laps], T, args.sl)
        s2 = spc(cpoly[laps*j:(laps*j)+laps], T, args.sl)
        s3 = spc(cinterpol[laps*j:(laps*j)+laps], T, args.sl)
        cp.append(s1.calc_capability(args.n))
        cp.append(s2.calc_capability(args.n))
        cp.append(s3.calc_capability(args.n))
        cpk.append(s1.calc_capability_index(args.n))
        cpk.append(s2.calc_capability_index(args.n))
        cpk.append(s3.calc_capability_index(args.n))

    # plot results
    plot(clin, cpoly, cinterpol, vel, steps, laps, ltl, T, utl, cp, cpk)

if __name__ == "__main__":
    main()