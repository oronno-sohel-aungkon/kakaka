import math

def deg2rad(angle_deg: float) -> float:
    """Convert degrees to radians."""
    return math.radians(angle_deg)

def sin_deg(angle_deg: float) -> float:
    """Sine of angle in degrees."""
    return math.sin(deg2rad(angle_deg))

def cos_deg(angle_deg: float) -> float:
    """Cosine of angle in degrees."""
    return math.cos(deg2rad(angle_deg))

def tan_deg(angle_deg: float) -> float:
    """Tangent of angle in degrees. Returns float('inf') if angle is odd multiple of 90°."""
    rad = deg2rad(angle_deg)
    cosv = math.cos(rad)
    if math.isclose(cosv, 0.0, abs_tol=1e-12):
        raise ValueError(f"Tangent is undefined for {angle_deg}° (cos({angle_deg}) ~ 0).")
    return math.tan(rad)
