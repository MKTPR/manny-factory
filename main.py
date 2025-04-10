from scheduler.models import Machine
from scheduler.monte_carlo import run_monte_carlo
from scheduler.utils import load_orders_from_csv, save_schedule_as_csv

orders = load_orders_from_csv('data/orders.csv')
cut_machines = [Machine(id=i, stage='cut') for i in range(2)]
sew_machines = [Machine(id=i, stage='sew') for i in range(3)]
pack_machines = [Machine(id=0, stage='pack')]

best = run_monte_carlo(orders, cut_machines, sew_machines, pack_machines, iterations=500)

save_schedule_as_csv(best, 'results/best_schedule.csv')
