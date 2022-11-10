import sympy.physics.units as u
from sympy.physics.units.systems import SI

distance = u.Quantity('d')
SI.set_quantity_dimension(distance, u.length)
SI.set_quantity_scale_factor(distance, 5.*u.meter)


