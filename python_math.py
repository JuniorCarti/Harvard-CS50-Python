#python math
# Python Math
import math
# Example of using the math module to calculate the square root of a number
def calculate_square_root(number):
    return math.sqrt(number)
# Example of using the calculate_square_root function
def main_square_root():
    number = 16
    square_root = calculate_square_root(number)
    print(f"Square Root of {number}: {square_root}")    
if __name__ == "__main__":
    main_square_root()
# Example of using the math module to calculate the factorial of a number
def calculate_factorial(number):
    return math.factorial(number)
# Example of using the calculate_factorial function
def main_factorial():
    number = 5
    factorial = calculate_factorial(number)
    print(f"Factorial of {number}: {factorial}")
if __name__ == "__main__":
    main_factorial()
# Example of using the math module to calculate the sine of an angle
def calculate_sine(angle):
    return math.sin(math.radians(angle))
# Example of using the calculate_sine function
def main_sine():
    angle = 30
    sine_value = calculate_sine(angle)
    print(f"Sine of {angle} degrees: {sine_value}")
if __name__ == "__main__":
    main_sine()
# Example of using the math module to calculate the cosine of an angle
def calculate_cosine(angle):
    return math.cos(math.radians(angle))
# Example of using the calculate_cosine function
def main_cosine():
    angle = 60
    cosine_value = calculate_cosine(angle)
    print(f"Cosine of {angle} degrees: {cosine_value}")
if __name__ == "__main__":
    main_cosine()
# Example of using the math module to calculate the tangent of an angle
def calculate_tangent(angle):
    return math.tan(math.radians(angle))
# Example of using the calculate_tangent function
def main_tangent():
    angle = 45
    tangent_value = calculate_tangent(angle)
    print(f"Tangent of {angle} degrees: {tangent_value}")
if __name__ == "__main__":
    main_tangent()
# Example of using the math module to calculate the logarithm of a number
def calculate_logarithm(number, base=10):
    return math.log(number, base)
# Example of using the calculate_logarithm 
def main_logarithm():
    number = 100
    base = 10
    logarithm_value = calculate_logarithm(number, base)
    print(f"Logarithm of {number} to base {base}: {logarithm_value}")
if __name__ == "__main__":
    main_logarithm()
# Example of using the math module to calculate the power of a number
def calculate_power(base, exponent):
    return math.pow(base, exponent)
# Example of using the calculate_power function
def main_power():
    base = 2
    exponent = 3
    power_value = calculate_power(base, exponent)
    print(f"{base} raised to the power of {exponent}: {power_value}")
if __name__ == "__main__":
    main_power()
# Example of using the math module to calculate the greatest common divisor (GCD) of two numbers
def calculate_gcd(a, b):
    return math.gcd(a, b)
# Example of using the calculate_gcd function
def main_gcd():
    a = 48
    b = 18
    gcd_value = calculate_gcd(a, b)
    print(f"GCD of {a} and {b}: {gcd_value}")
if __name__ == "__main__":
    main_gcd()
# Example of using the math module to calculate the least common multiple (LCM) of two numbers
def calculate_lcm(a, b):
    return abs(a * b) // math.gcd(a, b)
# Example of using the calculate_lcm function
def main_lcm():
    a = 12
    b = 15
    lcm_value = calculate_lcm(a, b)
    print(f"LCM of {a} and {b}: {lcm_value}")
if __name__ == "__main__":
    main_lcm()
# Example of using the math module to calculate the area of a circle
def calculate_circle_area(radius):
    return math.pi * (radius ** 2)
# Example of using the calculate_circle_area function
def main_circle_area():
    radius = 5
    circle_area = calculate_circle_area(radius)
    print(f"Area of a circle with radius {radius}: {circle_area}")
if __name__ == "__main__":
    main_circle_area()
# Example of using the math module to calculate the circumference of a circle
def calculate_circle_circumference(radius):
    return 2 * math.pi * radius
# Example of using the calculate_circle_circumference function
def main_circle_circumference():
    radius = 5
    circle_circumference = calculate_circle_circumference(radius)
    print(f"Circumference of a circle with radius {radius}: {circle_circumference}")
if __name__ == "__main__":
    main_circle_circumference()
# Example of using the math module to calculate the area of a triangle
def calculate_triangle_area(base, height):
    return 0.5 * base * height
# Example of using the calculate_triangle_area function
def main_triangle_area():
    base = 10
    height = 5
    triangle_area = calculate_triangle_area(base, height)
    print(f"Area of a triangle with base {base} and height {height}: {triangle_area}")
if __name__ == "__main__":
    main_triangle_area()
# Example of using the math module to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    return length * width
# Example of using the calculate_rectangle_area function
def main_rectangle_area():
    length = 10
    width = 5
    rectangle_area = calculate_rectangle_area(length, width)
    print(f"Area of a rectangle with length {length} and width {width}: {rectangle_area}")
if __name__ == "__main__":
    main_rectangle_area()
# Example of using the math module to calculate the area of a square
def calculate_square_area(side):
    return side ** 2
# Example of using the calculate_square_area function
def main_square_area():
    side = 4
    square_area = calculate_square_area(side)
    print(f"Area of a square with side {side}: {square_area}")
if __name__ == "__main__":
    main_square_area()
# Example of using the math module to calculate the volume of a sphere
def calculate_sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)
# Example of using the calculate_sphere_volume function
def main_sphere_volume():
    radius = 3
    sphere_volume = calculate_sphere_volume(radius)
    print(f"Volume of a sphere with radius {radius}: {sphere_volume}")
if __name__ == "__main__":
    main_sphere_volume()
# Example of using the math module to calculate the volume of a cylinder
def calculate_cylinder_volume(radius, height):
    return math.pi * (radius ** 2) * height
