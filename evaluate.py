from settings import MAX_TIME, SPEED

def evaluate(individual, distance_matrix, start_idx, end_idx):
    total_time = 0
    
    first_point = individual[0]
    total_time += (distance_matrix[start_idx][first_point] / SPEED) * 60
    
    for i in range(len(individual)-1):
        total_time += (distance_matrix[individual[i]][individual[i+1]] / SPEED) * 60
    
    total_time += (distance_matrix[individual[-1]][end_idx] / SPEED) * 60
    
    penalty = max(0, total_time - MAX_TIME) * 100
    return (total_time + penalty,)