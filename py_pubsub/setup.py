from setuptools import setup
import os 
from glob import glob

package_name = 'py_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch/'),
         glob('launch/*launch.[pxy][yma]*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bot',
    maintainer_email='manoj.mb.murali@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "pose_sub = py_pubsub.sub_pose:main",
            "draw_circle = py_pubsub.circle:main",
            "hello = py_pubsub.hello:main",
            "farmer1 = py_pubsub.publisher_farmer1:main",
            "farmer2 = py_pubsub.publisher_farmer2:main",
            "shop = py_pubsub.subscriber_shop:main",
            "operand = py_pubsub.publisher_operands:main",
            "operator = py_pubsub.pub_sub_operator:main",
            "output = py_pubsub.subscriber_output:main"
        ],
    },
)
