import subprocess
import os

if __name__ == "__main__":
    cmd = "py -m test.test_battery.test_nubbin_battery"
    cmd += " && py -m test.test_battery.test_spindler_battery"
    cmd += " && py -m test.test_engine.test_capulet_engine"
    cmd += " && py -m test.test_engine.test_sternman_engine"
    cmd += " && py -m test.test_engine.test_willoughby_engine"
    cmd += " && py -m test.test_tire.test_octoprime_tires"
    cmd += " && py -m test.test_tire.test_carrigan_tires"
    subprocess.run(cmd, shell = True)