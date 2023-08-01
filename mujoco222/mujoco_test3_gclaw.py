# ref1 : https://mujoco.readthedocs.io/en/2.2.0/programming.html  (mujoco222 install)
# ref2 : https://github.com/vikashplus/robel_sim/tree/9d774735f5d6a599774d01d8808f411054f8cf28/dclaw (dclaw mujoco200)
# ref3 : export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so   << add must be add
import mujoco_py
import math
import os
"""
    - TAB: Switch between MuJoCo cameras.
    - H: Toggle hiding all GUI components.
    - SPACE: Pause/unpause the simulation.
    - RIGHT: Advance simulation by one step.
    - V: Start/stop video recording.
    - T: Capture screenshot.
    - I: Drop into ``ipdb`` debugger.
    - S/F: Decrease/Increase simulation playback speed.
    - C: Toggle visualization of contact forces (off by default).
    - D: Enable/disable frame skipping when rendering lags behind real time.
    - R: Toggle transparency of geoms.
    - M: Toggle display of mocap bodies.
    - 0-4: Toggle display of geomgroups
"""
mj_path = mujoco_py.utils.discover_mujoco()
mj_path = mj_path+'/model/robel_sim/dclaw/dclaw3xh.xml'
xml_path = os.path.join(mj_path)
# '/home/songwoo/.mujoco222/mujoco210/model/robel_sim/dclaw/dclaw3xh.xml'   => install mujoco210
model = mujoco_py.load_model_from_path(xml_path)
sim = mujoco_py.MjSim(model)
viewer = mujoco_py.MjViewer(sim)
t= 0

# these ID must be remapped to real dynamixel ID
# ctrl value's unit is degree and dynamixel rotate 2000 -> = 0 degree
while True:  
    # sim.data.ctrl[0] = math.cos(t / 10.) * 1   # actuator ID 10 
    sim.data.ctrl[1] = 90   # actuator ID 11``
    # sim.data.ctrl[2] = 0.9   # actuator ID 12
    # sim.data.ctrl[3] = 0.1 # actuator ID 20  (actuactor degree which is abs(45) bounded by .mjcf)
    # sim.data.ctrl[4] = math.cos(t / 10.) * 0.1 # actuator ID 21
    sim.data.ctrl[5] = math.sin(t / 100.) * 1.5 # actuator ID 22
    # sim.data.ctrl[6] = math.cos(t / 10.) * 0.1 # actuator ID 30
    # sim.data.ctrl[7] = math.sin(t / 10.) * 0.1 # actuator ID 31
    # sim.data.ctrl[8] = math.sin(t / 10.) * 0.1 # actuator ID 32
    t += 1
    sim.step(t)
    viewer.render()
    if t > 100 and os.getenv('TESTING') is not None:
        break
#print(sim.data.qpos)