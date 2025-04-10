from scheduler.forward import forward_schedule
from scheduler.models import Machine
from scheduler.utils import load_orders_from_csv, evaluate_schedule

def test_basic_schedule():
    orders = load_orders_from_csv('results/best_schedule.csv')
    cut_machines = [Machine(id=i, stage='cut') for i in range(2)]
    sew_machines = [Machine(id=i, stage='sew') for i in range(3)]
    pack_machines = [Machine(id=0, stage='pack')]
    schedule = forward_schedule(orders, 
                                [m.copy() for m in cut_machines], 
                                [m.copy() for m in sew_machines], 
                                [m.copy() for m in pack_machines])
    evaluation = evaluate_schedule(schedule)
    print("Total orders completed on time:", evaluation["total_on_time"])
    print("Average days late:", round(evaluation["average_lateness"]/24,2))

test_basic_schedule()
