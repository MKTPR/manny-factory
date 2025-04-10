from dataclasses import dataclass, field
from typing import List
import copy

@dataclass
class Order:
    id: str
    product_type: str
    cut_time: int
    sew_time: int
    pack_time: int
    deadline: int
    requires_out_of_factory_delay: bool

@dataclass
class ScheduledTask:
    start: int
    end: int
    order_id: int
    product_type: str

@dataclass
class Machine:
    id: int
    stage: str
    schedule: List[ScheduledTask] = field(default_factory=list)


    # For ease of M-C testing
    def copy(self):
        return Machine(id=self.id, stage=self.stage, schedule=copy.deepcopy(self.schedule))
    
    def get_available_time(self):
        if not self.schedule:
            return 0
        return self.schedule[-1].end

    def last_product_type(self):
        if not self.schedule:
            return None
        return self.schedule[-1].product_type

    def schedule_task(self, start, duration, order: Order):
        end = start + duration
        self.schedule.append(ScheduledTask(
            start=start,
            end=end,
            order_id=order.id,
            product_type=order.product_type
        ))
        return start, end
