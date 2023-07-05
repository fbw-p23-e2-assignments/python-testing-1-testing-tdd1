#!/usr/bin/env python

from cat_controller import CatController

WATER_HOURS = [8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19]


def main():
    test_failed = False
    cat_controller = CatController()

    # Test that water is only given each hour 8-11 and 13-19.
    for hour in range(0, 23):
        if hour in WATER_HOURS:
            if not "Give water." in cat_controller.hourly_run(hour):
                test_failed = True
        elif "Give water." in cat_controller.hourly_run(hour):
            test_failed = True

    # Test that cat cage is opened at 7:
    if not "Open cat cage." in cat_controller.hourly_run(7):
        test_failed = True

    # Test that cat cage is closed at 20:
    if not "Close cat cage." in cat_controller.hourly_run(20):
        test_failed = True

    # Test that cat is fed at 8, 12 and 17.
    for hour in [8, 12, 17]:
        if not "Feed" in cat_controller.hourly_run(hour):
            test_failed = True

    # Test that cat is fed 1 mouse, 1 hamster and 1 chicken per day.
    not_yet_fed = ["1 mouse", "1 hamster", "1 chicken"]
    for hour in [8, 12, 17]:
        hour_status = cat_controller.hourly_run(hour)
        for food in not_yet_fed:
            if food in hour_status:
                not_yet_fed.remove(food)
    if len(not_yet_fed):
        test_failed = True

    if test_failed:
        print("Unfortunately, one or several tests failed.")
    else:
        print("All tests ran successfully.")


if __name__ == "__main__":
    main()
