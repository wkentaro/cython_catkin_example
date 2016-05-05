cython_catkin_example
=====================

.. image:: https://travis-ci.org/wkentaro/cython_catkin_example.svg?branch=master
    :target: https://travis-ci.org/wkentaro/cython_catkin_example


Simple example of Catkin + Cython.


Usage
-----

.. code-block:: bash

  $ cd ~/catkin_ws/src
  $ git clone https://github.com/wkentaro/cython_catkin_example.git
  $ cd cython_catkin_example

  $ catkin bt -iv

  $ python
  >>> from cython_catkin_example.add_ints import add_ints
  >>> add_ints
  <module 'cython_catkin_example.add_ints' from '/home/wkentaro/ros/cython_ws/devel/lib/python2.7/dist-packages/cython_catkin_example/add_ints.so'>
  >>> add_ints.add_ints(1, 3)
  4
