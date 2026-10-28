""" 
from datetime import date

from app import app
from database import add_leave

with app.app_context():

    leave = add_leave(
        employee_id=101,
        leave_type="Paid Leave",
        start_date=date(2026, 11, 2),
        end_date=date(2026, 11, 4),
        reason="Personal work"
    )

    print("Leave application saved!")
    print("Leave ID:", leave.id)
    print("Status:", leave.status)
 """


from app import app
from database import view_leaves

with app.app_context():

    leaves = view_leaves(101)

    for leave in leaves:
        print("Leave ID:", leave.id)
        print("Leave Type:", leave.leave_type)
        print("Start Date:", leave.start_date)
        print("End Date:", leave.end_date)
        print("Reason:", leave.reason)
        print("Status:", leave.status)
        print("--------------------")
