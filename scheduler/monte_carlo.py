import random
from .forward import forward_schedule
from .utils import evaluate_schedule

def run_monte_carlo(orders, cut_machines, sew_machines, pack_machines, iterations=100):
    best_schedule = None
    best_schedule_evaluation = None
    lowest_avg_lateness = float('inf')

    for _ in range(iterations):
        shuffled = random.sample(orders, len(orders))
        schedule = forward_schedule(shuffled, 
                                    [m.copy() for m in cut_machines], 
                                    [m.copy() for m in sew_machines], 
                                    [m.copy() for m in pack_machines])
        evaluation = evaluate_schedule(schedule)
        if evaluation['average_lateness'] < lowest_avg_lateness:
            lowest_avg_lateness = evaluation['average_lateness']
            best_schedule_evaluation = evaluation;
            best_schedule = schedule
    print("Total orders completed on time:", best_schedule_evaluation["total_on_time"])
    print("Average days late:", round(best_schedule_evaluation["average_lateness"]/24,2))
    return best_schedule
