def forward_schedule(orders, cut_machines, sew_machines, pack_machines):
    schedule_summary = []

    for order in orders:
        # === CUT ===
        best_cut_start = float('inf')
        chosen_cut_machine = None
        for machine in cut_machines:
            available_time = machine.get_available_time()
            setup_time = 0
            if machine.last_product_type() and machine.last_product_type() != order.product_type:
                setup_time = 10

            earliest_start = available_time + setup_time
            if earliest_start < best_cut_start:
                best_cut_start = earliest_start
                chosen_cut_machine = machine

        cut_start = best_cut_start
        cut_end = cut_start + order.cut_time
        chosen_cut_machine.schedule_task(cut_start, order.cut_time, order)

        # === Optional Post-Cut Delay ===
        if order.requires_out_of_factory_delay:
            post_cut_ready = cut_end + 48
        else:
            post_cut_ready = cut_end

        # === SEW ===
        best_sew_start = float('inf')
        chosen_sew_machine = None
        for machine in sew_machines:
            available_time = machine.get_available_time()
            earliest_start = max(available_time, post_cut_ready)
            if earliest_start < best_sew_start:
                best_sew_start = earliest_start
                chosen_sew_machine = machine

        sew_start = best_sew_start
        sew_end = sew_start + order.sew_time
        chosen_sew_machine.schedule_task(sew_start, order.sew_time, order)

        # === PACK ===
        best_pack_start = float('inf')
        chosen_pack_machine = None
        for machine in pack_machines:
            available_time = machine.get_available_time()
            earliest_start = max(available_time, sew_end)
            if earliest_start < best_pack_start:
                best_pack_start = earliest_start
                chosen_pack_machine = machine

        pack_start = best_pack_start
        pack_end = pack_start + order.pack_time
        chosen_pack_machine.schedule_task(pack_start, order.pack_time, order)
        # === Record ===
        schedule_summary.append({
            "order_id": order.id,
            "product_type": order.product_type,
            "cut_time": order.cut_time,
            "sew_time": order.sew_time,
            "pack_time": order.pack_time,
            "sew_end": sew_end,
            "deadline": order.deadline,
            "requires_out_of_factory_delay": order.requires_out_of_factory_delay,
            "late_by": max(0, pack_end - order.deadline)
        })

    return schedule_summary
