import math

def deg2rad(angle_deg: float) -> float:
    return math.radians(angle_deg)

def sin_deg(angle_deg: float) -> float:
    return math.sin(deg2rad(angle_deg))

def cos_deg(angle_deg: float) -> float:
    return math.cos(deg2rad(angle_deg))

def tan_deg(angle_deg: float) -> float:
    rad = deg2rad(angle_deg)
    cosv = math.cos(rad)
    if math.isclose(cosv, 0.0, abs_tol=1e-12):
        raise ValueError(f"Tangent is undefined for {angle_deg}° (cos({angle_deg}) ~ 0).")
    return math.tan(rad)

def main():
    angle_deg = float(input("Enter angle in degrees: "))
    s = sin_deg(angle_deg)
    c = cos_deg(angle_deg)
    try:
        t = tan_deg(angle_deg)
        tan_str = f"{t:.6f}"
    except ValueError as e:
        tan_str = str(e)

    print(f"sin({angle_deg}°) = {s:.6f}")
    print(f"cos({angle_deg}°) = {c:.6f}")
    print(f"tan({angle_deg}°) = {tan_str}")

if __name__ == "__main__":
    main()
