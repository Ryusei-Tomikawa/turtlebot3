#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import math

import rospy
import actionlib
import moveit_commander

from geometry_msgs.msg import Quaternion, PoseStamped
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from tf.transformations import quaternion_from_euler

######################################
# GLOBAL
######################################
waypoints = [
	[(0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 1.0)], # init
	[(-1.852, 3.1, 0), (0, 0, 0.7070, 0.7070)] # goal
]


def euler_to_quaternion(role, pitch, yaw):
	q = quaternion_from_euler(role, pitch, yaw)
	return Quaternion(q[0], q[1], q[2], q[3])


def goal_pose(pose):
	goal_pose = MoveBaseGoal()
	goal_pose.target_pose.header.frame_id = "map"
	goal_pose.target_pose.pose.position.x = pose[0][0]
	goal_pose.target_pose.pose.position.y = pose[0][1]
	goal_pose.target_pose.pose.position.z = pose[0][2]
	goal_pose.target_pose.pose.orientation.x = pose[1][0]
	goal_pose.target_pose.pose.orientation.y = pose[1][1]
	goal_pose.target_pose.pose.orientation.z = pose[1][2]
	goal_pose.target_pose.pose.orientation.w = pose[1][3]

	return goal_pose


def main():

	rospy.init_node("navigation")

	client = actionlib.SimpleActionClient("move_base", MoveBaseAction)
	client.wait_for_server()

	for i, pose in enumerate(waypoints):
		goal = goal_pose(pose)
		client.send_goal(goal)
		client.wait_for_result()

if __name__ == "__main__":
	try:
		main()
	except rospy.ROSInterruptException:
		exit()
