import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
from sensor_msgs_py import point_cloud2
import open3d as o3d
import numpy as np

class PointCloudROI(Node):
    def __init__(self):
        super().__init__('pointcloud_roi')

        self.declare_parameter('input_topic', '/input_cloud')
        self.declare_parameter('output_topic', '/roi_cloud')
        self.declare_parameter('x_min', -1.0)
        self.declare_parameter('x_max', 1.0)
        self.declare_parameter('y_min', -1.0)
        self.declare_parameter('y_max', 1.0)
        self.declare_parameter('z_min', 0.0)
        self.declare_parameter('z_max', 2.0)

        self.input_topic = self.get_parameter('input_topic').value
        self.output_topic = self.get_parameter('output_topic').value
        self.sub = self.create_subscription(PointCloud2, self.input_topic, self.cloud_callback, 10)
        self.pub = self.create_publisher(PointCloud2, self.output_topic, 10)

    def cloud_callback(self, msg):
        # Convert PointCloud2 to numpy array
        points = []
        for p in point_cloud2.read_points(msg, field_names=("x", "y", "z"), skip_nans=True):
            points.append([p[0], p[1], p[2]])
        points = np.array(points, dtype=np.float32)

        # Apply ROI filtering
        x_min, x_max = self.get_parameter('x_min').value, self.get_parameter('x_max').value
        y_min, y_max = self.get_parameter('y_min').value, self.get_parameter('y_max').value
        z_min, z_max = self.get_parameter('z_min').value, self.get_parameter('z_max').value
        mask = (points[:, 0] >= x_min) & (points[:, 0] <= x_max) & \
               (points[:, 1] >= y_min) & (points[:, 1] <= y_max) & \
               (points[:, 2] >= z_min) & (points[:, 2] <= z_max)
        filtered_points = points[mask]
        print(filtered_points)
        # Convert numpy array back to PointCloud2
        filtered_msg = point_cloud2.create_cloud_xyz32(msg.header, filtered_points)
        self.pub.publish(filtered_msg)


def main(args=None):
    rclpy.init(args=args)
    node = PointCloudROI()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
