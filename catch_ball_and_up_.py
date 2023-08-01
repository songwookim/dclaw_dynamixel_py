#!/usr/bin/env python
# -*- coding: utf-8 -*-

#*******************************************************************************
# Copyright 2017 ROBOTIS CO., LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#*******************************************************************************


#*******************************************************************************
#***********************     Read and Write Example      ***********************
#  Required Environment to run this example :
#    - Protocol 2.0 supported DYNAMIXEL(X, P, PRO/PRO(A), MX 2.0 series)
#    - DYNAMIXEL Starter Set (U2D2, U2D2 PHB, 12V SMPS)
#  How to use the example :
#    - Select the DYNAMIXEL in use at the MY_DXL in the example code. 
#    - Build and Run from proper architecture subdirectory.
#    - For ARM based SBCs such as Raspberry Pi, use linux_sbc subdirectory to build and run.
#    - https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/overview/
#  Author: Ryu Woon Jung (Leon)
#  Maintainer : Zerom, Will Son
# *******************************************************************************

import os
import numpy as np

if os.name == 'nt':
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

from dynamixel_sdk import * # Uses Dynamixel SDK library

#********* DYNAMIXEL Model definition *********
#***** (Use only one definition at a time) *****
MY_DXL = 'X_SERIES'       # X330 (5.0 V recommended), X430, X540, 2X430


# Control table address
ADDR_TORQUE_ENABLE          = 64
ADDR_GOAL_POSITION          = 116
ADDR_PRESENT_POSITION       = 132
DXL_MINIMUM_POSITION_VALUE  = 0         # Refer to the Minimum Position Limit of product eManual
DXL_MAXIMUM_POSITION_VALUE  = 4095      # Refer to the Maximum Position Limit of product eManual
BAUDRATE                    = 57600



# DYNAMIXEL Protocol Version (1.0 / 2.0)
# https://emanual.robotis.com/docs/en/dxl/protocol2/
PROTOCOL_VERSION            = 2.0

# Factory default ID of all DYNAMIXEL is 1
DXL_ID                      = 31
DXL_IDs                      = [10,11,12,20,21,22,30,31,32]

# Use the actual port assigned to the U2D2.4
DEVICENAME                  = '/dev/ttyUSB0'

TORQUE_ENABLE               = 1     # Value for enabling the torque
TORQUE_DISABLE              = 0     # Value for disabling the torque
DXL_MOVING_STATUS_THRESHOLD = 20    # Dynamixel moving status threshold

index = 0
dxl_goal_position = [DXL_MINIMUM_POSITION_VALUE, DXL_MAXIMUM_POSITION_VALUE]         # Goal position

a = 25
b = 75

dxl_goal_positions1 = [
1018,
2059,
2370,
1008,
1902,
2546,
1007,
2031,
2332,]

dxl_goal_positions2 = [
1018,
2059+a,
2370+b,
1008,
1902+a,
2546+b,
1007,
2031+a,
2332+b,]


dxl_goal_positions3 = [
1018,
2059,
2370+b+b,
1008,
1902,
2546+b+b,
1007,
2031,
2332+b+b,]

dxl_goal_positions4 = [
1058,
2059-25,
2370+b+b,
1008,
1902-25,
2546+b+b,
1007,
2031-25,
2332+b+b,]

dxl_goal_positions5 = [
1058,
2059-50,
2370+b+b+b,
1008,
1902-50,
2546+b+b+b,
1007,
2031-50,
2332+b+b+b,]

dxl_goal_positions6 = [
1058,
2059-50-a-a,
2370+b+b+b+b,
1008,
1902-50-a-a,
2546+b+b+b+b,
1007,
2031-50-a-a,
2332+b+b+b+b,]

dxl_goal_positions7 = [
1058,
2059-50-a-a-a,
2370+b+b+b+b+b,
1008,
1902-50-a-a-a,
2546+b+b+b+b+b,
1007,
2031-50-a-a-a,
2332+b+b+b+b+b,]

dxl_goal_positions8 = [
1058,
2059-50-a-a-a-a,
2370+b+b+b+b+b+b,
1008,
1902-50-a-a-a-a,
2546+b+b+b+b+b+b,
1007,
2031-50-a-a-a-a,
2332+b+b+b+b+b+b,]

dxl_goal_positions9 = [
1058,
2059-50-a-a-a-a-a,
2370+b+b+b+b+b+b+b,
1008,
1902-50-a-a-a-a-a,
2546+b+b+b+b+b+b+b,
1007,
2031-50-a-a-a-a,
2332+b+b+b+b+b+b+b,]