# Example of using the calculate_cylinder_volume function
def main_cylinder_volume():
    radius = 3
    height = 5
    cylinder_volume = calculate_cylinder_volume(radius, height)
    print(f"Volume of a cylinder with radius {radius} and height {height}: {cylinder_volume}")
if __name__ == "__main__":
    main_cylinder_volume()
# Example of using the math module to calculate the volume of a cone
def calculate_cone_volume(radius, height):
    return (1/3) * math.pi * (radius ** 2) * height
# Example of using the calculate_cone_volume function
def main_cone_volume():
    radius = 3
    height = 5
    cone_volume = calculate_cone_volume(radius, height)
    print(f"Volume of a cone with radius {radius} and height {height}: {cone_volume}")
if __name__ == "__main__":
    main_cone_volume()
# Example of using the math module to calculate the area of a trapezoid
def calculate_trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height
# Example of using the calculate_trapezoid_area function
def main_trapezoid_area():
    base1 = 10
    base2 = 5
    height = 4
    trapezoid_area = calculate_trapezoid_area(base1, base2, height)
    print(f"Area of a trapezoid with bases {base1} and {base2} and height {height}: {trapezoid_area}")
if __name__ == "__main__":
    main_trapezoid_area()
# Example of using the math module to calculate the area of a parallelogram
def calculate_parallelogram_area(base, height):
    return base * height
# Example of using the calculate_parallelogram_area function
def main_parallelogram_area():
    base = 10
    height = 5
    parallelogram_area = calculate_parallelogram_area(base, height)
    print(f"Area of a parallelogram with base {base} and height {height}: {parallelogram_area}")
if __name__ == "__main__":
    main_parallelogram_area()
# Example of using the math module to calculate the area of a rhombus
def calculate_rhombus_area(diagonal1, diagonal2):
    return 0.5 * diagonal1 * diagonal2
# Example of using the calculate_rhombus_area function
def main_rhombus_area():
    diagonal1 = 8
    diagonal2 = 6
    rhombus_area = calculate_rhombus_area(diagonal1, diagonal2)
    print(f"Area of a rhombus with diagonals {diagonal1} and {diagonal2}: {rhombus_area}")
if __name__ == "__main__":
    main_rhombus_area()
# Example of using the math module to calculate the area of an ellipse
def calculate_ellipse_area(semi_major_axis, semi_minor_axis):
    return math.pi * semi_major_axis * semi_minor_axis
# Example of using the calculate_ellipse_area function
def main_ellipse_area():
    semi_major_axis = 5
    semi_minor_axis = 3
    ellipse_area = calculate_ellipse_area(semi_major_axis, semi_minor_axis)
    print(f"Area of an ellipse with semi-major axis {semi_major_axis} and semi-minor axis {semi_minor_axis}: {ellipse_area}")
if __name__ == "__main__":
    main_ellipse_area()
# Example of using the math module to calculate the area of a sector of a circle
def calculate_sector_area(radius, angle):
    return 0.5 * radius ** 2 * math.radians(angle)
# Example of using the calculate_sector_area function
def main_sector_area():
    radius = 5
    angle = 60
    sector_area = calculate_sector_area(radius, angle)
    print(f"Area of a sector of a circle with radius {radius} and angle {angle} degrees: {sector_area}")
if __name__ == "__main__":
    main_sector_area()
# Example of using the math module to calculate the area of a segment of a circle
def calculate_segment_area(radius, angle):
    return (math.pi * radius ** 2 * angle / 360) - (0.5 * radius ** 2 * math.sin(math.radians(angle)))
# Example of using the calculate_segment_area function
def main_segment_area():
    radius = 5
    angle = 60
    segment_area = calculate_segment_area(radius, angle)
    print(f"Area of a segment of a circle with radius {radius} and angle {angle} degrees: {segment_area}")
if __name__ == "__main__":
    main_segment_area()
# Example of using the math module to calculate the area of a polygon
def calculate_polygon_area(num_sides, side_length):
    return (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))
# Example of using the calculate_polygon_area function
def main_polygon_area():
    num_sides = 5
    side_length = 6
    polygon_area = calculate_polygon_area(num_sides, side_length)
    print(f"Area of a regular polygon with {num_sides} sides and side length {side_length}: {polygon_area}")
if __name__ == "__main__":
    main_polygon_area()
# Example of using the math module to calculate the area of a regular hexagon
def calculate_hexagon_area(side_length):
    return (3 * math.sqrt(3) * side_length ** 2) / 2
# Example of using the calculate_hexagon_area function
def main_hexagon_area():
    side_length = 4
    hexagon_area = calculate_hexagon_area(side_length)
    print(f"Area of a regular hexagon with side length {side_length}: {hexagon_area}")
if __name__ == "__main__":
    main_hexagon_area()
# Example of using the math module to calculate the area of a regular pentagon
def calculate_pentagon_area(side_length):
    return (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side_length ** 2
# Example of using the calculate_pentagon_area function
def main_pentagon_area():
    side_length = 4
    pentagon_area = calculate_pentagon_area(side_length)
    print(f"Area of a regular pentagon with side length {side_length}: {pentagon_area}")
if __name__ == "__main__":

    main_pentagon_area()
# Example of using the math module to calculate the area of a regular octagon
def calculate_octagon_area(side_length):
    return 2 * (1 + math.sqrt(2)) * side_length ** 2
# Example of using the calculate_octagon_area function
def main_octagon_area():
    side_length = 4
    octagon_area = calculate_octagon_area(side_length)
    print(f"Area of a regular octagon with side length {side_length}: {octagon_area}")
if __name__ == "__main__":
    main_octagon_area()

