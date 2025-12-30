#!/usr/bin/env python3
import rospy, yaml, actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from std_msgs.msg import String

class Mission:
    def __init__(self):
        rospy.init_node("mission_runner")
        self.client = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        rospy.loginfo("⏳ move_base bekleniyor...")
        self.client.wait_for_server()
        rospy.loginfo("✅ move_base bağlı")

        self.qr_data = None
        rospy.Subscriber("/qr_result", String, self.qr_cb)

        with open(rospy.get_param("~mission_file")) as f:
            self.mission = yaml.safe_load(f)

        self.run()

    def qr_cb(self, msg):
        self.qr_data = msg.data

    def send_goal(self, g):
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = g["x"]
        goal.target_pose.pose.position.y = g["y"]
        goal.target_pose.pose.orientation.w = 1.0
        self.client.send_goal(goal)
        self.client.wait_for_result()

    def run(self):
        for room in self.mission["rooms"]:
            rospy.loginfo(f"🚪 Odaya gidiliyor: {room}")
            entry = self.mission[room]["entry_goal"]
            self.send_goal(entry)

            rospy.loginfo("📷 QR bekleniyor...")
            self.qr_data = None
            start = rospy.Time.now()

            while self.qr_data is None and (rospy.Time.now() - start).to_sec() < 15:
                rospy.sleep(0.2)

            if self.qr_data == self.mission[room]["qr_expected"]:
                rospy.loginfo(f"✅ {room} DOĞRULANDI")
            else:
                rospy.logwarn(f"⚠️ {room} QR OKUNAMADI")

        rospy.loginfo("🏁 MISSION COMPLETED")

if __name__ == "__main__":
    Mission()