dxl_goal_positions10 = [
1058,
2059-50-a-a-a-a-a-a-a,
2370+b+b+b+b+b+b+b+b,
1008,
1902-50-a-a-a-a-a-a-a,
2546+b+b+b+b+b+b+b+b,
1007,
2031-50-a-a-a-a-a-a,
2332+b+b+b+b+b+b+b+b,]


dxl_goal_positions11 = [
1058,
2059-50-a-a-a-a-a-a-a-a,
2370+b+b+b+b+b+b+b+b+b,
1008,
1902-50-a-a-a-a-a-a-a-a,
2546+b+b+b+b+b+b+b+b+b,
1007,
2031-50-a-a-a-a-a-a-a,
2332+b+b+b+b+b+b+b+b+b,]

dxl_goal_positions12 = [
1058,
2059-50-a-a-a-a-a-a-a-a-a,
2370+b+b+b+b+b+b+b+b+b+b,
1008,
1902-50-a-a-a-a-a-a-a-a-a,
2546+b+b+b+b+b+b+b+b+b+b,
1007,
2031-50-a-a-a-a-a-a-a-a,
2332+b+b+b+b+b+b+b+b+b+b,]

dxl_goal_positions13 = [
1058,
2059-50-a-a-a-a-a-a-a-a-a-a,
2370+b+b+b+b+b+b+b+b+b+b+b,
1008,
1902-50-a-a-a-a-a-a-a-a-a-a,
2546+b+b+b+b+b+b+b+b+b+b+b,
1007,
2031-50-a-a-a-a-a-a-a-a-a,
2332+b+b+b+b+b+b+b+b+b+b+b,]

dxl_goal_positions13 = [
1058,
2059-50-a-a-a-a-a-a-a-a-a-a,
2370+b+b+b+b+b+b+b+b+b+b+b,
1008,
1902-50-a-a-a-a-a-a-a-a-a-a,
2546+b+b+b+b+b+b+b+b+b+b+b,
1007,
2031-50-a-a-a-a-a-a-a-a-a,
2332+b+b+b+b+b+b+b+b+b+b+b+b,]

dxl_goal_positions14 = [
1058,
2059-50-a-a-a-a-a-a-a-a-a-a,
2370+b+b+b+b+b+b+b+b+b+b+b,
1008,
1902-50-a-a-a-a-a-a-a-a-a-a,
2546+b+b+b+b+b+b+b+b+b+b+b,
1007,
2031-50-a-a-a-a-a-a-a-a-a,
2332+b+b+b+b+b+b+b+b+b+b+b+b,]

dxl_goal_positions15 = [
1058,
2059-50-a-a-a-a-a-a-a-a-a-a-a,
2370+b+b+b+b+b+b+b+b+b+b+b+b,
1008,
1902-50-a-a-a-a-a-a-a-a-a-a-a,
2546+b+b+b+b+b+b+b+b+b+b+b+b,
1007,
2031-50-a-a-a-a-a-a-a-a-a-a-a,
2332+b+b+b+b+b+b+b+b+b+b+b+b+b,]


goals = [dxl_goal_positions1, dxl_goal_positions2, dxl_goal_positions3, dxl_goal_positions4, dxl_goal_positions5, dxl_goal_positions6, dxl_goal_positions7,dxl_goal_positions8, dxl_goal_positions9, dxl_goal_positions10, dxl_goal_positions11, dxl_goal_positions12, dxl_goal_positions13, dxl_goal_positions14, dxl_goal_positions15]

# Initialize PortHandler instance
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows
portHandler = PortHandler(DEVICENAME)

# Initialize PacketHandler instance
# Set the protocol version
# Get methods and members of Protocol1PacketHandler or Protocol2PacketHandler
packetHandler = PacketHandler(PROTOCOL_VERSION)

# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    print("Press any key to terminate...")
    getch()
    quit()


# Set port baudrate
if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    print("Press any key to terminate...")
    getch()
    quit()

# Enable Dynamixel Torque
for id in DXL_IDs:
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, id, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)    
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        print("%s" % packetHandler.getRxPacketError(dxl_error))
    else:
        print("Dynamixel has been successfully connected")


flag = 0
for goal in goals :
    for idx, position in enumerate(goal):
        dxl_id = DXL_IDs[idx]
        dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, dxl_id, ADDR_GOAL_POSITION, position)

    time.sleep(1)

# # Disable Dynamixel Torque
# dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_TORQUE_ENABLE, TORQUE_DISABLE)
# if dxl_comm_result != COMM_SUCCESS:
#     print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
# elif dxl_error != 0:
#     print("%s" % packetHandler.getRxPacketError(dxl_error))

# Close port
portHandler.closePort()
