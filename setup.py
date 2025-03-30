from setuptools import setup
import os
from glob import glob

package_name = 'takeout3week'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.rviz')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
        (os.path.join('share', package_name, 'bag'), glob('bag/*.db3')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='a',
    maintainer_email='ehdehddl7979@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            f'pointcloud_cluster = {package_name}.pointcloud_cluster:main',
            f'pointcloud_voxel = {package_name}.pointcloud_voxel:main',
            f'pointcloud_roi = {package_name}.pointcloud_roi:main',
        ],
    },
)
