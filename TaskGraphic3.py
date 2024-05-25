import matplotlib.pyplot as plt
def plot_circle(center_x, center_y, radius):
    x = radius
    y = 0
    pk = 1 - radius

    points = []
    while x >= y:
        points.append((x + center_x, y + center_y))
        points.append((-x + center_x, y + center_y))
        points.append((x + center_x, -y + center_y))
        points.append((-x + center_x, -y + center_y))
        points.append((y + center_x, x + center_y))
        points.append((-y + center_x, x + center_y))
        points.append((y + center_x, -x + center_y))
        points.append((-y + center_x, -x + center_y))

        y += 1
        if pk > 0:
            x -= 1
            pk += 2 * (y - x) + 1
        else:
            pk += 2 * y + 1

    x_points, y_points = zip(*points)
    plt.scatter(x_points, y_points, marker='s', color='b')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
plot_circle(0,0, 10)