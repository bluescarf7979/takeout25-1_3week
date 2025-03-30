import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
from sensor_msgs_py import point_cloud2
import numpy as np
from sklearn.cluster import DBSCAN

class PointCloudCluster(Node):
    def __init__(self):
        super().__init__('pointcloud_cluster')

        # 파라미터 선언
        self.declare_parameter('input_topic', '/input_cloud')
        self.declare_parameter('output_topic', '/cluster_centroids')
        self.declare_parameter('cluster_tolerance', 0.05)
        self.declare_parameter('min_cluster_size', 100)
        self.declare_parameter('max_cluster_size', 25000)

        self.input_topic = self.get_parameter('input_topic').value
        self.output_topic = self.get_parameter('output_topic').value
        self.cluster_tolerance = self.get_parameter('cluster_tolerance').value
        self.min_cluster_size = self.get_parameter('min_cluster_size').value
        self.max_cluster_size = self.get_parameter('max_cluster_size').value

        self.sub = self.create_subscription(PointCloud2, self.input_topic, self.cloud_callback, 10)
        self.pub = self.create_publisher(PointCloud2, self.output_topic, 10)

    def cloud_callback(self, msg):
        # PointCloud2 -> numpy array 변환
        points = []
        for p in point_cloud2.read_points(msg, field_names=("x", "y", "z"), skip_nans=True):
            points.append([p[0], p[1], p[2]])
        points = np.array(points, dtype=np.float32)

        # DBSCAN을 사용한 클러스터링
        clustering = DBSCAN(eps=self.cluster_tolerance, min_samples=self.min_cluster_size).fit(points)
        labels = clustering.labels_

        # 클러스터 중심 계산 및 필터링
        unique_labels = set(labels)
        cluster_centroids = []
        for label in unique_labels:
            if label == -1:
                continue  # 노이즈 제거
            cluster = points[labels == label]
            if self.min_cluster_size <= len(cluster) <= self.max_cluster_size:
                centroid = np.mean(cluster, axis=0)
                cluster_centroids.append(centroid)

        cluster_centroids = np.array(cluster_centroids, dtype=np.float32)

        # numpy array -> PointCloud2 변환 및 publish
        centroids_msg = point_cloud2.create_cloud_xyz32(msg.header, cluster_centroids)
        self.pub.publish(centroids_msg)


def main(args=None):
    rclpy.init(args=args)
    node = PointCloudCluster()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
