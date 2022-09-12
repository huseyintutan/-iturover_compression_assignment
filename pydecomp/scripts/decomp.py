#!/usr/bin/env python

# @author huseyintutan

# iturover team software subteam assignment part 1

import rospy
from std_msgs.msg import String
from std_msgs.msg import Char
import bz2
import binascii
import collections

       
def callback(data):
    msg=data.data
    rospy.logwarn("BZ2 De-Compress Subscriber Node Started!")
    unhexlified_msg = binascii.unhexlify(msg)
    rospy.logerr(unhexlified_msg)
    decompressed_msg = bz2.decompress(unhexlified_msg)
    rospy.logerr(decompressed_msg)
    answer=(collections.Counter(decompressed_msg).most_common(1)[0])
    rospy.loginfo(answer[0])
    pub.publish(answer[0])

rospy.init_node("decomp", anonymous=True)
pub=rospy.Publisher("solution", Char, queue_size=10)
sub=rospy.Subscriber("/bz2_message", String, callback)

rospy.Rate(1)

rospy.spin()

  
