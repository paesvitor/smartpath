from settings import MAX_TIME, SPEED

def print_route_details(points, route, distance_matrix, garage_idx, office_idx, total_time):
    print("\n--- Detalhes da Rota Otimizada ---")
    current_point = garage_idx
    total_distance = 0
    
    print(f"{'De':<25} {'Para':<25} {'Distância (km)':<15} {'Tempo (min)':<15} {'Acumulado (min)':<15}")
    print("-" * 85)
    
    for next_point in route + [office_idx]:
        distance = distance_matrix[current_point][next_point]
        time = (distance / SPEED) * 60
        total_distance += distance
        total_time += time
        
        print(f"{points[current_point][0]:<25} {points[next_point][0]:<25} "
              f"{distance:.2f}{' (Garagem)' if current_point == garage_idx else '':<15} "
              f"{time:.1f}{' (Início)' if current_point == garage_idx else '':<15} "
              f"{total_time:.1f}")
        current_point = next_point
    
    print("-" * 85)
    print(f"{'TOTAL':<50} {total_distance:.2f} km{total_time:.1f} minutos")
    print(f"Velocidade média: {SPEED} km/h | Tempo máximo: {MAX_TIME} minutos")