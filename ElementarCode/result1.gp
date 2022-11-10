set log x
plot [200:1e6] "result1N.dat"u 1:(($2+2.9237405274557)*$1**2) w lp
