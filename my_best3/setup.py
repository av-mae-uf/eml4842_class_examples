from setuptools import find_packages, setup

package_name = 'my_best3'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='carl',
    maintainer_email='carl.crane@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pub_me = my_best3.pub_pt:main',
            'lets_go = my_best3.sub_pt_pub_polar:main',
        ],
    },
)
