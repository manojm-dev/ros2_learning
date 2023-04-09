from setuptools import setup
import os 
from glob import glob

package_name = 'pub_sub_py'

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
            "pose_sub = pub_sub_py.sub_pose:main",
            "draw_circle = pub_sub_py.circle:main",
            "hello = pub_sub_py.hello:main",
            "farmer1 = pub_sub_py.publisher_farmer1:main",
            "farmer2 = pub_sub_py.publisher_farmer2:main",
            "shop = pub_sub_py.subscriber_shop:main",
            "operand = pub_sub_py.publisher_operands:main",
            "operator = pub_sub_py.pub_sub_operator:main",
            "output = pub_sub_py.subscriber_output:main"
        ],
    },
)
