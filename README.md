# eml4842_class_examples
This contains several ROS2 packages that demonstrate how to create publish/subscribe and client/server nodes.

## Installation/Build
- Create a development workspace by typing the following when in your home directory. Replace the text within the <> to be whatever you want.

  - mkdir -p <your_dev_ws>/src
- Move into the src directory.

  - cd <your_dev_ws>/src
- Download the repository using

  - git clone https://github.com/av-mae-uf/eml4842_class_examples.git

- Change your directory to your root workspace directory (~/<your_dev_ws>) and build the workspace.

  - colcon build
- Source your workspace with

  - source install/setup.bash

## Explanation of packages
- The pdf of a PowerPoint file provides an overview of the nodes in each package.
  - [Package_Descriptions.pdf](docs/Package_Descriptions.pdf)
- The video explains the items in the PowerPoint video.
  - [video explanation](http://www.ccrane3.com/eml4842/videos/package_descriptions.mp4)
