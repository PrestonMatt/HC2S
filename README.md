# Hilbert Curve to Sound Project
This project is inspired by the 'fantastical' (i.e. not-yet-realized) code described in this video: https://www.youtube.com/watch?v=3s7h2MHQtxc and this project: https://community.wolfram.com/groups/-/m/t/1862464

26 March 2020

## Abstract

A Hilbert curve or Hilbert space-filling curve is a family of curves that are infinite lines bend in such a way that they fill all of infinite space. These curves are named after the mathematician who discovered them, David Hilbert, as variants of Peano curves (same mathematical concept).

The use of these curves in general and in this project, is as a mapping of a two-dimensional space to a one-dimensional space, which particularly preserve location of points well. That is, as the order of the curve increases, a point on that curve gets closer and closer to a location. As the limit of the order of the curve goes to infinity, a point on this curve approaches its spot.

This is in contrast to other, more intuitive space filling curves such as the “S-Curve” described in 3Blue1Brown’s video entitled Hilbert's Curve: Is infinite math useful? where said curve does not preserve locality of a point.

## Concrete Problem Statement

In this project, my initial goals are to:
1.	Program a (scalable) algorithm that parses a square image using a pseudo-Hilbert curve without using outside modules.
2.	Take that parsed data and transform it into a sound with frequencies mapped to color and brightness mapped to volume.
3.	Take a sound bit encoded the same as above and decode it back into an image.
4.	Make this application usable with a passible user interface/GUI.

My stretch goals are to:
1.	See if I can use a combination of Fourier Transform and machine learning libraries in the SKLearn module to try to classify these ‘images-as-sounds’.
  -	For example, we can train neural networks to identify things like a bee versus a three. What about when these images are encoded as sounds? Does that make it easier or harder for an ML model to classify?
2.	Scale the Hilbert Curve tracer to parse non-square image files.
3.	Give the program a function to use differently shaped curves; in looking at pictures of Peano’s and Hilbert’s different curves you’ll see what I mean.
4.	Create a tutorial for the user to try to get a grasp on trying to ‘see’ with sound.

## Potential Challenges

The challenges I foresee in this project are the meat of the issue. Creating a pathfinding Hilbert curve from scratch will be difficult, especially trying to make it iterative and non-exponential as I try to scale curves from one order to the next.

In addition, mapping the colors and brightness to sound in an *intuitive* manner will be a design challenge as I try to make it as easy as possible for a layman to get the grasp of an image through just a sound bit. 

## Potential Applications

This application may be useful as:
  - A tool in research on brain plasticity. Scientists are trying to answer and experiment with ideas and questions on just what auditory and visual cortexes can do, and the limits of how ‘plastic’ our brains are: http://web.mit.edu/surlab/publications/Newton_Sur04.pdf
  - A tool in image processing research. If indeed it’s true that ML models can more easily classify images when they’re encoded to sound than as they are as pictures, then it might speed up scientific research that right now has tons of image data that necessitates machine learning. For example the problem as discussed in this video: https://www.youtube.com/watch?v=tSoqJpisKIg

## Works Cited

Sanderson, Grant. “Hilbert's Curve: Is infinite math useful?” *YouTube*, uploaded by 3Blue1Brown, 21 July 2017, https://www.youtube.com/watch?v=3s7h2MHQtxc.

Rangan, Srinath “Using Pseudo-Hilbert Curves to Assist People Perceive Images via Sound.” *Wolfram Community*, January 2020, https://community.wolfram.com/groups/-/m/t/1862464.

Newton, Jessica R. and Sur, Mriganka. “REWIRING CORTEX: FUNCTIONAL PLASTICITY OF THE AUDITORY CORTEX DURING DEVELOPMENT.” *Department of Brain & Cognitive Sciences, Picower Center for Learning & Memory*, Massachusetts Institute of Technology http://web.mit.edu/surlab/publications/Newton_Sur04.pdf. Accessed 28 March 2020.

Yoshida, Kate. “Can AI Help Us Identify Animals?”. *YouTube*, uploaded by MinuteEarth, 3 December 2019, https://www.youtube.com/watch?v=tSoqJpisKIg.
