# udooneo_motorControl
ROS package for UDOO NEO that sends /cmd_vel messages to the CORTEX M4

Subscribes to /cmd_vel (geometry_msgs Twis) and reads the messages. Currently understands only velocity between +/- 1 and it does not take into account the dimesion of the robot.
