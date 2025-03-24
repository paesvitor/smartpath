import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from settings import MAX_TIME

def plot_route(points, route, garage, office, total_time):
    plt.figure(figsize=(12, 8))
    
    lats = [p[1] for p in points] + [office[0], garage[0]]
    lons = [p[2] for p in points] + [office[1], garage[1]]
    
    m = Basemap(projection='mill', llcrnrlat=min(lats)-0.1, urcrnrlat=max(lats)+0.1,
                llcrnrlon=min(lons)-0.1, urcrnrlon=max(lons)+0.1, resolution='l')
    m.drawcoastlines()
    m.drawcountries()
    m.drawstates()
    m.fillcontinents(color='lightgray', lake_color='lightblue')
    
    x, y = m(lons, lats)
    
    m.scatter(x[:-2], y[:-2], color='blue', s=100, label='Colaboradores', zorder=5)
    m.scatter(x[-2], y[-2], color='red', s=150, marker='*', label='Escritório', zorder=5)
    m.scatter(x[-1], y[-1], color='green', s=150, marker='s', label='Garagem', zorder=5)
    
    route_lons = [points[i][2] for i in route] + [office[1]]
    route_lats = [points[i][1] for i in route] + [office[0]]
    x_route, y_route = m(route_lons, route_lats)
    m.plot(x_route, y_route, 'r-', linewidth=2, label='Rota completa', zorder=4)
    
    if route: 
        first_point_idx = route[0]
        garage_to_first_lons = [garage[1], points[first_point_idx][2]]
        garage_to_first_lats = [garage[0], points[first_point_idx][1]]
        x_gf, y_gf = m(garage_to_first_lons, garage_to_first_lats)
        m.plot(x_gf, y_gf, 'g--', linewidth=3, label='Garagem → 1º ponto', zorder=3)
        
        m.scatter(x_gf[1], y_gf[1], color='lime', s=200, marker='o', 
                 edgecolor='black', zorder=6, label='1º ponto de coleta')

    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.title(f'Rota Otimizada\nTempo total: {total_time:.1f} minutos (Limite: {MAX_TIME} min)')
    plt.tight_layout()
    plt.show()