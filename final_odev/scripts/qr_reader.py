#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from pyzbar import pyzbar
import cv2
from std_msgs.msg import String

class QRReader:
    def __init__(self):
        rospy.init_node("qr_reader")
        self.bridge = CvBridge()
        self.pub = rospy.Publisher("/qr_result", String, queue_size=10)
        rospy.Subscriber("/camera/rgb/image_raw", Image, self.image_cb)
        rospy.loginfo("📷 QR Reader başladı")
        rospy.spin()

    def image_cb(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        barcodes = pyzbar.decode(frame)

        for barcode in barcodes:
            data = barcode.data.decode("utf-8")
            rospy.loginfo(f"✅ QR OKUNDU: {data}")
            self.pub.publish(data)

if __name__ == "__main__":
    QRReader()

