import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
from sensor_msgs_py import point_cloud2
import open3d as o3d
import numpy as np
import struct

class PointCloudVoxel(Node):
    def __init__(self):
        super().__init__('pointcloud_voxel')

        self.declare_parameter('input_topic', '/input_cloud')
        self.declare_parameter('output_topic', '/voxel_downsampled_cloud')
        self.declare_parameter('voxel_size', 0.05)

        self.input_topic = self.get_parameter('input_topic').value
        self.output_topic = self.get_parameter('output_topic').value
        self.voxel_size = self.get_parameter('voxel_size').value

        self.sub = self.create_subscription(PointCloud2, self.input_topic, self.cloud_callback, 10)
        self.pub = self.create_publisher(PointCloud2, self.output_topic, 10)

    def cloud_callback(self, msg):
        # Convert PointCloud2 to numpy array manually
        points = []
        for p in point_cloud2.read_points(msg, field_names=("x", "y", "z"), skip_nans=True):
            points.append([p[0], p[1], p[2]])
        points = np.array(points, dtype=np.float32)

        # Convert numpy array to Open3D point cloud
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(points)

        # Apply voxel downsampling
        downsampled_pcd = pcd.voxel_down_sample(voxel_size=self.voxel_size)

        # Convert Open3D point cloud back to numpy array
        downsampled_points = np.asarray(downsampled_pcd.points, dtype=np.float32)

        # Convert numpy array to PointCloud2 message
        downsampled_msg = point_cloud2.create_cloud_xyz32(msg.header, downsampled_points)

        self.pub.publish(downsampled_msg)


def main(args=None):
    rclpy.init(args=args)
    node = PointCloudVoxel()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
