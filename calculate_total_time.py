from settings import SPEED

def calculate_total_time(route, distance_matrix, garage_idx, office_idx):
    total_time = 0
    current_point = garage_idx
    for next_point in route + [office_idx]:
        total_time += (distance_matrix[current_point][next_point] / SPEED) * 60
        current_point = next_point
    return total_time