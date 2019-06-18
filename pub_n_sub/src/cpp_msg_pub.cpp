#include "ros/ros.h"
#include "std_msgs/String.h"
#include "pub_n_sub/Num.h"
#include <sstream>

int main(int argc, char **argv)
{
	ros::init(argc, argv, "talker");
	ros::NodeHandle n;

	ros::Publisher chatter_pub = n.advertise<pub_n_sub::Num>("custom_msg", 1000);
	ros::Rate loop_rate(10);
	int count = 0;

	while (ros::ok())
	{
		pub_n_sub::Num msg;
        msg.first_name = "pika";
        msg.last_name = "chu";
        msg.age = 8;
        msg.score = 87;
        std::cout<<msg<<std::endl;
		chatter_pub.publish(msg);
		ros::spinOnce();
		loop_rate.sleep();
		++count;
	}

	return 0;
}