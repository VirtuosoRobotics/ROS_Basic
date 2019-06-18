#include "ros/ros.h"
#include "std_msgs/String.h"
#include "pub_n_sub/Num.h"

void chatterCallback(const pub_n_sub::Num::ConstPtr &msg)
{
    std::cout<<*msg<<std::endl;
}

int main(int argc, char **argv)
{

    ros::init(argc, argv, "listener");
    ros::NodeHandle n;

    ros::Subscriber sub = n.subscribe("custom_msg", 1000, chatterCallback);

    ros::spin();

    return 0;
}
