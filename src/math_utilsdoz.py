from lib.mathdoz import dot, transpose, PI_DOZ, E_DOZ, abs_doz, pow_doz, sqrt_doz, exp_doz, log_doz, sin_doz, cos_doz, tan_doz, factorial_doz
from lib.activationsdoz import relu, sigmoid

# Constantes disponibles para el visitor
constants = {
    "PI": PI_DOZ,
    "E": E_DOZ
}
from lib.lossesdoz import mse, mse_grad

# We can re-export them or simply use this as a central module if desired.
# For now, it just exposes the same interface `visitor.py` was expecting.
