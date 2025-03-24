import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_route_on_sphere(points, route, garage, office, total_time):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))
    
    ax.plot_surface(x, y, z, color='lightblue', alpha=0.3)
    
    def latlon_to_cartesian(lat, lon, R=1):
        lat, lon = np.radians(lat), np.radians(lon)
        x = R * np.cos(lat) * np.cos(lon)
        y = R * np.cos(lat) * np.sin(lon)
        z = R * np.sin(lat)
        return x, y, z
    
    for idx, point in enumerate(points[:-2]): 
        x, y, z = latlon_to_cartesian(point[1], point[2])
        ax.scatter(x, y, z, color='blue', s=50, label='Colaboradores' if idx == 0 else "")
    
    # Plotar garagem e escritório
    x_g, y_g, z_g = latlon_to_cartesian(garage[0], garage[1])
    ax.scatter(x_g, y_g, z_g, color='green', s=100, marker='s', label='Garagem')
    
    x_o, y_o, z_o = latlon_to_cartesian(office[0], office[1])
    ax.scatter(x_o, y_o, z_o, color='red', s=100, marker='*', label='Escritório')
    
    if route:
        # Garagem → primeiro ponto
        first_point = route[0]
        x1, y1, z1 = latlon_to_cartesian(points[first_point][1], points[first_point][2])
        ax.plot([x_g, x1], [y_g, y1], [z_g, z1], 'g--', linewidth=2, label='Garagem → 1º ponto')
        
        # Pontos intermediários
        for i in range(len(route)-1):
            x1, y1, z1 = latlon_to_cartesian(points[route[i]][1], points[route[i]][2])
            x2, y2, z2 = latlon_to_cartesian(points[route[i+1]][1], points[route[i+1]][2])
            ax.plot([x1, x2], [y1, y2], [z1, z2], 'r-', linewidth=1)
        
        # Último ponto → escritório
        last_point = route[-1]
        x1, y1, z1 = latlon_to_cartesian(points[last_point][1], points[last_point][2])
        ax.plot([x1, x_o], [y1, y_o], [z1, z_o], 'r-', linewidth=1, label='Rota completa')
    
    ax.set_title(f'Rota em Esfera 3D\nTempo total: {total_time:.1f} minutos', pad=20)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1))
    ax.grid(False)
    plt.tight_layout()
    plt.show()