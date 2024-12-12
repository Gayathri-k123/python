from graphics.rectangle import area as rect_area
from graphics.rectangle import perimeter as rect_perimeter
from graphics.circle import area as circle_area
from graphics.circle import circumference as circle_circumference
from graphics.graphics_3d.cuboid import volume as cuboid_volume
from graphics.graphics_3d.cuboid import surfacearea as cuboid_surface_area
from graphics.graphics_3d.sphere import volume as sphere_volume
from graphics.graphics_3d.sphere import surfacearea as sphere_surface_area
length=float(input("\nEnter the length of the rectangle : "))
breadth=float(input("Enter the breadth of the rectangle : "))
print("Area of the Rectangle : ",rect_area(length,breadth))
print("Perimeter of the Rectangle : ",rect_perimeter(length,breadth))
radius=float(input("\nEnter the radius of the circle : "))
print("Area of the Circle : ",circle_area(radius))
print("Circumference of the Circle : ",circle_circumference(radius))
cuboid_length=float(input("\nEnter the length of the cuboid : "))
cuboid_breadth=float(input("Enter the breadth of the cuboid : "))
cuboid_height=float(input("Enter the height of the cuboid : "))
print("Volume of the Cuboid : ",cuboid_volume(cuboid_length,cuboid_breadth,cuboid_height))
print("Surface area of the cuboid : ",cuboid_surface_area(cuboid_length,cuboid_breadth,cuboid_height))
sphere_radius=float(input("\nEnter the radius of the sphere : "))
print("Volume of the Sphere : ",sphere_volume(sphere_radius))
print("Surface area of the Sphere : ",sphere_surface_area(sphere_radius))



