import csv
from .models import Order

def load_orders_from_csv(filepath):
    orders = []
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            order = Order(
                id=row["order_id"],
                product_type=row["Product type"],
                cut_time=int(row["cut time"]),
                sew_time=int(row["sew time"]),
                pack_time=int(row["pack time"]),
                deadline=int(row["deadline"]),
                requires_out_of_factory_delay=row["requires_out_of_factory_delay"].strip().upper() == "TRUE"
            )
            orders.append(order)
    return orders

def save_schedule_as_csv(schedule_summary, output_file_path):
    # Define fieldnames including the new 'late_by' field
    fieldnames = ['order_id', 'Product type', 'cut time', 'sew time', 'pack time', 'deadline', 
                  'requires_out_of_factory_delay', 'late_by']
    
    # Write updated schedule to a new CSV file
    with open(output_file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for entry in schedule_summary:
            # Prepare data for each order
            schedule_entry = {
                "order_id": entry["order_id"],
                "Product type": entry["product_type"],
                "cut time": entry["cut_time"],
                "sew time": entry["sew_time"],
                "pack time": entry["pack_time"],
                "deadline": entry["deadline"],
                "requires_out_of_factory_delay": "TRUE" if entry["requires_out_of_factory_delay"] else "FALSE",
                "late_by": entry["late_by"]
            }
            writer.writerow(schedule_entry)

def evaluate_schedule(schedule_summary):
    total_orders = len(schedule_summary)
    total_on_time = sum(1 for entry in schedule_summary if entry['late_by'] == 0)
    average_lateness = sum(entry['late_by'] for entry in schedule_summary) / total_orders if total_orders > 0 else 0
    return {
        "total_orders": total_orders,
        "total_on_time": total_on_time,
        "average_lateness": average_lateness
    }